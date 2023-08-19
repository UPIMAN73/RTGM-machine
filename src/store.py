## Store Object Class
## Store object structure is written within the class

class Store:
    def __init__(self, name="", des="", inventory={"weapons":[], "armors":[], "items":[], "potions":[]}):
        self.info = {
            "name": name,
            "des": des,
            "inventory": inventory
        }
    
    def get(self, arg):
        return self.info.get(arg, "INVALID")

    def setV(self, key, value):
        for i in self.info.keys():
            if (key == i):
                self.info[key] = value
                break
            else:
                continue
    
    def getNames(self, name=""):
        res = []
        x = self.get("inventory").get(name, "INVALID")
        if (x != "INVALID"):
            for i in x:
                res.append(i.get("name"))
        return res

    def findInv(self, location="", name=""):
        if location in self.get("inventory").keys():
            for i in self.get("inventory")[location]:
                if i.get("name") == name:
                    return i
        # return nothing
        return None
    
    def delItem(self, location="", name=""):
        if location in self.get("inventory").keys():
            self.get("inventory")[location].remove(self.findInv(location, name))
        else:
            print("Cant delete an item that does not exist.")
                    