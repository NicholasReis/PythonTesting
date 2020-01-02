import livingThing
import random

class logic:
    h = livingThing.hero()
    characters = [livingThing.hero(), livingThing.hero(), livingThing.hero(), livingThing.hero(), livingThing.hero(), livingThing.hero(), livingThing.hero()]

    def evaluations(self):
        for people in self.characters:
            people.getStats()
            print("\n")


    def liveCheck(self):
        stop = len(self.characters)
        for lifeForm in self.characters:
            if not lifeForm.isAlive():
                print(str(lifeForm), " is dead!")
                stop = stop -1
                self.characters.remove(lifeForm)
            else:
                print("Alive!")
        if stop <= 1:
            return True
        else:
            return False

    def playerTurn(self):
        for lifeForm in range(0, len(self.characters)-1):
            if self.characters[lifeForm].isAlive():
                target = random.randint(0, len(self.characters)-1)
                if target == lifeForm:
                    self.characters[lifeForm].heal(self.characters[lifeForm].getMaxHealth()/5)
                else:
                    self.characters[lifeForm].attackOther(self.characters[target])
    def repopulate(self):
        tempPop = []
        for people in range(0, len(self.characters)):
            target = random.randint(0, len(self.characters)-1)
            if target == people:
                continue
            else:
                tempPop.append(self.characters[people].createChild(self.characters[target]))
        for newGuys in tempPop:
            self.characters.append(newGuys)
