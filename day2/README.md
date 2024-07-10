# Team Project Planner Tool
Name: Annarhysa Albert\
Register No: RA2111047010144\
Course: BTech Artificial Intelligence\
Campus: SRMIST Ktr

## Overview

The Team Project Planner Tool provides APIs to manage users, teams, team boards, and tasks within a board. This tool uses local file storage for persistence and interacts with users through JSON-formatted APIs.

## Directory Structure

- `project_board_base.py`: Contains the base class for managing project boards.
- `team_base.py`: Contains the base class for managing teams.
- `user_base.py`: Contains the base class for managing users.
- `main.py`: To run the whole management system.
- `README.md`: A project summary and the rationale behind design choices.
- `requirements.txt`: Lists dependencies required for the project.
- `db`: Folder for storing persistence data (will be excluded from the final submission zip).

## Design Choices
1. **Persistence**: JSON files are used for local storage to keep the implementation simple and easy to manage. The `db` folder contains `users.json`, `teams.json`, and `boards.json` to store users, teams, and board data, respectively.
2. **API Design**: The APIs accept and return JSON strings, making integrating with other systems or front-end applications easy.
3. **Constraints Handling**: All constraints mentioned in the method docstrings are strictly enforced. Exceptions are raised for invalid inputs to ensure data integrity and consistency.
4. **Structure**: The directory is organized to separate base classes and their concrete implementations. The `main.py` file can be used to demonstrate the functionality of the APIs.

## Assumptions
1. **Current Time**: In the absence of a proper datetime input, "current_time" is used as a placeholder. In a real implementation, a datetime library would be used to fetch the current time.
2. **Task Management**: The implementation for task management within boards is partially complete and can be extended as needed.

## Installation

1. Clone the repository.
   ```sh
   git clone https://github.com/Annarhysa/RA2111047010144_Factwise_BE.git
   ```
   
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### 1. User Management
- Create User: Create a new user with a unique name.
- List Users: List all existing users.
- Describe User: Provide details of a specific user.
- Update User: Update user details.
- Get User Teams: List all teams a user is part of.

### 2. Team Management
- Create Team: Create a new team with a unique name.
- List Teams: List all existing teams.
- Describe Team: Provide details of a specific team.
- Update Team: Update team details.
- Add Users to Team: Add users to a team, with a maximum limit of 50 users.
- Remove Users from Team: Remove users from a team.
- List Team Users: List all users of a team.

### 3. Board and Task Management
- Create Board: Create a new board for a team, ensuring board name uniqueness within the team.
- Close Board: Close a board, ensuring all tasks are marked as complete.
- Add Task: Add a new task to an open board.
- Update Task Status: Update the status of a task.
- List Boards: List all open boards for a team.
- Export Board: Export a board's details to a text file.

## Thought Process
1. JSON for Persistence: JSON is human-readable, easy to parse, and works well for the hierarchical data structure required for users, teams, boards, and tasks.
2. UUID for IDs: Using UUIDs ensures unique identifiers for users, teams, boards, and tasks across the application.
3. Error Handling: Each API method includes checks and raises exceptions for invalid inputs, ensuring data integrity and robustness.
4. Modular Design: Separating user, team, and board management into different classes promotes modularity and makes the codebase easier to maintain and extend.

## Testing
1. Create the db folder to store JSON files

2. Run the main.py file
```sh
python main.py file
```

3. The stored users, teams and boards data can be seen in json format in the db file now.

## Future Improvements
1. Implement task management APIs in `project_board.py`.
2. Add logging for better debugging and monitoring.
3. Implement unit tests to ensure code reliability.
4. Enhance the `export_board` method to create a more presentable output.
