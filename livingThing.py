import random
import races
import jobs

class livingThing:
    alive = True

     #job = classes.getRandomClass()
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




class hero(livingThing):
    def __init__(self, ra = None, cl = None):
        alive = True
        if ra is not None:
            self.race = ra
        else:
            r = races.races()
            self.race = r.getRandomRace(random.randint(0,2))
        if cl is not None:
            self.job = cl
        else:
            c = jobs.jobs()
            self.job = c.getRandomJob(random.randint(0,1))
    def getRace(self):
        return self.race

    def getJob(self):
        return self.job

    def createChild(self, parents):
        p1Job = parents[0].getJob()
        p2Job = parents[1].getJob()
        p1Race = parents[0].getRace()
        p2Race = parents[1].getRace()
        #Initializes and creates inherited race
        race = {}
        race["Human"] = 100*(p1Race["Human"]/200 + p2Race["Human"]/200)
        race["Elf"] =  100*(p1Race["Elf"]/200 + p2Race["Elf"]/200)
        race["Orc"] = 100*(p1Race["Orc"]/200 + p2Race["Orc"]/200)
        jobNum = random.randint(0,3)
        job = ""
        if jobNum == 0:
            job = p1Job
        elif jobNum == 1:
            job = p2Job
        else:
            j = jobs.jobs()
            job = j.getRandomJob(random.randint(0,3))

        return hero(race, job)
#    def resetTurn(self):
#        self.defense = self.lastDefense
#        self.lastDefense = self.defense
#        self.defense = self.defense + 10
#        attacks = -1
###
