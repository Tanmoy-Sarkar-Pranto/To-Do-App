import PySimpleGUI as sg

label1 = sg.Text("Select files to compress")
label2 = sg.Text("Select destination folder")

input1 = sg.Input()
input2 = sg.Input()

sg.theme("black")
choose_box1 = sg.FilesBrowse("Choose")
choose_box2 = sg.FolderBrowse("Choose")
button = sg.Button(button_text="Compress")

window = sg.Window("File Zipper",layout=[[label1,input1,choose_box1],[label2,input2,choose_box2],[button]])


while True:
    event, values = window.read()
    if event == 'Compress': # if user closes window or clicks cancel
        print("Compressed")


window.read()
window.close()

