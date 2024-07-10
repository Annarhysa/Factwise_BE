import json
import os
import uuid
from datetime import datetime

class ProjectBoardBase:
    def __init__(self):
        self.boards_file = 'db/boards.json'
        self.tasks_file = 'db/tasks.json'

    def create_board(self, request: str):
        data = self._read_data(self.boards_file)
        req = json.loads(request)

        if len(req['name']) > 64 or len(req['description']) > 128:
            raise ValueError("Board name or description length exceeded")

        if any(board['name'] == req['name'] for board in data.values() if board['team_id'] == req['team_id']):
            raise ValueError("Board name must be unique for a team")

        board_id = str(uuid.uuid4())
        data[board_id] = {
            "id": board_id,
            "name": req['name'],
            "description": req['description'],
            "team_id": req['team_id'],
            "creation_time": req['creation_time'],
            "status": "OPEN",
            "tasks": []
        }
        self._write_data(self.boards_file, data)
        return json.dumps({"id": board_id})

    def close_board(self, request: str) -> str:
        data = self._read_data(self.boards_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("Board not found")

        board = data[req['id']]
        if board['status'] == "CLOSED":
            raise ValueError("Board is already closed")

        tasks = self._read_data(self.tasks_file)
        if any(task['status'] != "COMPLETE" for task in tasks.values() if task['board_id'] == req['id']):
            raise ValueError("All tasks must be marked as COMPLETE to close the board")

        board['status'] = "CLOSED"
        board['end_time'] = datetime.now().isoformat()
        self._write_data(self.boards_file, data)
        return json.dumps({"status": "Board closed"})

    def add_task(self, request: str) -> str:
        boards = self._read_data(self.boards_file)
        tasks = self._read_data(self.tasks_file)
        req = json.loads(request)

        board = boards.get(req['board_id'])
        if not board or board['status'] != "OPEN":
            raise ValueError("Task can only be added to an OPEN board")

        if len(req['title']) > 64 or len(req['description']) > 128:
            raise ValueError("Task title or description length exceeded")

        if any(task['title'] == req['title'] for task in tasks.values() if task['board_id'] == req['board_id']):
            raise ValueError("Task title must be unique within a board")

        task_id = str(uuid.uuid4())
        tasks[task_id] = {
            "id": task_id,
            "title": req['title'],
            "description": req['description'],
            "user_id": req['user_id'],
            "board_id": req['board_id'],
            "creation_time": req['creation_time'],
            "status": "OPEN"
        }
        board['tasks'].append(task_id)
        self._write_data(self.boards_file, boards)
        self._write_data(self.tasks_file, tasks)
        return json.dumps({"id": task_id})

    def update_task_status(self, request: str):
        tasks = self._read_data(self.tasks_file)
        req = json.loads(request)

        if req['id'] not in tasks:
            raise ValueError("Task not found")

        tasks[req['id']]['status'] = req['status']
        self._write_data(self.tasks_file, tasks)
        return json.dumps({"status": "Task status updated"})

    def list_boards(self, request: str) -> str:
        boards = self._read_data(self.boards_file)
        req = json.loads(request)

        open_boards = [
            {"id": board_id, "name": board['name']}
            for board_id, board in boards.items()
            if board['team_id'] == req['id'] and board['status'] == "OPEN"
        ]
        return json.dumps(open_boards)

    def export_board(self, request: str) -> str:
        boards = self._read_data(self.boards_file)
        tasks = self._read_data(self.tasks_file)
        req = json.loads(request)

        board = boards.get(req['id'])
        if not board:
            raise ValueError("Board not found")

        board_tasks = [
            {"id": task_id, **task}
            for task_id, task in tasks.items()
            if task['board_id'] == req['id']
        ]

        output = f"Board: {board['name']}\nDescription: {board['description']}\nTasks:\n"
        for task in board_tasks:
            output += f" - {task['title']}: {task['description']} (Status: {task['status']})\n"

        output_file = f"out/board_{req['id']}.txt"
        with open(output_file, 'w') as file:
            file.write(output)

        return json.dumps({"out_file": output_file})

    def _read_data(self, file_path):
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r') as file:
            return json.load(file)

    def _write_data(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
