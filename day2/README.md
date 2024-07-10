# Team Project Planner Tool
Name: Annarhysa Albert
Register No: RA2111047010144
Course: BTech Artificial Intelligence
Campus: SRMIST Ktr

## Overview

The Team Project Planner Tool provides APIs to manage users, teams, team boards, and tasks within a board. This tool uses local file storage for persistence and interacts with users through JSON-formatted APIs.

## Directory Structure

- `project_board_base.py`: Contains the base class for managing project boards.
- `team_base.py`: Contains the base class for managing teams.
- `user_base.py`: Contains the base class for managing users.
- `user.py`: Implements user management functionalities.
- `team.py`: Implements team management functionalities.
- `project_board.py`: Implements board and task management functionalities.
- `README.md`: Contains a summary of the project and the rationale behind design choices.
- `requirements.txt`: Lists dependencies required for the project.
- `db`: Folder for storing persistence data (will be excluded from the final submission zip).

## Installation

1. Clone the repository.
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt

## Usage
1. User Management
- Create User: Create a new user with a unique name.
- List Users: List all existing users.
- Describe User: Provide details of a specific user.
- Update User: Update user details.
- Get User Teams: List all teams a user is part of.

2. Team Management
- Create Team: Create a new team with a unique name.
- List Teams: List all existing teams.
- Describe Team: Provide details of a specific team.
- Update Team: Update team details.
- Add Users to Team: Add users to a team, with a maximum limit of 50 users.
- Remove Users from Team: Remove users from a team.
- List Team Users: List all users of a team.

3. Board and Task Management
- Create Board: Create a new board for a team, ensuring board name uniqueness within the team.
- Close Board: Close a board, ensuring all tasks are marked as complete.
- Add Task: Add a new task to an open board.
- Update Task Status: Update the status of a task.
- List Boards: List all open boards for a team.
- Export Board: Export a board's details to a text file.
- Thought Process and Design Choices

4. JSON for Persistence: JSON is human-readable, easy to parse, and works well for the hierarchical data structure required for users, teams, boards, and tasks.

5. UUID for IDs: Using UUIDs ensures unique identifiers for users, teams, boards, and tasks across the application.

6. Error Handling: Each API method includes checks and raises exceptions for invalid inputs, ensuring data integrity and robustness.

7. Modular Design: Separating user, team, and board management into different classes promotes modularity and makes the codebase easier to maintain and extend.

## Testing
Run the unit tests to ensure the correctness of each API method and handle edge cases.

sh
Copy code
# Example: running tests
python -m unittest discover -s tests
Packaging
Prepare the final project for submission by creating a zip file excluding the db folder and any installed libraries.

bash
Copy code

### `requirements.txt`

```text
# List dependencies required for the project
This implementation should cover the full functionality of the team project planner tool, ensuring that all the specified requirements are met.