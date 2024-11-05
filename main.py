# source code : https://youtu.be/aEIHZDv_23U?si=_9aS1rbBVMLJMA-N

tasks = []

def addTask():
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"task {tasks} has been add to the list")

def listTask():
    if not tasks:
        print("There are no have task yet")
    else:
        print("Task List: ")
        for index, task in enumerate(tasks):
            print(f"Task {index+1}. {task}")

def delete():
    listTask()
    try:
        taskToDelete = int(input("Choose task that you want to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been deleted")
        else:
            print(f"Task {taskToDelete} was not found")  
    except:
        print("invalid input")


if __name__ == '__main__':
    # create a loop to run the app
    print('welcome to the do list app :')
    while True:
        print("\n")
        print("Please select one of the option")
        print("--------------------------------")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3.List task")
        print("4.Exit")

        choice = input("Select option: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTask()
        elif choice == "4":
            print("Thank youu for using")
            break
        else:
            print("Invalid Input, Please try again")

print("Adios")