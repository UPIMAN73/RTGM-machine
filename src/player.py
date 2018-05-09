## Player Class Object
## Personality section are strength, wisdom, stamina, and speed.

## Equipped structure:
## Weapons, talisman, bracelet, ring
from weapons import Weapons
from item import Item, Potions
from armor import Armor


class Player:
    def __init__(self, name="", race="", gender="", pclass="", personality={"strength": 5, "dexterity": 5, "constitution": 5, "intelligence": 5, "wisdom": 5, "charisma": 5}):
        self.info = {
            "name": name,
            "race": race,
            "gender": gender,
            "class": pclass,
            "personality": personality,
            "level": 1,
            "mhp": 100,
            "mmp": 100,
            "hp": 100,
            "mp": 100,
            "xp": 0,
            "def": 3 * int(personality["strength"]),
            "atk": 5 * int(personality["strength"]),
            "spd": 5 * int(personality["dexterity"]),
            "crit": 2 * int(personality["dexterity"]),
            "money": 0,
            "invlimit": 3 * int((personality["strength"]+personality["dexterity"])/2),
            "wplimit": 2 * int((personality["strength"]+personality["dexterity"])/2),
            "arlimit": int((personality["strength"]+personality["dexterity"])/2),
            "inventory": {"weapons": [], "armors": [], "items": [], "potions": []},
            "equipped armors": {"left": Armor(), "right": Armor(), "head": Armor(), "body": Armor()},
            "equipped": {"weapon": Weapons(), "talisman": Item(), "bracelet": Item(), "ring": Item()}
        }

    def toObject(self):
        output = self.info
        for i in self.get("equipped armors").keys():
            print(type(output["equipped armors"][i]))
            if (type(output["equipped armors"][i]).__name__ == "instance"):
                continue
            arminfo = output["equipped armors"][i]
            output["equipped armors"][i] = Armor()
            output["equipped armors"][i].serialize(arminfo)

        for i in self.get("equipped").keys():
            print(type(output["equipped"][i]))
            if (type(output["equipped"][i]).__name__ == "instance"):
                continue
            arminfo = output["equipped"][i]
            output["equipped"][i] = Armor()
            output["equipped"][i].serialize(arminfo)

    def toJson(self):
        output = self.info
        for i in self.get("equipped armors").keys():
            print(type(output["equipped armors"][i]))
            if (type(output["equipped armors"][i]).__name__ == "dict"):
                continue
            output["equipped armors"][i] = output["equipped armors"][i].getInfo()

        for x in self.get("equipped").keys():
            print(type(output["equipped"][x]))
            if (type(output["equipped"][x]).__name__ == "dict"):
                continue
            output["equipped"][x] = output["equipped"][x].info
        return output

    def serialize(self, info):
        if info != self.info and type(info) == type(self.info):
            self.info = info

    def __del__(self):
        self.info = None

    def get(self, arg):
        return self.info.get(arg, "INVALID")

    def setV(self, key, value):
        for i in self.info.keys():
            if (key == i):
                self.info[key] = value
                break
            else:
                continue
