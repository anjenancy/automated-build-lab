class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append({"task": task, "status": "Pending"})
            return "Task added"
        return "Invalid task"

    def view_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = "Completed"
            return "Task completed"
        return "Task not found"

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return "Task deleted"
        return "Task not found"


def main():
    manager = TaskManager()

    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            print(manager.add_task(task))

        elif choice == "2":
            tasks = manager.view_tasks()
            if not tasks:
                print("No tasks available")
            else:
                for i, t in enumerate(tasks):
                    print(f"{i+1}. {t['task']} - {t['status']}")

        elif choice == "3":
            index = int(input("Enter task number: ")) - 1
            print(manager.complete_task(index))

        elif choice == "4":
            index = int(input("Enter task number: ")) - 1
            print(manager.delete_task(index))

        elif choice == "5":
            print("Exiting program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
