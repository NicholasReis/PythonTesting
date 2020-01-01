class player:
    alive = True
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
