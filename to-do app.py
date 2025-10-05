def tasks():
    tasks = []
    print("---WELCOME TO THE TASK MANAGEMENT APP---")

    #the user will be asked to add number of tasks they want to add to list
    total_tasks = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task{i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        operation = int(input("\nEnter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nYour choice: "))
        #user will be given a choice to select what task thwy want to perform by entering that number
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task name = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task '{updated_val}' to '{up}'.")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Saving tasks and closing the program...")

            # ✅ Save tasks to file before exiting
            with open("tasks.txt", "w") as f:
                for t in tasks:
                    f.write(t + "\n")

            print("All tasks saved successfully in 'tasks.txt'.")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 5.")


tasks()












