import random
import races
import jobs

class livingThing:
    r = races.races()
    j = jobs.jobs()

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
        strike = random.randint(0,20)
        if(strike > self.defense):
            if self.health - pain < 0:
                self.health = 0
                self.alive = False
            else:
                self.health = self.health - pain

    def attackOther(self, target):
        strike = random.randint(0,20)
        if(strike > self.defense):
            print("Dealt", self.attack, "damage!")

    def getStats(self):
        print("Alive: "+str(self.alive)+"\nHealth: " + str(self.health)+"/"+str(self.maxHealth)+"\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense))




class hero(livingThing):

    job = ""
    race = {}
    def __init__(self, ra = None, jo = None):
        alive = True
        j = jobs.jobs()
        r = races.races()
        if ra is not None:
            self.race = ra
        else:
            self.race = r.getRandomRace(random.randint(0,2))
        if jo is not None:
            self.job = jo
        else:
            self.job = j.getRandomJob(random.randint(0,1))
            
        self.maxHealth = 10+ j.jobHPBonus(self.job) + r.racialHPBonus(self.race)
        self.health = self.maxHealth
        self.attack = 3 + j.jobAttackBonus(self.job) + r.racialAttackBonus(self.race)
        self.defense = 3 + j.jobDefenseBonus(self.job) + r.racialDefenseBonus(self.race)

    def getRace(self):
        return self.race

    def getJob(self):
        return self.job

    def setAttack(self):
        r = races.races()
        j = jobs.jobs()


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


    def getStats(self):
        print("Alive: "+str(self.alive)+"\nRace: "+str(self.race)+"\nJob: "+str(self.job)+"\nHealth: " + str(self.health)+"/"+str(self.maxHealth)+"\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense))
