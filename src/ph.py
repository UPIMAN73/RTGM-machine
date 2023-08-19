## Player Handler
## Deals with loading and saving player information

from player import Player
from save import Save
from mh import MapHandler



class PlayerHandler:
    def __init__(self, pl=Player(), mh=MapHandler()):
        self.pl = pl
        plinfo = self.pl.info
        self.mh = mh
        self.psave = {'player': plinfo, 'map': {"name": "", "location": ""}, 'xp': []}
        if pl != None:
            fname = pl.get("name").lower()
            if " " in fname:
                fname = fname.split(" ")
                res = ""
                for i in range(0, len(fname)-1):
                    res += fname[i] + "_"
                res += fname[len(fname)-1]
                fname = res
                res = None
                print(res)
                print(fname)
            self.ps = Save(str(fname)+".json")
            fname = None
        else:
            self.ps = Save()

    def __del__(self):
        self.mh = None
        self.pl = None
        self.psave = None
        self.ps = None
    
    # set the map json setup to the save location
    def setMap(self, mname="", location=""):
        self.psave['map'] = {"name": mname, "location": location}
    
    # Load Player object
    def loadPl(self):
        loadDict = None
        if (self.pl != None and self.ps != None):
            loadDict = self.ps.loadFile()
            self.pl.info = loadDict["player"]
            self.mh.loadMap(loadDict["map"]["name"])
            self.mh.loadLocation(loadDict["map"]["location"])
            self.pl.toObject()
        loadDict = None
    
    # Save the player info
    def savePl(self):
        if (self.psave != None and self.ps != None):
            self.pl.info = self.pl.toJson()
            self.psave["player"] = self.pl.info
            self.ps.saveFile(self.psave)
    
    # If the player ris dead
    def isDead(self):
        return self.pl.info["hp"] <= 0
    
    # If an item exists.
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
    
    # Add xp to the player
    def addXp(self, amount=0):
        if (amount > 0):
            xp = self.pl.get("xp")
            self.pl.setV("xp", xp+amount)
    
    # add an amount to the max hp
    def upgradeHp(self, amount=0):
        mhp = self.pl.get("mhp")
        if amount > 0:
            self.pl.setV("mhp", mhp+amount)
        mhp = None
    
    # add or subtract the hp amount
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
    
    # add or subtract the mp amount
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
    
    # add more mp to the max mp
    def upgradeMp(self, amount=0):
        mmp = self.pl.get("mmp")
        if amount > 0:
            self.pl.setV("mmp", mmp+amount)
        mmp = None
    
    # equip a weapon
    def equipWeapon(self, weapon):
        if self.exists(list(self.pl.get("inventory")["weapons"]), weapon):
            self.pl.info["equipped"][0] = weapon
        else:
            print("Does not exist.")
    
    # equip armor
    def equipArmor(self, armor):
        if armor == None:
            print("Your item does note exist because you did not ask for an item.")
        elif self.exists(list(self.pl.get("inventory")["armors"]), armor):
            self.pl.info["equipped"][1] = armor
        else:
            print("Does not exist.")
    
    # equip an item
    def equipItem(self, item, place=""):
        if item == None:
            print("Your item does note exist because you did not ask for an item.")
        elif self.exists(list(self.pl.get("inventory")["items"]), item):
            if place in self.pl.get("equipped").keys():
                self.pl.info["equipped"][place] = item
            else:
                print("That is not a part of the equipped section")
        else:
            print("Does not exist.")
    
    # ONLY Used for battle
    def getMean(self):
        if (self.pl != None):
            return (self.pl.get("atk") + self.pl.get("def") + self.pl.get("spd") + self.pl.get("level"))/4
        else:
            return 0
    
    # checks to see if an item is in your inventory by name
    def inInventory(self, name=""):
        res = False
        for x in self.pl.get("inventory").keys():
            for i in self.pl.get("inventory")[x]:
                if i.get("name") == name:
                    res = True
                    break
        return res
    
    # get an item based on the name and place
    def getItem(self, name="", place=""):
        if self.inInventory(name):
            for x in self.pl.get("inventory").keys():
                for i in self.pl.get("inventory")[x]:
                    if i.get("name") == name:
                        return i
        else:
            print("Does not exist")
            return -1
    
    # Get the item's id within a specific place
    def getItemId(self, name="", place=""):
        if self.inInventory(name) and (place in self.pl.get("inventory").keys()):
            return self.pl.get("inventory")[place].index(self.getItem(name))
        else:
            return -1
    
    # gain money to your wallet
    def gainMoney(self, amt=0):
        total = (self.pl.get("money") + amt) % 999999
        if total < 0:
            total = 0
        self.pl.setV("money", total)
    
    # Change player abilities
    def affectPl(self, name="", amt=0):
        if name in self.pl.info:
            self.pl.setV(name, self.pl.get(name)+amt)
