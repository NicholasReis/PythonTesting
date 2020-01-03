import random
import races
import jobs

class livingThing:
    r = races.races()
    j = jobs.jobs()
    alive = True
    gender = 0 #0 = Male, #1 = Female
    attack = 0
    defense = 0
    maxHealth = 0
    health = 0
    maxMana = 0
    mana = 0

    def getGender(self):
        return self.gender;

    def isAlive(self):
        return self.alive

    def getMaxHealth(self):
        return self.maxHealth

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

    def attackOther(self, target):
        strike = random.randint(0,20)
        if(strike > target.getDefense()):
            target.hurt(self.attack)

    def getStats(self):
        print("Alive: "+str(self.alive)+"\nHealth: " + str(self.health)+"/"+str(self.maxHealth)+"\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense))




class hero(livingThing):

    job = ""
    race = {}
    def __init__(self, ra = None, jo = None, tMaxHealth = None, tAttack = None, tDefense = None):
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

        if tMaxHealth is not None:
            self.maxHealth = tMaxHealth + j.jobHPBonus(self.job) + r.racialHPBonus(self.race)
        else:
            self.maxHealth = 10 + j.jobHPBonus(self.job) + r.racialHPBonus(self.race)
        self.health = self.maxHealth
        if tAttack is not None:
            self.attack = tAttack + j.jobAttackBonus(self.job) + r.racialAttackBonus(self.race)
        else:
            self.attack = 3 + j.jobAttackBonus(self.job) + r.racialAttackBonus(self.race)
        if tDefense is not None:
            self.defense = tDefense + j.jobDefenseBonus(self.job) + r.racialDefenseBonus(self.race)
        else:
            self.defense = 3 + j.jobDefenseBonus(self.job) + r.racialDefenseBonus(self.race)
        if self.defense > 19:
            self.defense = 19
        self.gender = random.randint(0,1)

    def getRace(self):
        return self.race

    def getJob(self):
        return self.job

    def setAttack(self):
        r = races.races()
        j = jobs.jobs()


    def createChild(self, parent):
        p1Job = self.getJob()
        p2Job = parent.getJob()
        p1Race = self.getRace()
        p2Race = parent.getRace()
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
        maxHealth = (self.getMaxHealth() + parent.getMaxHealth())/2
        attack = (self.getAttack() + parent.getAttack())/2
        defense = (self.getDefense() + parent.getDefense())/2
        return hero(race, job, maxHealth, attack, defense)


    def getStats(self):
        print("Alive: "+str(self.alive)+"\nRace: "+str(self.race)+"\nGender: "+str(self.gender)+"\nJob: "+str(self.job)+"\nHealth: " + str(self.health)+"/"+str(self.maxHealth)+"\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense))
