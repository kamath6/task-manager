import json
import os

FILE = "tasks.json"

class TaskManager:

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "status": "Pending"
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(f'ID: {task["id"]} | Title: {task["title"]} | Status: {task["status"]}')

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                self.save_tasks()
                print("Task marked as completed!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()
        print("Task deleted successfully!")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Smart Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter Task ID: "))
            manager.mark_completed(task_id)

        elif choice == "4":
            task_id = int(input("Enter Task ID: "))
            manager.delete_task(task_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
