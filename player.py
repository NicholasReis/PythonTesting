class player:
    alive = True
    attack = 0
    maxHealth = 100
    health = maxHealth
    maxMana = 50
    mana = maxMana

    def heal(self, hp):
        print("That hits the spot!")
        if self.health + hp > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health = self.health + hp

    def hurt(self, pain):
        print("Ouch!")
        if self.health - pain < 0:
            self.health = 0
            self.alive = False
        else:
            self.health = self.health - pain

    def attackOther(self):
        print("Dealt", self.attack, "damage!")

class paladin(player):
    defense = 15
    attack = 10
    lastDefense = defense

    def resetTurn(self):
        self.defense = self.lastDefense
    def shield(self):
        self.lastDefense = self.defense
        self.defense = self.defense + 10
        attacks = -1
