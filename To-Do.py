import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)

        elif choice == '2':
            show_tasks(tasks)

        elif choice == '3':
            show_tasks(tasks)
            num = int(input("Enter task number to mark as done: "))
            if 0 < num <= len(tasks):
                tasks[num - 1] += " ✅"
                save_tasks(tasks)

        elif choice == '4':
            show_tasks(tasks)
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)

        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
