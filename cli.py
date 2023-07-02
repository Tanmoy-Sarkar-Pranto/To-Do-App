from modules import functions
import time
import tkinter

print("It's "+time.strftime("%b %d, %Y %H:%M"))

while True:
    a = input("Type add,show,edit,complete or exit: ").strip()
    if a.startswith("add"):  
        to_dos = functions.load_tasks()
        todo = a[4:]
        to_dos.append(todo)
        
        functions.save_tasks(to_dos)
    elif a.startswith("show"):
        to_dos = functions.load_tasks()
        for i,task in enumerate(to_dos):
            task = task.strip("\n")
            print(f"{i+1}: {task}")       
    
    elif a.startswith("edit"):
        if a[5:].isdigit() is True:
            index = int(a[5:])
        else:
            print("Not a digit Input")
            continue
        # for i,task in enumerate(to_dos):
        #     if index-1 == i:
        #         print(f"Editing {task}")
        #         to_dos.remove(task)
        #         n_task = input("Enter the new task: ")
        #         to_dos.insert(i, n_task)
        to_dos = functions.load_tasks()
        if index <= len(to_dos) and index > 0:
            old_task = to_dos[index-1]
            print(f"Editing {old_task}")
            to_dos.remove(old_task)
            new_task = input("Enter the new task: ")+"\n"
            to_dos.insert(index-1, new_task)
            functions.save_tasks(to_dos)
        else:
            print("Index is not correct")
    elif a.startswith("complete"):
        try:
            to_dos = functions.load_tasks()
            com_index = int(a[8:])
            print(f"{to_dos[com_index-1]} completed\n")
            to_dos.pop(com_index-1)
            functions.save_tasks(to_dos)
        except IndexError:
            print("The number you entered is not in the list")
            continue

    elif a.startswith("exit"):
        break 
    else :
        print("Invalid Input")

print("Bye!")