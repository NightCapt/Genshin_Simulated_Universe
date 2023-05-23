import json


def substat_return(key,value):
    if key == "atk":
        text = "Flat ATK " + str(value)
    elif key == "def":
        text = "Flat DEF " + str(value)
    elif key == "hp":
        text = "Flat HP " + str(value)
    elif key == "critRate_":
        text = "Crit Rate " + str(value)
    elif key == "eleMas":
        text = "EM " + str(value)
    elif key == "atk_":
        text = "ATK% " + str(value)
    elif key == "hp_":
        text = "HP% " + str(value)
    elif key == "def_":
        text = "DEF% " + str(value)
    elif key == "critDMG_":
        text = "Crit DMG " + str(value)
    elif key == "enerRech_":
        text = "Energy Recharge " + str(value)
    else:
        text = key + " " + str(value)
    return text


def dataset(weapons, artifacts, characters):
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    for i in data['weapons']:
        if i["level"] > 59:
            newWeapon = {
                "name": i["key"],
                "type": "sword"
            }
            weapons.append(newWeapon)

    for i in data["artifacts"]:
        if i["level"] > 15:
            newArtifact = {
                "level": i["level"],
                "Set": i["setKey"],
                "slot": i["slotKey"],
                "main stat": i["mainStatKey"],
                "substat1": substat_return(i["substats"][0]["key"], i["substats"][0]["value"]),
                "substat2": substat_return(i["substats"][1]["key"], i["substats"][1]["value"]),
                "substat3": substat_return(i["substats"][2]["key"], i["substats"][2]["value"]),
                "substat4": substat_return(i["substats"][3]["key"], i["substats"][3]["value"]),
                "blessing": "wisdom"
            }

            artifacts.append(newArtifact)

    for i in data['characters']:

        if i["level"] > 59 and not i["key"] == "TravelerDendro" and not i["key"] == "TravelerElectro" and not i["key"] == "TravelerAnemo" and not i["key"] == "TravelerGeo":
            newCharacter = {
                "name": i["key"],
                "element": "hydro",
                "weapon":"sword"
            }
            characters.append(newCharacter)

    f.close()
