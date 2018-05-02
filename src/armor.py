## Armor Class
## Armor pieces that allows players and npcs to have defensive

class Armor:
    def __init__(self, name="", msg="", defs=0, abl={"fire": 0, "water": 0, "earth": 0, "lightning": 0, "darkness": 0, "death": 0, "critical": 0, "magic boost": 0}):
        self.info = {
            "name": name,
            "description": msg,
            "def": defs,
            "abilities":abl
        }
    
    def getInfo(self):
        return self.info

    def serialize(self, info):
        if info != self.info and type(info) == type(self.info):
            self.info = info

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