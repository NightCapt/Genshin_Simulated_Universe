import json


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
                "substat1": i["substats"][0]["key"]+str(i["substats"][0]["value"]),
                "substat2": i["substats"][1]["key"] + str(i["substats"][1]["value"]),
                "substat3": i["substats"][2]["key"] + str(i["substats"][2]["value"]),
                "substat4": i["substats"][3]["key"] + str(i["substats"][3]["value"]),
                "blessing": "wisdom"
            }
            if i["substats"][0]["key"] == "atk":
                newArtifact["substat1"] = "flat atk"+str(i["substats"][0]["value"])
            elif i["substats"][0]["key"] == "def":
                newArtifact["substat1"] = "flat def" + str(i["substats"][0]["value"])
            elif i["substats"][0]["key"] == "hp":
                newArtifact["substat1"] = "flat hp" + str(i["substats"][0]["value"])

            if i["substats"][1]["key"] == "atk":
                newArtifact["substat2"] = "flat atk"+str(i["substats"][1]["value"])
            elif i["substats"][1]["key"] == "def":
                newArtifact["substat2"] = "flat def" + str(i["substats"][1]["value"])
            elif i["substats"][1]["key"] == "hp":
                newArtifact["substat2"] = "flat hp" + str(i["substats"][1]["value"])

            if i["substats"][2]["key"] == "atk":
                newArtifact["substat3"] = "flat atk"+str(i["substats"][2]["value"])
            elif i["substats"][2]["key"] == "def":
                newArtifact["substat3"] = "flat def" + str(i["substats"][2]["value"])
            elif i["substats"][2]["key"] == "hp":
                newArtifact["substat3"] = "flat hp" + str(i["substats"][2]["value"])

            if i["substats"][3]["key"] == "atk":
                newArtifact["substat4"] = "flat atk"+str(i["substats"][3]["value"])
            elif i["substats"][3]["key"] == "def":
                newArtifact["substat4"] = "flat def" + str(i["substats"][3]["value"])
            elif i["substats"][3]["key"] == "hp":
                newArtifact["substat4"] = "flat hp" + str(i["substats"][3]["value"])



            artifacts.append(newArtifact)

    for i in data['characters']:

        if i["level"] > 59:
            newCharacter = {
                "name": i["key"],
                "element": "hydro",
                "weapon":"sword"
            }
            characters.append(newCharacter)

    f.close()
