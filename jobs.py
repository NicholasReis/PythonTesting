import random
class jobs:
    def getRandomJob(self, jobNum):
        if jobNum == 0:
            return "Paladin"
        elif jobNum == 1:
            return "Wizard"
        else:
            return "None"

    def jobHPBonus(self, jobType):
        if jobType == "Paladin":
            return random.randint(5, 7)
        elif jobType == "Wizard":
            return random.randint(1, 4)
        else:
            return random.randint(0, 6)

    def jobAttackBonus(self, jobType):
        if jobType == "Paladin":
            return random.randint(2, 4)
        elif jobType == "Wizard":
            return random.randint(4, 9)
        else:
            return random.randint(3, 10) #it's hard to be homeless

    def jobDefenseBonus(self, jobType):
        if jobType == "Paladin":
            return random.randint(5, 8)
        elif jobType == "Wizard":
            return random.randint(2, 5)
        else:
            return random.randint(3, 6)
