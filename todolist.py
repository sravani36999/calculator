tasks = []

while True :
    print("---To-Do List---")
    print("Select Option")
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")

    choice = int(input("Choose your Option: "))

    if choice == 1:
        task = input("Enter Your Task: ")
        tasks.append(task)
        print("Task Added!")
    
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks to View!")
        else:
            print("\n Your Tasks Here!")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])
    
    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            num = int(input("Enter the task number to delete: "))
            if num > 0 and num <= len(tasks):
                tasks.pop(num-1)
            else:
                print("Invalid Number!")
    
    elif choice == 4:
        print("Bye!!!")
        break 
    
    else:
        print("Invalid Choice!!!")

'''I built a To-Do List application using Python.
 It allows users to add, view, and delete tasks 
 using lists, loops, and conditional statements.
 It runs in a loop until the user exits.'''