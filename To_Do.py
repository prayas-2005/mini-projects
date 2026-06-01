tasks = []

while True:
    # select the number
    choice = (int)(input("Enter the choice : "))
    
    # Add Task
    if choice == 1:
        task_name = input("Enter task name : ")
        tasks.append(task_name)
        print(f"{task_name}, added successfully")
    elif choice == 2:
        if not tasks:
            print("Task list is empty")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == 3:
        print("Goodbye")
        break
    else:
        print("Invalid Choice")