import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file]
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to remove: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")