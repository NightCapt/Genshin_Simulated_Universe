import PySimpleGUI as sg
import shutil
import os


def data_window():
    layout = [[sg.T("")], [sg.Text("Choose the json file: "), sg.Input(), sg.FileBrowse(key="-IN-")], [sg.Button("Submit")]]

    window = sg.Window('My File Browser', layout, size=(600, 150))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Submit":
            location = values["-IN-"]
            original = r''+location
            target = r''

            shutil.copy(location, os.getcwd()+"/data.json")
            sg.popup("New Data loaded, Reset to floor one to start.")
            break

    window.close()
