## JSONHANDLER
## Handles json objects and writes the objects into a file.
import json
from fh import FileHandler

class JsonHandler:
    def __init__(self, fname=""):
        self.fname = fname
    
    def _bytefied(self, data, ingore_dicts=False):
        if isinstance(data, unicode):
            return data.encode('utf-8')
        elif isinstance(data, list):
            return [ self._bytefied(item, ingore_dicts=True) for item in data]
        elif isinstance(data, dict) and not ingore_dicts:
            return {
                self._bytefied(key, ingore_dicts=True): self._bytefied(value, ingore_dicts=True) for key,value in data
            }
        else:
            return data

    # write to file
    def write(self, obj):
        json.dump(obj, open(self.fname, "w"))
   
    # read from file
    def read(self):
        return self._bytefied(json.loads(FileHandler(self.fname).read()), ingore_dicts=True)
    
    def exists(self, name=""):
        return FileHandler(name).exists()

