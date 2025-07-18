# todo.py

def load_tasks(filename="tasks.txt"):
    """Load tasks from a file into a list."""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    """Save the list of tasks to a file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
