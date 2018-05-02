## Command Handler
## command details are setup within a text file
## Command Structures are setup within two different classes
## Default Class:
## Deals with normal/default game 
from fh import FileHandler


class Commands:
    def __init__(self, cinput=[], output=[]):
        self.info = {
            "inputs": [],
            "outputs": []
        }
    
    def __del__(self):
        self.info = None
    
    def exists(self, ary=[], arg=""):
        res = False
        if len(ary) > 0:
            for i in ary:
                if arg == i:
                    res = True
                    break
        return res
    
    def get(self, arg):
        return self.info.get(arg, "INVALID")

    def setV(self, key, value):
        for i in self.info.keys():
            if (key == i):
                self.info[key] = value
                break
            else:
                continue