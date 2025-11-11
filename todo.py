todo_list=[]

def add_task():
    task=input("Enter a task:")
    todo_list.append({"Task":task,"Status":"Pending"})
    print("new Task Added Succesfully")
    print("\n")


def view_task():
    print("Your To-do-list")
    if len(todo_list)==0:
        print("No pending Task ")
    else:
        for index,task in enumerate(todo_list,1):
            print(f"{index}:{task['Task']}-{task['Status']}")
    print("\n")


def remove_task():
    if len(todo_list)==0:
        print("List is Empty")
    else:
        try:
            search_index = int(input("Enter the task number:"))-1
            if 0<= search_index < len(todo_list):
                removed_task= todo_list.pop(search_index)
                print(f"Task is Remove:{removed_task}") 
            else:
                print("Invalid Task number")
        except ValueError:
            print("Please Enter a Valid task number ")
            print("\n")

def mark_done():
    if len(todo_list)==0:
        print("List is Empty")
    else:
        try:
            search_index = int(input("Enter the task number that you complete:"))-1
            if 0<= search_index < len(todo_list):
                todo_list[search_index]['Status'] ='done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as Done.")
            else:
                print("Invalid Task number")
        except ValueError:
            print("Please Enter a Valid task number ")
            print("\n")


def menu():
    while(True):
        print("This main menu")
        print("1.Add new tsak")
        print("2.Vie All Tasks")
        print("3.Remove aTask")
        print("4.Mark a Task as Completed")
        print("5.Exit")

        choice=input("Enter your choice :")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the app")
            exit()
        else:
            print("Invalid Input")  
            
menu()
