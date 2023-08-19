## User input Class
## Deals with user input, user handling, and command based objects within the game

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

# System based
from os import system


class UserInterface:
    def __init__(self, ph=PlayerHandler(), eh=EnemyHandler(), defDir=""):
        # Game Objects
        self.ph = ph
        self.eh = eh
        self.eh.pl = Enemy(name="goblin", mhp=100, atk=8, pdef=4, spd=10)

        # Command Line Interface
        self.defDir = defDir
        self.quitcmd = ["quit", "exit", "q"]
        self.defcommands = {"help":self.displayHelp, "save":self.saveGame, "load":self.loadGame, "play":self.playGame, "inventory":self.inventory, "i":self.inventory}
        self.commands = {"battle":self.battle, "fight":self.battle}
        if (self.ph.mh != None):
            inputs = self.ph.mh.current_location.get("commands")["inputs"]
            if len(inputs) > 0:
                self.commands = inputs
        
        # Help 
        self.defHelp = "def_help.txt"
        self.helpfile = FileHandler(self.defHelp)
        if self.helpfile.exists() and self.helpfile.isFile():
            self.help = self.helpfile.readLines()
        else:
            self.help = []
        
        # Game Over
        self.defGameOver = "def_game_over.txt"
        self.gameOverFile = FileHandler(self.defGameOver)
        if self.gameOverFile.exists() and self.gameOverFile.isFile():
            self.gameO = self.gameOverFile.readLines()
        else:
            self.gameO = []
    
    def __del__(self):
        self.quitcmd = None
        self.defDir = None
        self.userLoop = None
        self.defcommands = None
        self.commands = None
        self.defHelp = None
        self.helpfile.__del__()
        self.helpfile = None
        self.help = None
        self.defGameOver = None
        self.gameOverFile.__del__()
        self.gameOverFile = None
        self.gameO = None
        #self.eh.__del__()
        self.eh = None
        #self.mh.__del__()
        self.mh = None
        #self.ph.__del__()
        self.ph = None
    
    def UILoop(self):
        user_input = " "
        while user_input not in self.quitcmd:
            user_input = raw_input("> ")
            if user_input in self.quitcmd:
                break
            elif user_input in self.defcommands:
                self.defcommands.get(user_input, lambda:"INVALID")()
            else:
                self.execute(user_input)
        # try:
        #     while user_input not in self.quitcmd:
        #         user_input = raw_input("> ")
        #         if user_input in self.quitcmd:
        #             break
        #         elif user_input in self.defcommands:
        #             self.defcommands.get(user_input, lambda:"INVALID")()
        #             print("DONE")
        #         else:
        #             self.execute(user_input)
        # finally:
        #     user_input = None
        #     print("Thanks for playing")
        #     exit()

    # display help text
    def displayHelp(self):
        for i in self.help:
            print i
    
    def printGameOver(self):
        for i in self.gameO:
            print i
    
    def saveGame(self):
        self.ph.savePl()
        print("Saved Game")
    
    def loadGame(self):
        self.ph.loadPl()
        system("clear")
        print("Loaded Game")
    
    def playGame(self):
        user_input = ""
        while self.ph.mh.exists(user_input) == False and user_input not in self.quitcmd:
            print("\n\n")
            print("Game or Map name?")
            user_input = raw_input("> ")
        self.setupGame(user_input)
        user_input = None
    
    def setupGame(self, name=""):
        if (self.ph.mh != None):
            if self.ph.mh.exists(name):
                self.ph.mh.ms.fn = name
                self.ph.mh.loadMap()
                self.commands = self.ph.mh.current_location.get("commands")["inputs"]
                print("Game loaded succesfully...\nEnjoy!!!\n")
            else:
                print("That map does not exist...\nMake sure that the map file is located in the right place.")
        else:
            print("There is no Map Handler.")
    
    def execute(self, cmd=""):
        if cmd in self.commands:
            self.commands.get(cmd, lambda:"INVALID")()
        else:
            print("Invalid Command")
            self.displayHelp()
    
    def getPlace(self):
        return self.ph.mh.current_location
    
    def battle(self):
        battle = Battle(self.ph, self.eh)
        bres = battle.battleLoop()
        if bres == 0:
            print("You died...")
            print("\n\n")
            self.printGameOver()
        elif bres == 1:
            print("You won!!!")
        elif bres == 2:
            print("You ran away...")
        else:
            print("Battle broken")
    
    def inventory(self):
        inv = InventoryHandler(self.ph)
        inv.inventoryLoop()
        inv = None
            