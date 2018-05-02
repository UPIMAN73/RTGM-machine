## File Handler
## Deals with file read and write
import os.path


class FileHandler:
    def __init__(self, fname=""):
        self.fname = fname
        self.f = None
    
    def __del__(self):
        self.fname = None
        self.f = None

    def write(self, contents):
        self.f = open(self.fname, "w")
        self.f.write(contents)
        self.f.close()
    
    def read(self):
        res = ""
        self.f = open(self.fname, "r")
        res = self.f.read()
        self.f.close()
        print(res)
        return res
    
    def readLines(self):
        res = self.read()
        return res.split("\n")

    def exists(self):
        return os.path.exists(self.fname)
    
    def isFile(self):
        return os.path.isfile(self.fname)