## Inventory viewer/handler class
## Deals with inventory based actions

class InventoryHandler:
    def __init__(self, ph):
        self.ph = ph
        self.quitCommands = ["quit", "exit", "q"]
        self.keys = self.ph.pl.get("inventory").keys()

    def __del__(self):
        self.ph = None
        self.quitCommands = None
        self.keys = None

    # ITEM Manipulation
    def useItem(self, obj="", place="potions"):
        if self.ph.inInventory(obj) and (place in self.ph.pl.get("inventory").keys()):
            id = self.ph.getItemId(obj, place)
            itmm = self.ph.pl.get("inventory")[place].pop(id)
            for i in itmm.get("abilities").keys():
                if i == "hp":
                    self.ph.setHp(itmm.get("abilities")[i])
                elif i == "mp":
                    self.ph.setMp(itmm.get("abilities")[i])
                else:
                    self.ph.affectPl(name=i, amt=itmm.get("abilities")[i])
                print(i + "    " + str(self.ph.pl.get(i)))

        else:
            # Error message for use item
            print("USE ITEM ERROR")
            print("ERROR LOADING... ITEM DOES NOT EXIST")

    # USER INTERFACE INVENTORY HANDLING
    def printInventory(self, section=""):
        if section in self.ph.pl.get("inventory").keys():
            sec = self.ph.pl.get("inventory")[section]
            i = 0
            for x in sec:
                i += 1
                print(str(i) + "    " + x.get("name"))
            print("")
            sec = None
        else:
            print("That part does not exist.")
    
    # Section handler for an item
    def sectionHandling(self, name=""):
        if name in self.keys:
            itm = []
            for i in self.ph.pl.get("inventory")[name]:
                itm.append(i.get("name"))
            user_input = ""
            while user_input not in self.quitCommands:
                self.printInventory(name)
                user_input = str(raw_input("> "))

                # Quit
                if user_input in self.quitCommands:
                    break
                
                # Equip items
                elif (user_input == "equip" or user_input == "e") and (user_input != "potions"):
                    item_input = ""
                    while item_input not in self.quitCommands and not self.ph.inInventory(item_input):
                        self.printInventory(name)
                        print("\nSelect an item that is in your inventory")
                        item_input = str(raw_input("> "))
                        # Number based input
                        if item_input.isdigit():
                            item_input = int(item_input)
                            if item_input <= len(itm) and item_input > 0:
                                item_input = itm[item_input-1]
                        
                        # quit
                        if item_input in self.quitCommands:
                            break
                        
                        # item equip
                        elif item_input in self.ph.inInventory(item_input):
                            self.ph.equipItem(item_input)
                            break
                    item_input = None
                
                # Use item
                elif (user_input == "use" or user_input == "u") and (name == "potions"):
                    item_input = ""
                    while item_input not in self.quitCommands and not self.ph.inInventory(item_input):
                        self.printInventory(name)
                        item_input = str(raw_input("> "))
                        # Number based input
                        if item_input.isdigit():
                            item_input = int(item_input)
                            if item_input <= len(itm) and item_input > 0:
                                item_input = itm[item_input-1]
                        
                        # Quit
                        elif item_input in self.quitCommands:
                            break
                    self.useItem(item_input)
                    item_input = None
                
                # View item
                elif (user_input == "view" or user_input == "v"):
                    item_input = ""
                    while item_input not in self.quitCommands and not self.ph.inInventory(item_input):
                        self.printInventory(name)
                        item_input = str(raw_input("> "))
                        # Number based input
                        if item_input.isdigit():
                            item_input = int(item_input)
                            if item_input <= len(itm) and item_input > 0:
                                item_input = itm[item_input-1]
                        
                        # Quit
                        if item_input in self.quitCommands:
                            break
                    item_input = self.ph.getItem(item_input)
                    self.printSpecs(item_input)
                    item_input = None
                
                # Not a valid command
                else:
                    print("Not a valid command")

    # print specs of the object
    def printSpecs(self, obj):
        if obj != None:
            k = obj.info.keys()
            for j in k:
                if type(obj.info[j]).__name__ == "dict":
                    c = obj.info[j].keys()
                    for i in c:
                        print(i + ":    " + str(obj.info[j][i]))
                else:
                    print(j + ":    " + str(obj.info[j]))

    # Inventory loop
    def inventoryLoop(self):
        user_input = ""
        while user_input not in self.quitCommands:
            print("The commands for navigating are: ")
            for i in range(0, len(self.keys)):
                print self.keys[i],
            print("")
            user_input = str(raw_input('> '))
            if user_input in self.quitCommands:
                break
            elif len(user_input) == 1:
                for i in self.keys:
                    if user_input == i[0]:
                        self.sectionHandling(i)
            elif user_input in self.keys:
                self.sectionHandling(user_input)
            else:
                print("That does not exist")
        user_input = None
