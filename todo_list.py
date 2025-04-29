tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

while True:

    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")
    elif choice == '2':
        print("\n--- Current Tasks ---")
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i+1}. [{status}] {task['task']}")
    elif choice == '3':
        num = int(input("Enter task number to mark as done: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")
