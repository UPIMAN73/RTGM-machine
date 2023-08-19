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
from store import Store

# Game Objects handler
from ph import PlayerHandler
from eh import EnemyHandler
from fh import FileHandler
from sh import StoreHandler
from ih import InventoryHandler

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
        self.game_name = "test"
        self.ui = UserInterface(ph=self.ph, eh=self.eh, defDir=str("~/rtgm/games/" + self.game_name))

    # def __del__(self): 
        # self.pl = None
        # self.map = None
        # self.mh = None
        # self.ph = None   
        # self.ui = None 

    def mapSetup(self):
        self.map.setV("name", "earth")
        self.map.setV("msg", "This planet is named Earth. There are many mysteries that lie inside of this planet. ")
        # self.ph.mh.map = self.map
        self.ph.mh.loadMap("earth.json")

    def plSetup(self):
        from pc import PlayerCreator
        plc = PlayerCreator()
        plc.createLoop()
        self.pl = plc.pl
        self.ph = PlayerHandler(self.pl)
    
    def createEnemy(self):
        return Enemy(name="goblin", mhp=100, atk=8, pdef=4, spd=10)
    
    def uiTest(self):
        # self.plSetup()
        self.ui = UserInterface(ph=self.ph, eh=self.eh)
        self.ui.UILoop()

    def enemySetup(self):
        enemy = self.createEnemy()
        self.eh = EnemyHandler(enemy)
    
    def battleTest(self):
        battle = Battle(self.ph, self.eh)
        battle.battleLoop()
    
    def storeSetup(self):
        store = Store(name="Shop", des="Just an average shop")
        store.get("inventory")["items"].append(Item(name="testitem", des="This item is test item."))
        sh = StoreHandler(self.ph, store)
        sh.storeLoop()
    
    def inventorySetup(self):
        inventory = InventoryHandler(self.ph)
        inventory.inventoryLoop()

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

#game.storeSetup()
# game.inventorySetup()
#game.ui.saveGame()
#game.ui.loadGame()
#game.ui.loadGame()