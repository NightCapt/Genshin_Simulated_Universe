import PySimpleGUI as sg


def show_characters(characters_inv):

    my_text = ""

    for x in characters_inv:
        my_text += x["name"] + "\n"
    sg.popup_scrolled(my_text, size=(80, 10))


def show_weapons(weapons_inv):

    my_text = ""

    for x in weapons_inv:
        my_text += x["name"] + "\n"
    sg.popup_scrolled(my_text, size=(80, 10))


def show_artifacts(artifacts_inv):
    artifact_text = ""
    for x in artifacts_inv:
        artifact_text = artifact_text + "Level" + str(x["level"]) + " " + x["Set"] +" "+ x["slot"] +"\n"
        artifact_text = artifact_text + x["main stat"] + " main stat \n"
        artifact_text = artifact_text + x["substat1"] + "\n" + x["substat2"] + "\n" + x["substat3"] + "\n" + x["substat1"] + "\n "
        artifact_text = artifact_text + "\n"
    sg.popup_scrolled(artifact_text, size=(80, 25))