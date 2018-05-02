## Map Class
## Map structure and level structure

## Map Class
## Available player classes

from store import Store
from chest import Chest

class Map:
    def __init__(self, name="", msg="", enemies=[], chest=[], store=[], pclass=[], il=[], levels=[]):
        self.info = {
            "name": name,
            "msg": msg,
            "enemies": enemies,
            "chests": chest,
            "stores": store,
            "player classes": pclass,
            "item list": il,
            "levels": levels
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
    
    def levelExists(self, name=""):
        res = False
        if (len(self.get("levels")) > 0):
            lvls = self.get("levels")
            for i in lvls:
                if (i.get("name") == name):
                    res = True
                    break
        return res

    def levelIndex(self, name=""):
        res = -1
        if self.levelExists(name):
            lvls = self.get("levels")
            for i in range(0, len(lvls)):
                if lvls[i]["name"] == name:
                    res = i
                    break
        return res


    
    def getLevel(self, name=""):
        res = None
        if self.levelExists(name):
            res = self.levelIndex(name)
            if res != -1:
                return self.get("levels")[res]
        return res
            


## Level Class
## Level structure:
## name, msg, input directions, output locations, enemies enabled, enemy restrictions, chest enabled, chests restriction, store enabled, store restrictions, boss enabled, boss restrictions
class Level:
    def __init__(self, name="", msg="", commands={"inputs": [], "outputs": []}, typelist={"enemies": {"enabled": False, "restrictions": {"levels": 1, "creatures": []}}, "chest": {"enabled": False, "restrictions": {"rareities": [], "chests": []}}, "store": {"enabled": False, "store": Store()}, "boss": {"enabled": False, "restrictions": {"level": 1, "creature": {}}}}):
        self.info = {
            "name": name,
            "msg": msg,
            "commands": commands,
            "type enabled": typelist
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
