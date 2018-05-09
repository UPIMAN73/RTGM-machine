## Battle Class
## Battle loop handler

import random
from ih import InventoryHandler
# from ph import PlayerHandler
# from eh import EnemyHandler


class Battle:
    def __init__(self, ph=None, eh=None, bossBattle=False):
        self.ph = ph
        self.eh = eh
        self.turn = None
        self.bossBattle = bossBattle
        self.runaway = False
        self.blocked = False
        self.pl_blocked = False
        self.en_blocked = False
    
    def __del__(self):
        self.ui = None
        self.ph = None
        self.eh = None
        self.turn = None
        self.bossBattle = None
        self.runaway = None
        self.pl_blocked = None
        self.en_blocked = None

    def battleLoop(self):
        plmean = self.ph.getMean()
        enmean = self.eh.getMean()
        if (plmean > enmean):
            self.turn = True
        else:
            chance = random.randint(0, 5)
            if (chance == 1):
                self.turn = True
            else:
                self.turn = False
        while ((self.ph.isDead() == False) and (self.eh.isDead() == False)) and (self.runaway == False):
            if (self.ph.isDead() or self.eh.isDead() or self.runaway):
                break
            print("\n\n")
            self.printStats()
            print("\n\n")
            if (self.turn):
                self.battlePrompt()
                self.turn = False
            else:
                self.aiChoice()
                self.turn = True
        if (self.ph.isDead()):
            print("Player " + self.ph.pl.get("name") + " has died...")
            return 0
        elif (self.eh.isDead()):
            print(self.eh.pl.get("name") + " has died...")
            return 1
        else:
            return 2

    def battlePrompt(self):
        choices = {"attack": self.attack, "block": self.block, "inventory":self.inventory, "run": self.run}
        user_input = None
        while user_input not in choices.keys():
            print("Choices: attack, block, inventory, run")
            user_input = raw_input("> ")
            if len(user_input) == 1:
                for i in choices.keys():
                    if user_input == i[0]:
                        user_input = i
                    else:
                        continue
            elif user_input in choices.keys():
                break
        choices.get(user_input, lambda: "INVALID OPTION")()

    def aiChoice(self):
        choices = [self.attack, self.block]
        choice = random.randint(0, len(choices)-1)
        choices[choice]()

    def attackPl(self, pl=None, eh=None):
        print(pl.get("name") + " has swung")
        damage = int(random.randint(0, pl.get("atk")))
        if (self.ph.pl.get("equipped")["weapon"] != "none"):
            damage += int(random.randint(0, pl.get("equipped")
                                         ["weapon"].get("atk")))
        weakness = 0
        listBonus = pl.get("equipped")["weapon"].listAbilities()
        for i in listBonus:
            weakness += random.randint(0, pl.get("equipped")
                                       ["weapon"].get("abilities")[i])
        listBonus = None
        damage += int(weakness)
        chance = random.randint(0, 10)
        if chance == 4:
            damage += random.randint(int(damage/2), damage)
        chance = None
        weakness = None
        eh.setHp(-damage)
        print(str(damage) + " damage")

    def attack(self):
        # player
        if self.turn == True:
            self.attackPl(self.ph.pl, self.eh)
        # enemy
        else:
            self.attackPl(self.eh.pl, self.ph)

    def blockPl(self, pl=None, eh=None):
        print(pl.get("name") + " has blocked")

        blocked = int(random.randint(0, pl.get("def")))
        chance = random.randint(0, 10)
        # equippment defense
        for i in pl.get("equipped").keys():
            if (i == "weapon"):
                continue
            amt = int(pl.get("equipped")[i].get("abilities")['def'])
            if (amt > 1):
                blocked += random.randint(0, int(amt/2))
            else:
                blocked += random.randint(0, 1)

        # armor section
        for i in pl.get("equipped armors").keys():
            amt = pl.get("equipped armors")[i].get("def")
            if (amt > 4):
                blocked += random.randint(0, int(amt/2))
            else:
                blocked += random.randint(0, 1)

        # critical defense
        if chance == 4:
            blocked += random.randint(0, int(blocked/2))

        eh.setHp(blocked)
        print(str(blocked) + " damage")

    def block(self):
        # player block
        if (self.turn == True and self.pl_blocked == False):
            self.pl_blocked = True
        
        # enemy block
        if (self.turn == False and self.en_blocked == False):
            self.en_blocked = True
        
        # both player and enemy block
        if (self.pl_blocked and self.en_blocked):
            print("You both blocked at the same time...\nNothing happened...")
            self.pl_blocked = False
            self.en_blocked = False
        
        # player blocks enemy
        elif (self.turn == False and self.pl_blocked == True):
            self.blockPl(self.ph.pl, self.eh)
            self.pl_blocked = False
        
        # enemy blocks player
        elif (self.turn == True and self.en_blocked == True):
            self.blockPl(self.eh.pl, self.ph)
            self.en_blocked = False
    
    # Run away
    def run(self):
        if self.bossBattle == True:
            print("You cannot run away.")

        elif self.ph.pl.get("spd") > self.eh.pl.get("spd"):
            chance = random.randint(0, 5)
            if chance == 1:
                print(self.ph.pl.get("name") + " succesfully ran away.")
                self.runaway = True
            else:
                print(self.ph.pl.get("name") +
                      " could not run away successfully.")

        else:
            chance = random.randint(0, 50)
            if chance == 7:
                print(self.ph.pl.get("name") + " succesfully ran away.")
                self.runaway = True
            else:
                print(self.ph.pl.get("name") +
                      " could not run away succesfully.")
    
    # Prints basic stats
    # Will change later so the game can make their own 
    def printStats(self):
        print("Player Stats: ")
        print("Name: " + self.ph.pl.get("name"))
        print("HP: " + str(self.ph.pl.get("hp")))
        print("MP: " + str(self.ph.pl.get("mp")))
        print("")
        print("Enemy Stats: ")
        print("Name: " + self.eh.pl.get("name"))
        print("HP: " + str(self.eh.pl.get("hp")))
        print("Mp: " + str(self.eh.pl.get("mp")))
    
    def inventory(self):
        inv = InventoryHandler(self.ph)
        inv.inventoryLoop()
        inv = None