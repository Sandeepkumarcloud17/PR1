# todo.py

tasks = []

def show_tasks():
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks in your to-do list!")

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    show_tasks()
    if tasks:
        task_number = int(input("Enter the task number to remove: "))
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to remove.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
sss