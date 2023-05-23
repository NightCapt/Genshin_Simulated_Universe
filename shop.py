import random

import inventory
import give_blessing
import PySimpleGUI as sg


def start_shop(artifacts, characters, weapons, artifacts_inv, characters_inv, weapons_inv, money, rerolls):
    cost = 20
    cost_blessing = 30
    layout = [[sg.Text("Welcome to the shop", key="new")],
              [sg.Text('Current Currency:'), sg.Text(size=(15, 1), key='money')],
              [sg.Text('Cost per artifact:'), sg.Text(size=(15, 1), key='cost')],
              [sg.Button("ER Timepiece"), sg.Button("Crit Rate Hat"), sg.Button("Crit Damage Hat")],
              [sg.Button("Hydro Goblet"), sg.Button("Electro Goblet"), sg.Button("Anemo Goblet")],
              [sg.Button("Pyro Goblet"), sg.Button("Cryo Goblet"), sg.Button("Dendro Goblet")],
              [sg.Button("Geo Goblet"), sg.Button("EM Goblet"), sg.Button("EM Hat")],
              [sg.Text('Cost of Blessings:'), sg.Text(size=(15, 1), key='cost_blessing')],
              [sg.Button("Character Blessing"), sg.Button("Weapon Blessing")],
              [sg.Button("Leave Shop")],
              [sg.Button('Artifacts'), sg.Button('Weapons'), sg.Button('Characters')]]
    window = sg.Window("Artifact Blessing", layout, modal=True, finalize=True)
    window['money'].update(money[0])
    window['cost'].update(cost)
    window['cost_blessing'].update(cost_blessing)
    while True:
        event, values = window.read()
        if money[0] < cost:
            window['ER Timepiece'].update(disabled=True)
            window['Crit Rate Hat'].update(disabled=True)
            window['Crit Damage Hat'].update(disabled=True)
            window['Hydro Goblet'].update(disabled=True)
            window['Anemo Goblet'].update(disabled=True)
            window['Electro Goblet'].update(disabled=True)
            window['Cryo Goblet'].update(disabled=True)
            window['Dendro Goblet'].update(disabled=True)
            window['Geo Goblet'].update(disabled=True)
            window['Pyro Goblet'].update(disabled=True)
            window['Hydro Goblet'].update(disabled=True)
            window['EM Goblet'].update(disabled=True)
            window['EM Hat'].update(disabled=True)
        if money[0] < cost_blessing:
            window['Character Blessing'].update(disabled=True)
            window['Weapon Blessing'].update(disabled=True)

        if event == sg.WIN_CLOSED or event == "Leave Shop":
            break

        if event == 'ER Timepiece':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "enerRech_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['ER Timepiece'].update(disabled=True)

        if event == 'Crit Rate Hat':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "critRate_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Crit Rate Hat'].update(disabled=True)

        if event == 'Crit Damage Hat':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "critDMG_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Crit Damage Hat'].update(disabled=True)

        if event == 'Hydro Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "hydro_dmg_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Hydro Goblet'].update(disabled=True)

        if event == 'Anemo Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "anemo_dmg_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Anemo Goblet'].update(disabled=True)

        if event == 'Electro Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "electro_dmg_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Electro Goblet'].update(disabled=True)

        if event == 'Cryo Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "cryo_dmg_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Cryo Goblet'].update(disabled=True)

        if event == 'Dendro Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "dendro_dmg_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Dendro Goblet'].update(disabled=True)

        if event == 'Geo Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "geo_dmg_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Geo Goblet'].update(disabled=True)

        if event == 'Pyro Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "pyro_dmg_":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['Pyro Goblet'].update(disabled=True)

        if event == 'EM Goblet':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "eleMas" and x["slot"] == "goblet":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['EM Goblet'].update(disabled=True)

        if event == 'EM Hat':
            legal_artifacts = []
            for x in artifacts:
                if x["main stat"] == "eleMas" and x["slot"] == "circlet":
                    legal_artifacts.append(x)
            new_artifact = []
            new_artifact.append(random.choice(legal_artifacts))
            give_blessing.blessing_window(new_artifact)
            artifacts_inv.append(new_artifact[0])
            artifacts.pop(artifacts.index(new_artifact[0]))
            money[0] = money[0] - cost
            window['money'].update(money[0])
            window['EM Hat'].update(disabled=True)

        if event == "Character Blessing":
            give_blessing.character_blessing(characters, characters_inv, artifacts_inv, weapons_inv, money, rerolls)
            money[0] = money[0] - 30
            window['Character Blessing'].update(disabled=True)
            window['money'].update(money[0])

        if event == "Weapon Blessing":
            give_blessing.weapon_blessing(weapons, weapons_inv, characters_inv, artifacts_inv, money, rerolls)
            money[0] = money[0] - 30
            window['Weapon Blessing'].update(disabled=True)
            window['money'].update(money[0])
        if event == 'Characters':
            inventory.show_characters(characters_inv)
        if event == 'Artifacts':
            inventory.show_artifacts(artifacts_inv)
        if event == 'Weapons':
            inventory.show_weapons(weapons_inv)
        if money[0] < cost:
            window['ER Timepiece'].update(disabled=True)
            window['Crit Rate Hat'].update(disabled=True)
            window['Crit Damage Hat'].update(disabled=True)
            window['Hydro Goblet'].update(disabled=True)
            window['Anemo Goblet'].update(disabled=True)
            window['Electro Goblet'].update(disabled=True)
            window['Cryo Goblet'].update(disabled=True)
            window['Dendro Goblet'].update(disabled=True)
            window['Geo Goblet'].update(disabled=True)
            window['Pyro Goblet'].update(disabled=True)
            window['Hydro Goblet'].update(disabled=True)
            window['EM Goblet'].update(disabled=True)
            window['EM Hat'].update(disabled=True)

    window.close()
