"""
📝 Simple To-Do List Manager
-----------------------------
A beginner-friendly, console-based Python program to manage tasks.
Users can add, view, mark as done, and delete tasks.

Author: Abemelek Berhanu
"""

# Dictionary to store tasks
tasks = {}

def display_tasks():
    """Display all tasks with their status."""
    if not tasks:
        print("\n📭 Your to-do list is empty!\n")
        return
    print("\n📋 Your To-Do List:")
    for task_id, (task, done) in tasks.items():
        status = "✅ Done" if done else "❌ Pending"
        print(f"{task_id}. {task} [{status}]")
    print()


def add_task():
    """Add a new task to the to-do list."""
    task = input("Enter the task you want to add: ").strip()
    if task:
        task_id = len(tasks) + 1
        tasks[task_id] = (task, False)
        print(f"Task added: {task}\n")
    else:
        print("⚠️ Task cannot be empty!\n")


def mark_done():
    """Mark a task as completed."""
    display_tasks()
    try:
        task_id = int(input("Enter the task number to mark as done: "))
        if task_id in tasks:
            task, _ = tasks[task_id]
            tasks[task_id] = (task, True)
            print(f"Task '{task}' marked as done ✅\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def delete_task():
    """Delete a task from the list."""
    display_tasks()
    try:
        task_id = int(input("Enter the task number to delete: "))
        if task_id in tasks:
            task, _ = tasks.pop(task_id)
            print(f"Task '{task}' has been deleted 🗑️\n")
            # Reassign task IDs
            global tasks
            tasks = {i+1: v for i, v in enumerate(tasks.values())}
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def main():
    """Main program loop."""
    print("📝 Welcome to Your To-Do List Manager!")
    
    while True:
        print("Choose an option:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Exit\n")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye! Keep your tasks organized.")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()

