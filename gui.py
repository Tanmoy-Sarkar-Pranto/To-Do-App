from modules import functions

import PySimpleGUI as sg

label = sg.Text("To-Do App")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button(button_text="ADD")

# print(type(label),type(input_box))
window = sg.Window("To-Do App Title",layout=[[label],[input_box,add_button]])

window.read()
window.close()
