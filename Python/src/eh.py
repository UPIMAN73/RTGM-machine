## Enemy Handler
## Makes the enemy class function within the game

from save import Save
from enemy import Enemy


class EnemyHandler:
    def __init__(self, en=None):
        self.pl = en

    def __del__(self):
        self.pl = None
    
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

    def setMp(self, amount):
        mp = self.pl.get("mp")
        if amount >= 0:
            if (mp + amount > self.pl.info["mmp"]):
                self.pl.setV("mp", self.pl.info["mmp"])
            elif (mp + amount < 0):
                self.pl.setV("mp", 0)
            else:
                self.pl.setV("mp", mp+amount)
        mp = None
    
    def getMean(self):
        if (self.pl != None):
            return (self.pl.get("atk") + self.pl.get("def") + self.pl.get("spd") + self.pl.get("level"))/4
        else:
            return 0
    
