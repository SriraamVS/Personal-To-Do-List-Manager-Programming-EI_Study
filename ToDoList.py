from datetime import datetime

# Task class to represent individual tasks
class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.completed = False
        self.due_date = due_date

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - {status}, Due: {self.due_date}" if self.due_date else f"{self.description} - {status}"

# ToDoList class to manage tasks and interact with the user
class ToDoList:
    def __init__(self, filename):
        self.tasks = []  # List to store tasks
        self.filename = filename  # File to store tasks
        self.load_tasks()  # Load tasks from file when instantiated

    def add_task(self):
        # Function to add a new task to the list
        description = input("Enter task description: ")
        due_date_input = input("Enter due date (YYYY-MM-DD) or leave blank: ")
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d") if due_date_input else None
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        self.save_tasks()  # Save tasks to file after adding a new task
        print("Task added successfully!")

    def mark_completed(self):
        # Function to mark a task as completed
        pending_tasks = [task for task in self.tasks if not task.completed]
        if not pending_tasks:
            print("No pending tasks.")
            return

        print("Pending Tasks:")
        for idx, task in enumerate(pending_tasks, start=1):
            print(f"{idx}. {task}")

        task_number = input("Enter the number of the task to mark as completed: ")
        try:
            task_index = int(task_number) - 1
            if 0 <= task_index < len(pending_tasks):
                pending_tasks[task_index].mark_completed()
                self.save_tasks()  # Save tasks after marking a task as completed
                print(f"Task '{pending_tasks[task_index].description}' marked as completed.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        # Function to delete a task from the list
        description = input("Enter task description to delete: ")
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                self.save_tasks()  # Save tasks after deleting a task
                print(f"Task '{description}' deleted successfully.")
                return
        print(f"Task '{description}' not found!")

    def view_tasks(self):
        # Function to view tasks based on a filter
        filter_type = input("Filter tasks (all/completed/pending): ").lower()
        if filter_type == 'all':
            tasks = self.tasks
        elif filter_type == 'completed':
            tasks = [task for task in self.tasks if task.completed]
        elif filter_type == 'pending':
            tasks = [task for task in self.tasks if not task.completed]
        else:
            print("Invalid filter type! Showing all tasks")
            tasks = self.tasks

        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found for the specified filter")

    def load_tasks(self):
        # Function to load tasks from a file
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    description = parts[0]
                    completed = parts[1] == 'True'
                    due_date = datetime.strptime(parts[2], "%Y-%m-%d") if parts[2] != 'None' else None
                    task = Task(description, due_date)
                    task.completed = completed
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        # Function to save tasks to a file
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed},{task.due_date}\n")

# Main program execution
if __name__ == "__main__":
    todo_list = ToDoList("tasks.txt")  # Initialize the ToDoList with a file containing tasks

    while True:
        print("\n ----- To-Do List Manager -----")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.add_task()
        elif choice == '2':
            todo_list.mark_completed()
        elif choice == '3':
            todo_list.delete_task()
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please Enter a no. between 1 and 5")
