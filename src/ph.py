## Player Handler
## Deals with loading and saving player information

from save import Save
from mh import MapHandler
from player import Player


class PlayerHandler:
    def __init__(self, pl=Player(), mh=MapHandler()):
        self.pl = pl
        plinfo = self.pl.info
        self.mh = mh
        self.psave = {'player': plinfo, 'map': {"name": "", "location": ""}}
        if pl != None:
            self.ps = Save(pl.get("name")+".json")
        else:
            self.ps = Save()

    def __del__(self):
        self.mh = None
        self.pl = None
        self.psave = None
        self.ps = None

    def setMap(self, mname="", location=""):
        self.psave['map'] = {"name": mname, "location": location}

    def loadPl(self):
        loadDict = None
        if (self.pl != None and self.ps != None):
            loadDict = self.ps.loadFile()
            self.pl.info = loadDict["player"]
            self.mh.loadMap(loadDict["map"]["name"])
            self.mh.loadLocation(loadDict["map"]["location"])
            self.pl.toObject()
        loadDict = None

    def savePl(self):
        if (self.psave != None and self.ps != None):
            self.pl.info = self.pl.toJson()
            self.psave["player"] = self.pl.info
            self.ps.saveFile(self.psave)

    def isDead(self):
        return self.pl.info["hp"] <= 0

    def exists(self, array=[], item=None):
        res = False
        try:
            if len(array) > 0:
                for i in array:
                    if (item == i):
                        res = True
                        break
        finally:
            return res

    def addXp(self, amount=0):
        if (amount > 0):
            xp = self.pl.get("xp")
            self.pl.setV("xp", xp+amount)

    def upgradeHp(self, amount=0):
        mhp = self.pl.get("mhp")
        if amount > 0:
            self.pl.setV("mhp", mhp+amount)
        mhp = None

    def setHp(self, amount=None):
        hp = self.pl.get("hp")
        if amount != None:
            if ((hp + amount) > self.pl.info["mhp"]):
                self.pl.setV("hp", self.pl.info["mhp"])
            elif (hp + amount < 0):
                self.pl.setV("hp", 0)
            else:
                self.pl.setV("hp", hp+amount)
        hp = None

    def setMp(self, amount=0):
        mp = self.pl.get("mp")
        if amount >= 0:
            if (mp + amount > self.pl.info["mmp"]):
                self.pl.setV("mp", self.pl.info["mmp"])
            elif (mp + amount < 0):
                self.pl.setV("mp", 0)
            else:
                self.pl.setV("mp", mp+amount)
        mp = None

    def upgradeMp(self, amount=0):
        mmp = self.pl.get("mmp")
        if amount > 0:
            self.pl.setV("mmp", mmp+amount)
        mmp = None

    def equipWeapon(self, weapon=None):
        if self.exists(list(self.pl.get("weapons")), weapon):
            self.pl.info["equipped"][0] = weapon
        else:
            print("Does not exist.")

    def equipArmor(self, armor=None):
        if self.exists(list(self.pl.get("armors")), armor):
            self.pl.info["equipped"][1] = armor
        else:
            print("Does not exist.")

    def equipItem(self, item=None, place=""):
        if self.exists(list(self.pl.get("inventory")), item):
            if place in self.pl.get("equipped").keys():
                self.pl.info["equipped"][place] = item
            else:
                print("That is not a part of the equipped section")
        else:
            print("Does not exist.")

    def getMean(self):
        if (self.pl != None):
            return (self.pl.get("atk") + self.pl.get("def") + self.pl.get("spd") + self.pl.get("level"))/4
        else:
            return 0
