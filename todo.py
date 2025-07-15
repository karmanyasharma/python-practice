import os
import json

TODO_FILE = "todo.json"  # ✅ Better name

def load_task():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # If file is empty or invalid, return empty list
    else:
        return []


def save_task(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = input("Enter Task: ")
    tasks = load_task()
    tasks.append({"description": task, "done": False})
    save_task(tasks)
    print("✅ Task added.")

def view_tasks():
    tasks = load_task()
    if not tasks:
        print("No tasks found!")
        return
    print("📋 Your tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['description']}")

def delete_task():
    tasks = load_task()
    if not tasks:
        print("No tasks to delete!")
        return
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            save_task(tasks)
            print(f"🗑️ Deleted: {deleted['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    tasks = load_task()
    if not tasks:
        print("No tasks to mark!")
        return
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_task(tasks)
            print(f"✅ Marked as done: {tasks[num - 1]['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n==== To-Do Menu ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
