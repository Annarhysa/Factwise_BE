import json
import os
import uuid
from datetime import datetime

class TeamBase:
    def __init__(self):
        self.teams_file = 'db/teams.json'
        self.users_file = 'db/users.json'

    def create_team(self, request: str) -> str:
        data = self._read_data(self.teams_file)
        req = json.loads(request)

        if len(req['name']) > 64 or len(req['description']) > 128:
            raise ValueError("Team name or description length exceeded")

        if any(team['name'] == req['name'] for team in data.values()):
            raise ValueError("Team name must be unique")

        team_id = str(uuid.uuid4())
        data[team_id] = {
            "id": team_id,
            "name": req['name'],
            "description": req['description'],
            "admin": req['admin'],
            "creation_time": datetime.now().isoformat(),
            "members": []
        }
        self._write_data(self.teams_file, data)
        return json.dumps({"id": team_id})

    def list_teams(self) -> str:
        data = self._read_data(self.teams_file)
        return json.dumps(list(data.values()))

    def describe_team(self, request: str) -> str:
        data = self._read_data(self.teams_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("Team not found")

        return json.dumps(data[req['id']])

    def update_team(self, request: str) -> str:
        data = self._read_data(self.teams_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("Team not found")

        if len(req['team']['name']) > 64 or len(req['team']['description']) > 128:
            raise ValueError("Team name or description length exceeded")

        if any(team['name'] == req['team']['name'] and team_id != req['id'] for team_id, team in data.items()):
            raise ValueError("Team name must be unique")

        data[req['id']].update(req['team'])
        self._write_data(self.teams_file, data)
        return json.dumps({"status": "Team updated"})

    def add_users_to_team(self, request: str):
        data = self._read_data(self.teams_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("Team not found")

        current_members = set(data[req['id']]['members'])
        new_members = req['users']

        if len(current_members) + len(new_members) > 50:
            raise ValueError("Cannot add more than 50 users to a team")

        data[req['id']]['members'] = list(current_members.union(set(new_members)))
        self._write_data(self.teams_file, data)
        return json.dumps({"status": "Users added to team"})

    def remove_users_from_team(self, request: str):
        data = self._read_data(self.teams_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("Team not found")

        current_members = set(data[req['id']]['members'])
        users_to_remove = req['users']

        data[req['id']]['members'] = list(current_members.difference(set(users_to_remove)))
        self._write_data(self.teams_file, data)
        return json.dumps({"status": "Users removed from team"})

    def list_team_users(self, request: str) -> str:
        data = self._read_data(self.teams_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("Team not found")

        team_members = [
            {"id": user_id, **user}
            for user_id, user in self._read_data(self.users_file).items()
            if user_id in data[req['id']]['members']
        ]

        return json.dumps(team_members)

    def _read_data(self, file_path):
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r') as file:
            return json.load(file)

    def _write_data(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
