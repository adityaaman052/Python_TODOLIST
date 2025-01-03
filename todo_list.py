# To-Do List Program

# List to store tasks
tasks = []

# Function to display tasks
def show_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter the task number to remove: "))
            removed_task = tasks.pop(task_no - 1)
            print(f"Task '{removed_task}' removed successfully!")
        except (ValueError, IndexError):
            print("Invalid task number!")

# Function to display menu
def menu():
    print("\nMenu:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main program loop
if __name__ == "__main__":
    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
