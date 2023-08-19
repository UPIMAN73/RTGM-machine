## Save class
## All save types are written within this file
## Players, enemies, maps, items, etc

from jh import JsonHandler
from fh import FileHandler


class Save:
    def __init__(self, fname=""):
        self.fn = fname
        self.jh = JsonHandler(self.fn)

    def __del__(self):
        self.fn = None
        self.jh = None
    
    def exists(self, name=""):
        return self.jh.exists(name)

    def saveFile(self, setup={}):
        self.jh.write(setup)
        print("File Saved")

    def loadFile(self):
        if self.exists(self.fn):
            return self.jh.read()
        else:
            return {}