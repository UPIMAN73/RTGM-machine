## Player Creator Class
## Allows the player to creat a player object
## Your normal player setup

from random import randint
from player import Player
from jh import JsonHandler

class PlayerCreator:
    def __init__(self):
        self.pl = None
        # self.jh = JsonHandler("def_pcreator_settings.json")
        # self.jstruct = self.jh.read()
        # self.raceList = self.jstruct["race"]
        # self.defPlayerAd = self.jstruct["class"]

        self.raceList = ["human", "elf", "dwarf", "orc", "dark elf", "halfling"]
        self.defPlayerAd = {"barbarian": {"strength": 5, "dexterity": 5, "constitution": 5, "intelligence": 5, "wisdom": 5, "charisma": 5}, "bard":{"strength": 5, "dexterity": 5, "constitution": 5, "intelligence": 5, "wisdom": 5, "charisma": 5}, "druid": {"strength": 5, "dexterity": 5, "constitution": 5, "intelligence": 5, "wisdom": 5, "charisma": 5}}
        self.defPlayerClass = [] #["barbarian", "bard", "druid", "monk", "paladin", "ranger", "sorcerer", "warlock"]
        for i in self.defPlayerAd.keys():
            self.defPlayerClass.append(i)
    
    def printPersonality(self, p):
        for i in p.keys():
            print(i + "    " + str(p[i]))
        print("")

    def createLoop(self):
        quitCmds = ["quit", "done", "exit", "q"]
        genderList = ["male", "female"]
        pamt = 10
        name = ""
        race = ""
        gender = ""
        pclass = ""
        personality = {}
        # {"strength": 5, "dexterity": 5, "constitution": 5, "intelligence": 5, "wisdom": 5, "charisma": 5}
        
        # Name
        while len(name) <= 0:
            name = str(raw_input("Name?: "))
        print("")

        while (len(gender) <= 0) and (gender not in genderList):
            gender = str(raw_input("Gender (m/f)?: "))
            for i in genderList:
                if gender[0] == i[0]:
                    gender = i
                    break
                else:
                    continue
        print("")

        # Race
        while race not in self.raceList:
            print("The following races are: ")
            for i in range(0, len(self.raceList)):
                if i == int(i%4 == 0):
                    print("")
                print self.raceList[i],
            print("")
            race = str(raw_input("Race?: "))
        print("")

        # Player Class
        while pclass not in self.defPlayerClass:
            for i in self.defPlayerClass:
                print i,
            print("")
            pclass = raw_input("Player Class: ")
        personality = self.defPlayerAd[pclass]
        print("")

        # Personality makeup
        user_input = ""
        while user_input not in quitCmds:
            self.printPersonality(personality)
            print("Available points:    " + str(pamt))
            user_input = str(raw_input("> "))

            # Randomize the traits
            if user_input == "random" or user_input == "r":
                ipmt = pamt
                user_input = ["", ""]
                layers = personality.keys()
                rint = 0
                while ipmt > 0:
                    user_input[0] = layers[randint(0, len(layers)-1)]
                    rint = randint(0, ipmt)
                    user_input[1] = str(rint)
                    personality, ipmt = self.personalityEdit(user_input, personality, ipmt)
                pamt = ipmt
                ipmt = None
                user_input = None
                layers = None
                rint = None
                user_input = ""
            
            # If there is a space within the user input
            elif " " in user_input:
                user_input = user_input.split(" ")
                # Keyboard shortcut
                if len(user_input[0]) == 1:
                    lst = []
                    for i in personality.keys():
                        if user_input[0] == i[0]:
                            lst.append(i)
                        else:
                            continue
                    # only one
                    if len(lst) == 1:
                        user_input[0] = lst[0]
                    # many
                    elif len(lst) > 1:
                        item_input = ""
                        while item_input not in lst:
                            for i in range(0, len(lst)):
                                print(str(i+1) + "    " + lst[i])
                            print("")
                            item_input = str(raw_input("> "))
                            if item_input.isdigit():
                                item_input = int(item_input)
                                if item_input <= len(lst) and item_input > 0:
                                    item_input = lst[item_input-1]
                        user_input[0] = item_input
                        item_input = None
                    lst = None

                # values of the change
                personality, pamt = self.personalityEdit(user_input, personality, pamt)
            
            # If the trait does not exist
            else:
                print("That does not exist as a character traits.")
                print("The structure for the command is (trait value)")
                print("EX: strength 5\nEX: dexterity -5")
            
            # if the amount of traits is below 0
            if pamt < 0:
                pamt = 0
                print("Are you done with your trait handling?")
                print("If so, type quit or q to leave")
        print("")
        # Player setup is finished
        self.pl = Player(name=name, race=race, pclass=pclass, personality=personality)
        personality = None
    
    def personalityEdit(self, user_input, personality, pamt):
        # manage the value
        if user_input[0] in personality.keys():
            if int(user_input[1]) != 0 and abs(int(user_input[1])) <= pamt:
                personality[user_input[0]] += int(user_input[1])
                pamt -= int(user_input[1])
                if personality[user_input[0]] < 0:
                    correction = abs(personality[user_input[0]])
                    personality[user_input[0]] = personality[user_input[0]] + correction
                    pamt -= correction
        return personality, pamt
