import random
class enemy:
    alive = True
    maxHealth = 0
    health = 0
    attack = 0
    defense = 0

    def isAlive(self):
        return self.alive

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def hurt(self, pain):
        if self.health - pain < 0:
            self.health = 0
            self.alive = False
        else:
            self.health = self.health - pain

    def returnStats(self):
        print("Alive: "+str(self.alive)+"\nHealth: " + str(self.health)+"/"+str(self.maxHealth)+"\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense))

class shark(enemy):
    maxHealth = random.randint(6, 8)
    health = maxHealth
    attack = random.randint(13,18)
    defense = random.randint(8, 10)
