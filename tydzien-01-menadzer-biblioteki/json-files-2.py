import json

def LoadChampions():
    try:
        with open("champions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No file found")
        return []

def SaveChampions(champions):
    with open("champions.json", "w") as file:
        json.dump(champions, file, indent=4)

def AddChampions():
    name = AskQuestion("Insert name of champion: ")
    damagetype = AskQuestion("Insert damage type of champion(AD/AP): ")
    lane = AskQuestion("Insert lane of champion: ")

    champions = LoadChampions()
    champions.append({"name": name, "damagetype": damagetype, "lane": lane})
    SaveChampions(champions)

def AskQuestion(question):
    return input(question)

for _ in range(4):
    AddChampions()