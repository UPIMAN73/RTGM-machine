## Items Class
## Creates a structure for the items being made within the game
## Structure:
## Name, Description, abilities, level required

## Abilities:
## atk, def, spd, crit, mhp, mmp, stamina
class Item:
    def __init__(self, name="", des="", lvl=1, abl={"atk": 0, "def": 0, "spd": 0, "hp": 0, "mp": 0, "crit": 0, "stm": 0}, price={"buy":0, "sell":0}):
        self.info = {
            "name": name,
            "description": des,
            "level": lvl,
            "abilities": abl,
            "price": price
        }

    def get(self, arg):
        return self.info.get(arg, "INVALID")

    def setV(self, key, value):
        for i in self.info.keys():
            if (key == i):
                self.info[key] = value
                break
            else:
                continue


## Potions Class
## Ability Structure:
## HP and MP
class Potions:
    def __init__(self, name="", des="", lvl=1, abl={"hp": 0, "mp": 0}, price={"buy":0, "sell":0}):
        self.info = {
            "name": name,
            "description": des,
            "level": lvl,
            "abilities": abl,
            "price": price
        }

    def get(self, arg):
        return self.info.get(arg, "INVALID")

    def setV(self, key, value):
        for i in self.info.keys():
            if (key == i):
                self.info[key] = value
                break
            else:
                continue
