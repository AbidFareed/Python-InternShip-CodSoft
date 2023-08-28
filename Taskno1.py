tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def list_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

def main():
    while True:
        print("Options")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
