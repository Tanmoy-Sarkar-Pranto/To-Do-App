from modules import functions
import time
import PySimpleGUI as sg
import random
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

themes = ["Black","SandyBeach","Topanga","TealMono","TanBlue","Tan","DarkGreen6","DarkGrey5","BlueMono","DarkBlack","Dark","Dark2","DarkBrown6","SystemDefaultForReal","Reddit","NeutralBlue","Kayak","LightBrown10","Material1"]
theme_index = random.randint(0,len(themes)-1)

sg.theme(themes[theme_index])

label = sg.Text("To-Do App")
clock = sg.Text('', key="clock")
input_box = sg.InputText(tooltip="Enter ToDo",key="todo")
add_button = sg.Button(button_text="ADD")
exit_button = sg.Button(button_text="Exit",key="ex")

tasks = sg.Listbox(values=functions.load_tasks(),enable_events=True,size=(30,10),key="tasks")
edit_button = sg.Button("Edit",key="edit")
# print(type(label),type(input_box))
complete_button = sg.Button("Complete",key="cmplt")

window = sg.Window("To-Do App(New Theme Everytime)",
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [tasks,edit_button,complete_button],
                           [exit_button]], 
                   font=("Helvetica",15))


while True:
    event, value = window.read(timeout=100)
    window["clock"].update(time.strftime("%d %b, %Y %H:%M:%S"))
    # print(event,value["tasks"])
    if event=="ADD":
        if len(value["todo"])>1:
            todos = functions.load_tasks()
            todo = value["todo"] + '\n'
            todos.append(todo)
            functions.save_tasks(todos)
            window["tasks"].update(todos)
            window['todo'].update('')
        else:
            sg.popup("There is no task to add.\nPlease type any task",
                     background_color='Red',
                     keep_on_top=True)
    elif event == "edit":
        if len(value["todo"])>1 and len(value["tasks"])>=1:
            new_task = value["todo"] + '\n'
            todos = functions.load_tasks()
            index = todos.index(value["tasks"][0])
            todos[index] = new_task
            functions.save_tasks(todos)
            window["tasks"].update(todos)
            window['todo'].update('')
        else:
            sg.popup("Please select a task first and then write something in todo to edit",
                     background_color="Red")
    elif event=="cmplt":
        if len(value["tasks"])>=1:
            todos = functions.load_tasks()
            index = todos.index(value["tasks"][0])
            todos.pop(index)
            functions.save_tasks(todos)
            window["tasks"].update(todos)
        else:
            sg.popup("Please select a task first",
                     background_color="Red")
    elif event==sg.WIN_CLOSED or event=="ex":
        break

window.close()
