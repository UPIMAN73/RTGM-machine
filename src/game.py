## Game Class
## Deals with game mechanics and features
## Player creation and other objects will be made here

## Save file
## json file format
## Player are a json file
## items are json objects
## Must come up with a world

# Game Objects
from map import Map, Level
from player import Player
from enemy import Enemy
from weapons import Weapons
from item import Item, Potions
from armor import Armor

# Game Objects handler
from ph import PlayerHandler
from eh import EnemyHandler
from fh import FileHandler

# Command based 
from battle import Battle

#from command import Command
from ui import UserInterface


class Game:
    def __init__(self):
        # Game Objects
        self.pl = Player()
        self.map = Map()
        self.ph = PlayerHandler()
        self.eh = EnemyHandler()
        self.ui = UserInterface(ph=self.ph, eh=self.eh)

    # def __del__(self): 
        # self.pl = None
        # self.map = None
        # self.mh = None
        # self.ph = None   
        # self.ui = None 

    def mapSetup(self):
        # self.map.setV("name", "earth")
        # self.map.setV("msg", "This planet is named Earth. There are many mysteries that lie inside of this planet. ")
        # self.ph.mh.map = self.map
        self.ph.mh.loadMap("earth.json")

    def plSetup(self):
        name = "Joshua"
        pclass = "Demon Slayer"
        self.pl = Player(name, pclass)
        self.pl.setV("equipped", {"weapon": Weapons(name="death scyth", atk=15), "talisman": Item(), "bracelet": Item(), "ring": Item()})
        self.ph = PlayerHandler(pl=self.pl)
    
    def createEnemy(self):
        return Enemy(name="goblin", mhp=100, atk=8, pdef=4, spd=10)
    
    def uiTest(self):
        self.plSetup()
        self.ui = UserInterface(ph=self.ph, eh=self.eh)
        #self.ui.UILoop()

    def enemySetup(self):
        enemy = self.createEnemy()
        self.eh = EnemyHandler(enemy)
    
    def battleTest(self):
        battle = Battle(self.ph, self.eh)
        battle.battleLoop()

# import json

# name = "Joshua"
# pclass = "Demon Slayer"
# test = Player(name, pclass)
# fname = test.get("name") + ".json"
# f = open(fname, "w")
# f.write(json.dumps(test.toJson()))
# f.close()


game = Game()
game.mapSetup()
game.plSetup()
game.uiTest()
game.ui.UILoop()
#game.ui.saveGame()
#game.ui.loadGame()
#game.ui.loadGame()