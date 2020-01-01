import random
class player:
    alive = True
    attack = 0
    defense = 0
    maxHealth = 0
    health = 0
    maxMana = 0
    mana = 0


    def isAlive(self):
        return self.alive

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense
        
    def heal(self, hp):
        if self.health + hp > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health = self.health + hp

    def hurt(self, pain):
        if self.health - pain < 0:
            self.health = 0
            self.alive = False
        else:
            self.health = self.health - pain

    def attackOther(self):
        print("Dealt", self.attack, "damage!")

    def returnStats(self):
        print("Alive: "+str(self.alive)+"\nHealth: " + str(self.health)+"/"+str(self.maxHealth)+"\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense))

class paladin(player):
    maxHealth = random.randint(15,30)
    health = maxHealth
    defense = random.randint(7, 12)
    attack = random.randint(11, 20)

    def shield(self):
        self.lastDefense = self.defense
        self.defense = self.defense + 10


###
#class paladin(player):
#    defense = 15
#    attack = 10
#    lastDefense = defense

#    def resetTurn(self):
#        self.defense = self.lastDefense
#        self.lastDefense = self.defense
#        self.defense = self.defense + 10
#        attacks = -1
###
