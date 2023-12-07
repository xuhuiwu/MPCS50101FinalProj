# Python Command Line Task Manager

## Description
This Python Command Line Task Manager allows you to manage your tasks directly from the command line. You can add, delete, list, query, mark tasks as done, and generate reports. The data is stored in a hidden `.todo.pickle` file in the user's home directory.

## Usage

### Running the Program
Use the following commands to manage your tasks:

- Add a task:
  ```
  python todo.py --add "Task Name" --due "Due Date" --priority [1-3]
  ```

- Delete a task:
  ```
  python todo.py --delete [Task ID]
  ```

- List tasks:
  ```
  python todo.py --list
  ```

- Query tasks:
  ```
  python todo.py --query "Search Term"
  ```

- Mark a task as done:
  ```
  python todo.py --done [Task ID]
  ```

- Generate a task report:
  ```
  python todo.py --report
  ```
