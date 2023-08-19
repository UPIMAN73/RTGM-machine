## Enemy Class
## All enemies are structured as so (even bosses)

from weapons import Weapons
from item import Item, Potions
from armor import Armor

## Structure:
## Name, description, level, max hp, max mp, attack, defense, speed, equipped items, drop items (range)
class Enemy:
    def __init__(self, name="", des="", lvl=1, mhp=0, mmp=0, atk=0, pdef=0, spd=0, crit=0, equipped={"weapon": Weapons(), "talisman": Item(), "bracelet": Item(), "ring": Item()}, eqarmors={"left": Armor(), "right": Armor(), "head": Armor(), "body": Armor()}, drop={"items":[], "xp":0}):
        self.info = {
            "name": name,
            "description": des,
            "level": lvl,
            "mhp": mhp,
            "mmp": mmp,
            "hp": mhp,
            "mp": mmp,
            "atk": atk,
            "def": pdef,
            "spd": spd,
            "crit": crit,
            "equipped": equipped,
            "equipped armors": eqarmors,
            "drop": drop
        }

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


