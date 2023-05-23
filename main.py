import inventory
import setData
import give_blessing
import PySimpleGUI as sg

weapons = []
characters = []
traveler = {
    "name": "Traveler",
    "element": "your choice",
    "weapon": "sword"
}

artifacts = []

weapons_inv = []
characters_inv = [traveler]
artifacts_inv = []

setData.dataset(weapons, artifacts, characters)

layout = [[sg.Text('Current Floor:'), sg.Text(size=(15, 1), key='floor')],
          [sg.Button('Cleared Floor')],
          [sg.Button('Artifacts'), sg.Button('Weapons'), sg.Button('Characters')]]

window = sg.Window('Golden Slumber', layout, finalize=True)
current_floor = 1
window['floor'].update(current_floor)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cleared Floor':
        current_floor += 1
        give_blessing.artifact_blessing(artifacts, artifacts_inv, weapons_inv, characters_inv)
        give_blessing.character_blessing(characters, characters_inv, artifacts_inv, weapons_inv)
        give_blessing.weapon_blessing(weapons, weapons_inv)
        window['floor'].update(current_floor)
    if event == 'Characters':
        inventory.show_characters(characters_inv)
    if event == 'Artifacts':
        inventory.show_artifacts(artifacts_inv)
    if event == 'Weapons':
        inventory.show_weapons(weapons_inv)

window.close()
