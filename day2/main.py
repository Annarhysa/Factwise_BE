from project_board_base import ProjectBoardBase
from team_base import TeamBase
from user_base import UserBase
import json

def main():
    project_board = ProjectBoardBase()
    team = TeamBase()
    user = UserBase()

    # Create a team
    team_id = json.loads(team.create_team('{"name": "Team A", "description": "Description of Team A", "admin": "admin_id"}'))['id']
    print(f"Created team with ID: {team_id}")

    # Create a user
    user_id = json.loads(user.create_user('{"name": "user1", "display_name": "User One"}'))['id']
    print(f"Created user with ID: {user_id}")

    # Create a board
    board_id = json.loads(project_board.create_board('{"name": "Board 1", "description": "Description of Board 1", "team_id": "' + team_id + '", "creation_time": "2024-07-15T12:00:00"}'))['id']
    print(f"Created board with ID: {board_id}")

if __name__ == "__main__":
    main()
