import argparse
import pickle
from datetime import datetime

class Task:
    """Representation of a task
  
    Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    """

    unique_id_counter = 0

    def __init__(self, name, priority=1, due_date=None):
        self.created = datetime.now()
        self.completed = None
        self.name = name
        self.unique_id = Task.unique_id_counter
        Task.unique_id_counter += 1
        self.priority = priority
        self.due_date = due_date

    def complete(self):
        self.completed = datetime.now()

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.unique_id}: {self.name}, Priority: {self.priority}, Status: {status}, Created: {self.created.strftime('%Y-%m-%d')}, Due: {self.due_date}, Completed: {self.completed}"

class Tasks:
    """A list of `Task` objects."""
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = []
        self.load_tasks()

    def add_task(self, name, priority=1, due_date=None):
        new_task = Task(name, priority, due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task.unique_id

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.unique_id != task_id]
        self.save_tasks()

    def list_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def save_tasks(self):
        with open('.todo.pickle', 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open('.todo.pickle', 'rb') as f:
                self.tasks = pickle.load(f)
        except FileNotFoundError:
            self.tasks = []

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.unique_id == task_id:
                task.complete()
                break
        self.save_tasks()

    def query_tasks(self, search_terms):
        return [task for task in self.tasks if any(term in task.name for term in search_terms)]

    def report_tasks(self):
        return self.tasks

def parse_arguments():
    parser = argparse.ArgumentParser(description="Task Manager")
    parser.add_argument('--add', nargs='+', help="Add a new task")
    parser.add_argument('--delete', type=int, help="Delete a task by ID")
    parser.add_argument('--list', action='store_true', help="List all tasks")
    parser.add_argument('--done', type=int, help="Mark a task as completed by ID")
    parser.add_argument('--query', nargs='+', help="Query tasks based on keywords")
    parser.add_argument('--report', action='store_true', help="Report all tasks")
    return parser.parse_args()

def main():
    args = parse_arguments()
    task_manager = Tasks()

    if args.add:
        name = ' '.join(args.add[:-2])
        priority = int(args.add[-2])
        due_date = args.add[-1]
        task_id = task_manager.add_task(name, priority, due_date)
        print(f"Created task {task_id}")

    elif args.delete:
        task_manager.delete_task(args.delete)
        print(f"Deleted task {args.delete}")

    elif args.list:
        for task in task_manager.list_tasks():
            print(task)

    elif args.done:
        task_manager.mark_completed(args.done)
        print(f"Completed task {args.done}")

    elif args.query:
        for task in task_manager.query_tasks(args.query):
            print(task)

    elif args.report:
        for task in task_manager.report_tasks():
            print(task)

    task_manager.save_tasks()

if __name__ == "__main__":
    main()
