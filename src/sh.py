## Store Handler
## Store interface within the store object

from store import Store
from ph import PlayerHandler
from armor import Armor
from weapons import Weapons
from item import Item, Potions


class StoreHandler:
    def __init__(self, ph=PlayerHandler(), store=Store()):
        self.ph = ph
        self.store = store
        self.quitCommands = ["quit", "exit", "q"]
        self.buyCommands = ["buy", "b", "purchase", "p"]
        self.sellCommands = ["sell", "s"]

    # main sell loop that allows the player to sell their items to the store
    def sellLoop(self):
        user_input = ""
        while user_input not in self.quitCommands:
            self.printSellInventory()
            user_input = str(raw_input("> "))
            if self.ph.inInventory(user_input):
                itemm = self.ph.getItem(user_input)
                if itemm != -1 and len(itemm) > 0:
                    # self.ph.get("inventory").pop(self.ph.get("inventory")[itemm[0]])
                    # self.store.get("")
                    print(itemm.get("name") + " sold for " +
                          itemm.get("price")["sell"])
        user_input = ""
        print("Anything else I can help you with...")

    # The main buy loop that allows the player to get what they need
    def buyLoop(self):
        user_input = ""
        while user_input not in self.quitCommands:
            self.printStoreInventory()
            print("Commands:  a, i, p, w")
            user_input = str(raw_input("> "))
            if user_input in self.quitCommands:
                break
            if user_input == "items" or user_input == "item" or user_input == "i":
                self.buySection("items")
            elif user_input == "weapons" or user_input == "weapon" or user_input == "w":
                self.buySection("weapons")
            elif user_input == "armor" or user_input == "armors" or user_input == "a":
                self.buySection("armors")
            elif user_input == "potions" or user_input == "potion" or user_input == "p":
                self.buySection("potions")
            else:
                print("Command does not exist.")
        user_input = ""
        print("Anything else I can help you with...")

    # Buy specific items from the store selection
    def buySection(self, name=""):
        user_input = ""
        if name in self.store.get("inventory").keys():
            while user_input not in self.quitCommands:
                self.printStoreSelected(name)
                user_input = str(raw_input("> "))
                if user_input in self.quitCommands:
                    print("Ok then... what else can I help you with?")
                    break
                elif user_input in self.store.getNames(name):
                    itm = self.store.findInv(name, user_input)
                    if itm.get("price")["buy"] <= self.ph.pl.get("money"):
                        if name == "armors":
                            self.ph.pl.get("armors").append(itm)
                        elif name == "weapons":
                            self.ph.pl.get("weapons").append(itm)
                        else:
                            self.ph.pl.get("inventory").append(itm)
                        self.store.delItem(name, user_input)
                        self.ph.gainMoney(-itm.get("price")["buy"])
                        print("YOU CAN BUY IT!")
                        self.printInventory()
                    else:
                        print("You do not have enough money to purchase this.")
                else:
                    print("That item does not exist.")
        else:
            print("ERROR!!!!\nTHIS DOES NOT EXISTS...")

    # Print the inventory of the store's items
    def printInventory(self):
        if len(self.ph.pl.get("inventory")) > 0:
            print("inventory" + ":")
            for x in self.ph.pl.get("inventory"):
                for i in self.ph.pl.get("inventory")[x]:
                    print(str(i.get("name") + "    " +
                              str(i.get("price")["buy"])))
                print("")
        print("")

    # print the inventory of the player to sell items
    def printSellInventory(self):
        for i in self.ph.pl.get("inventory"):
            print(str(i.get("name") + "    " + str(i.get("price")["sell"])))
        print("\n\n")

    # print store selected objects
    def printStoreSelected(self, name=""):
        if name in self.store.get("inventory").keys():
            print(name + ":")
            for i in self.store.get("inventory")[name]:
                print(str(i.get("name") + "    " + str(i.get("price")["buy"])))
            print("\n\n")

    # print store's inventory
    def printStoreInventory(self):
        for x in self.store.get("inventory").keys():
            if len(self.store.get("inventory")[x]) > 0:
                print(x + ":")
                for i in self.store.get("inventory")[x]:
                    print(str(i.get("name") + "    " +
                              str(i.get("price")["buy"])))
            print("")
        print("")

    # Print the main help of the store
    def printHelp(self):
        print("Buy or purchase from the store type one of these words: ")
        for i in self.buyCommands:
            print i,
        print("\nFor selling commands type one of these words: ")
        for i in self.sellCommands:
            print i,
        print("\nFor quitting the store entirely, type one of these words: ")
        for i in self.quitCommands:
            print i,
        print("\n\n")

    # Main loop for store handling
    def storeLoop(self):
        user_input = ""
        while user_input not in self.quitCommands:
            user_input = str(raw_input("> "))
            if user_input in self.quitCommands:
                print("Leaving Store...")
                break
            if user_input in self.buyCommands:
                print("Buying")
                self.buyLoop()
            elif user_input in self.sellCommands:
                print("Selling")
                self.sellLoop()
            else:
                self.printHelp()
        user_input = ""
