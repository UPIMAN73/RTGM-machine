## Map Handler
## Handles map functionality

from save import Save
from map import Map, Level
from battle import Battle

class MapHandler:
    def __init__(self, mp=Map()):
        self.map = mp
        self.current_location = Level()
        self.msave = {}
        if mp != None:
            self.msave = mp.info
            self.ms = Save(str(mp.get("name")) + ".json")
        else:
            self.ms = Save("")
        
    def __del__(self):
        self.map = None
        self.current_location = None
        self.msave = None
        self.ms = None
    
    def exists(self, name=""):
        return self.ms.exists(name)
    
    def welcomeScreen(self):
        print(self.map.get("msg"))

    def printMsg(self):
        print(self.current_location.get("msg"))

    def lexists(self, location=""):
        res = False
        for i in self.map.get("levels"):
            if i.get("name") == location:
                res = True
                break
        return res
    
    def goto(self, location):
        if self.lexists(location):
            self.current_location = location
        else:
            print(location + " does not exist.")
    
    def saveMap(self):
        if (self.ms.fn == ".json"):
            self.ms = Save(str(self.map.get("name")) + ".json")
        if (self.msave != self.map.info):
            self.msave = self.map.info
        self.ms.saveFile(self.msave)
    
    def loadMapFile(self):
        self.map.info = self.ms.loadFile()
        print(self.map.info)
    
    def loadMap(self, name=""):
        if self.ms.exists(name):
            self.ms.fn = name
            self.loadMapFile()
    
    def loadLocation(self, name=""):
        if self.map.levelExists(name):
            if (self.map.getLevel(name) != None):
                self.current_location = self.map.getLevel(name)
            else:
                print("Location does not exist in the game or on the map.")
    
    def locationType(self):
        for i in self.current_location.info.keys():
            if (self.current_location[i] == True):
                return i
        return ""