from modules import functions

import PySimpleGUI as sg

label = sg.Text("To-Do App")
input_box = sg.InputText(tooltip="Enter ToDo",key="todo",do_not_clear=False)
add_button = sg.Button(button_text="ADD")
exit_button = sg.Button(button_text="Exit",key="ex")

tasks = sg.Listbox(values=functions.load_tasks(),enable_events=True,size=(30,10),key="tasks")
edit_button = sg.Button("Edit",key="edit")
# print(type(label),type(input_box))
complete_button = sg.Button("Complete",key="cmplt")

window = sg.Window("To-Do App Title",
                   layout=[[label],[input_box,add_button],[tasks,edit_button],[complete_button],[exit_button]], 
                   font=("Helvetica",15))


while True:
    event, value = window.read()
    print(event,value)
    if event=="ADD":
        if len(value["todo"])>1:
            todos = functions.load_tasks()
            todo = value["todo"] + '\n'
            todos.append(todo)
            functions.save_tasks(todos)
            window["tasks"].update(todos)
    elif event == "edit":
        if len(value["todo"])>1:
            new_task = value["todo"] + '\n'
            todos = functions.load_tasks()
            index = todos.index(value["tasks"][0])
            todos[index] = new_task
            functions.save_tasks(todos)
            window["tasks"].update(todos)
            
    elif event=="cmplt":
        todos = functions.load_tasks()
        index = todos.index(value["tasks"][0])
        todos.pop(index)
        functions.save_tasks(todos)
        window["tasks"].update(todos)
    elif event==sg.WIN_CLOSED or event=="ex":
        break

window.close()
