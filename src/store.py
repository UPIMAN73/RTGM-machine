## Store Object Class
## Store object structure is written within the class

class Store:
    def __init__(self):
        self.info = {}
    
    def get(self, arg):
        return self.info.get(arg, "INVALID")

    def setV(self, key, value):
        for i in self.info.keys():
            if (key == i):
                self.info[key] = value
                break
            else:
                continue