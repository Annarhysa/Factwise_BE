import json
import os
import uuid
from datetime import datetime

class UserBase:
    def __init__(self):
        self.users_file = 'db/users.json'

    def create_user(self, request: str) -> str:
        data = self._read_data(self.users_file)
        req = json.loads(request)

        if len(req['name']) > 64 or len(req['display_name']) > 64:
            raise ValueError("User name or display name length exceeded")

        if any(user['name'] == req['name'] for user in data.values()):
            raise ValueError("User name must be unique")

        user_id = str(uuid.uuid4())
        data[user_id] = {
            "id": user_id,
            "name": req['name'],
            "display_name": req['display_name'],
            "creation_time": datetime.now().isoformat()
        }
        self._write_data(self.users_file, data)
        return json.dumps({"id": user_id})

    def list_users(self) -> str:
        data = self._read_data(self.users_file)
        return json.dumps(list(data.values()))

    def describe_user(self, request: str) -> str:
        data = self._read_data(self.users_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("User not found")

        return json.dumps(data[req['id']])

    def update_user(self, request: str) -> str:
        data = self._read_data(self.users_file)
        req = json.loads(request)

        if req['id'] not in data:
            raise ValueError("User not found")

        if len(req['user']['display_name']) > 128:
            raise ValueError("Display name length exceeded")

        data[req['id']]['display_name'] = req['user']['display_name']
        self._write_data(self.users_file, data)
        return json.dumps({"status": "User updated"})

    def get_user_teams(self, request: str) -> str:
        user_id = json.loads(request)['id']
        teams_data = self._read_data('db/teams.json')
        user_teams = [
            {"id": team_id, **team}
            for team_id, team in teams_data.items()
            if user_id in team['members']
        ]
        return json.dumps(user_teams)

    def _read_data(self, file_path):
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r') as file:
            return json.load(file)

    def _write_data(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
