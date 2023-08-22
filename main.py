from task import Task
import json
import json

def save_tasks():
    with open("tasks.json", "w") as file:
        task_data = [{"title": task.title, "description": task.description, "completed": task.completed} for task in tasks]
        json.dump(task_data, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            task_data = json.load(file)
            tasks.extend([Task(task["title"], task["description"]) for task in task_data])
    except FileNotFoundError:
        pass  # No tasks saved yet

tasks = []


def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(title, description)
    tasks.append(task)
    print("Task added successfully!")


def list_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"Task {index}:\n{task.format_task()}\n")


def mark_completed():
    list_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_index].mark_completed()
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid input or task number.")


def main():
    print("Welcome to the Task Tracker Application!")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
