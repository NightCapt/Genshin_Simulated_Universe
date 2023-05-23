import random
import PySimpleGUI as sg
import inventory


def blessing_window(new_artifacts):
    artifact_text = ""
    for x in new_artifacts:
        artifact_text = artifact_text + "Level" + str(x["level"]) + " " + x["Set"] +" "+ x["slot"] +"\n"
        artifact_text = artifact_text + x["main stat"] + " main stat \n"
        artifact_text = artifact_text + x["substat1"] + "\n" + x["substat2"] + "\n" + x["substat3"] + "\n" + x["substat1"] + "\n "
        artifact_text = artifact_text + "\n"
    sg.popup_scrolled(artifact_text)


def artifact_blessing(artifacts, artifact_inv, weapons_inv, characters_inv):
    sets = []
    for i in artifacts:
        if not i["Set"] in sets:
            sets.append(i["Set"])

    for art_set in sets:
        check_set = []
        for i in artifacts:
            if i["Set"] == art_set:
                check_set.append(i)

        if len(check_set) < 3:
            sets.pop(sets.index(art_set))

    blessing_list = random.sample(sets, k=3)

    layout = [[sg.Text("Choose an Artifact", key="new")],
              [sg.Button(blessing_list[0]), sg.Button(blessing_list[1]), sg.Button(blessing_list[2])],
              [sg.Button('Artifacts'), sg.Button('Weapons'), sg.Button('Characters')]]
    window = sg.Window("Artifact Blessing", layout, modal= True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == blessing_list[0]:
            this_set = []
            for i in artifacts:
                if i["Set"] == blessing_list[0]:
                    this_set.append(i)

            new_artifacts = random.sample(this_set, k=3)
            blessing_window(new_artifacts)

            artifact_inv.append(new_artifacts[0])
            artifact_inv.append(new_artifacts[1])
            artifact_inv.append(new_artifacts[2])

            artifacts.pop(artifacts.index(new_artifacts[0]))
            artifacts.pop(artifacts.index(new_artifacts[1]))
            artifacts.pop(artifacts.index(new_artifacts[2]))
            break

        if event == blessing_list[1]:
            this_set = []
            for i in artifacts:
                if i["Set"] == blessing_list[1]:
                    this_set.append(i)

            new_artifacts = random.sample(this_set, k=3)
            blessing_window(new_artifacts)

            artifact_inv.append(new_artifacts[0])
            artifact_inv.append(new_artifacts[1])
            artifact_inv.append(new_artifacts[2])

            artifacts.pop(artifacts.index(new_artifacts[0]))
            artifacts.pop(artifacts.index(new_artifacts[1]))
            artifacts.pop(artifacts.index(new_artifacts[2]))
            break

        if event == blessing_list[2]:
            this_set = []
            for i in artifacts:
                if i["Set"] == blessing_list[2]:
                    this_set.append(i)

            new_artifacts = random.sample(this_set, k=3)
            blessing_window(new_artifacts)

            artifact_inv.append(new_artifacts[0])
            artifact_inv.append(new_artifacts[1])
            artifact_inv.append(new_artifacts[2])

            artifacts.pop(artifacts.index(new_artifacts[0]))
            artifacts.pop(artifacts.index(new_artifacts[1]))
            artifacts.pop(artifacts.index(new_artifacts[2]))
            break
        if event == 'Characters':
            inventory.show_characters(characters_inv)
        if event == 'Artifacts':
            inventory.show_artifacts(artifact_inv)
        if event == 'Weapons':
            inventory.show_weapons(weapons_inv)
    window.close()


def character_blessing(characters, characters_inv,artifact_inv,weapons_inv):
    blessing_list = random.sample(characters, k=3)

    layout = [[sg.Text("Choose a Character", key="new")],
              [sg.Button(blessing_list[0]["name"]), sg.Button(blessing_list[1]["name"]), sg.Button(blessing_list[2]["name"])],
              [sg.Button('Artifacts'), sg.Button('Weapons'), sg.Button('Characters')]
              ]
    window = sg.Window("Character Blessing", layout, modal=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == blessing_list[0]["name"]:
            characters_inv.append(blessing_list[0])
            characters.pop(characters.index(blessing_list[0]))
            break
        if event == blessing_list[1]["name"]:
            characters_inv.append(blessing_list[1])
            characters.pop(characters.index(blessing_list[1]))
            break
        if event == blessing_list[2]["name"]:
            characters_inv.append(blessing_list[2])
            characters.pop(characters.index(blessing_list[2]))
            break
        if event == 'Characters':
            inventory.show_characters(characters_inv)
        if event == 'Artifacts':
            inventory.show_artifacts(artifact_inv)
        if event == 'Weapons':
            inventory.show_weapons(weapons_inv)
    window.close()


def weapon_blessing(weapons, weapons_inv):
    blessing_list = random.sample(weapons, k=3)

    layout = [[sg.Text("Choose a weapon", key="new")],
              [sg.Button(blessing_list[0]["name"]), sg.Button(blessing_list[1]["name"]), sg.Button(blessing_list[2]["name"])]]
    window = sg.Window("Weapon Blessing", layout, modal=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == blessing_list[0]["name"]:
            weapons_inv.append(blessing_list[0])
            weapons.pop(weapons.index(blessing_list[0]))
            break
        if event == blessing_list[1]["name"]:
            weapons_inv.append(blessing_list[1])
            weapons.pop(weapons.index(blessing_list[1]))
            break
        if event == blessing_list[2]["name"]:
            weapons_inv.append(blessing_list[2])
            weapons.pop(weapons.index(blessing_list[2]))
            break

    window.close()

