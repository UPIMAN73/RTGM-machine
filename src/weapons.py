# Available Weapons within the game itself
# All of the Weapons specs are setup here


## Weapon Abilities:
## poison, fire, water, wind, earth, lightning, darkness, death, critical, magic boost
class Weapons:
    def __init__(self, name="", msg="", atk=0, abl={"fire": 0, "water": 0, "earth": 0, "lightning": 0, "darkness": 0, "death": 0, "critical": 0, "magic boost": 0}):
        self.info = {
            "name": name,
            "description": msg,
            "atk": atk,
            "abilities": abl
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

    def listAbilities(self):
        res = []
        for i in self.info["abilities"].keys():
            if self.info["abilities"][i] > 0:
                res.append(i)
        return res


class WeaponsList:
    def __init__(self, wlist=[], rare=[]):
        self.info = {
            "weapons list": wlist,
            "rare range": rare
        }

    def __del__(self):
        self.wlist = None
        self.rare = None

    def get(self, arg):
        return self.info.get(arg, "INVALID")

    def setV(self, key, value):
        for i in self.info.keys():
            if (key == i):
                self.info[key] = value
                break
            else:
                continue

    def wexists(self, obj):
        res = False
        for i in self.info["weapons list"]:
            if i == obj:
                res = True
        return res
