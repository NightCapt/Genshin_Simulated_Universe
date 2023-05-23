import sys

import inventory
import setData
import give_blessing
import PySimpleGUI as sg
import shop
import load_genshin_data

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
rerolls = 1

while True:
    try:
        setData.dataset(weapons, artifacts, characters)
        break
    except:
        sg.popup("Genshin data file is not compatible. Check README for importing Genshin data")
        load_genshin_data.data_window()

layout = [[sg.Button('Load Genshin Data'), sg.Button('Reset to floor 1')],
          [sg.Text('Current Floor:'), sg.Text(size=(15, 1), key='floor')],
          [sg.Text('Current Currency:'), sg.Text(size=(15, 1), key='money')],
          [sg.Button('Cleared Floor')],
          [sg.Button('Artifacts'), sg.Button('Weapons'), sg.Button('Characters')]]

window = sg.Window('Golden Slumber', layout, finalize=True)
money = [0]

current_floor = 1
window['floor'].update(current_floor)
window['money'].update(money[0])

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cleared Floor':
        current_floor += 1
        money[0] += 50
        window['money'].update(money[0])
        give_blessing.artifact_blessing(artifacts, artifacts_inv, weapons_inv, characters_inv, money, rerolls)
        give_blessing.character_blessing(characters, characters_inv, artifacts_inv, weapons_inv, money, rerolls)
        give_blessing.weapon_blessing(weapons, weapons_inv, characters_inv, artifacts_inv, money, rerolls)
        window['floor'].update(current_floor)
        window['money'].update(money[0])
        if current_floor == 5 or current_floor == 9 or current_floor == 12:
            shop.start_shop(artifacts, characters, weapons, artifacts_inv, characters_inv, weapons_inv, money, rerolls)
    if event == 'Characters':
        inventory.show_characters(characters_inv)
    if event == 'Artifacts':
        inventory.show_artifacts(artifacts_inv)
    if event == 'Weapons':
        inventory.show_weapons(weapons_inv)
    if event == 'Load Genshin Data':
        load_genshin_data.data_window()
    if event == 'Reset to floor 1':
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
        rerolls = 1

        while True:
            try:
                setData.dataset(weapons, artifacts, characters)
                break
            except:
                sg.popup("Genshin data file is not compatible. Check README for importing Genshin data")
                load_genshin_data.data_window()
        window['floor'].update(current_floor)
        window['money'].update(money[0])

window.close()
