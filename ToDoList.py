# Mini Project: To-Do List Application

# To-Do list container
todo_list = []

def display_menu():
    """Display menu options to the user."""
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_todo_list():
    """Display the current to-do list."""
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{index}. {task['task']} [{status}]")

def add_task():
    """Add a new task to the to-do list."""
    task = input("\nEnter the task you want to add: ")
    todo_list.append({"task": task, "done": False})
    print(f"Task '{task}' added to your to-do list.")

def remove_task():
    """Remove a task from the to-do list."""
    view_todo_list()
    try:
        task_number = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_as_done():
    """Mark a task as done."""
    view_todo_list()
    try:
        task_number = int(input("\nEnter the number of the task to mark as done: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]['done'] = True
            print(f"Task '{todo_list[task_number - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list application."""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_as_done()
        elif choice == '5':
            print("\nGoodbye! Have a productive day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
