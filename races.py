import random

class races:
    def listOfRaces(self):
        return ["Human", "Elf", "Orc"]
        
    def getRandomRace(self, raceNum):
        if raceNum == 0:
            race = {}
            race["Human"] = 100
            race["Elf"]= 0
            race["Orc"]= 0
            return race
        elif raceNum == 1:
            race = {}
            race["Human"] = 0
            race["Elf"]= 100
            race["Orc"]= 0
            return race
        else:
            race = {}
            race["Human"] = 0
            race["Elf"]= 0
            race["Orc"]= 100
            return race

    def racialHPBonus(self, rDict):
        return ((rDict["Human"]/100)*1.3)+((rDict["Elf"]/100)*0.6)+((rDict["Orc"]/100)*1.8)

    def racialAttackBonus(self, rDict):
        return ((rDict["Human"]/100)*1)+((rDict["Elf"]/100)*0.7)+((rDict["Orc"]/100)*1.3)

    def racialDefenseBonus(self, rDict):
        return ((rDict["Human"]/100)*1.2)+((rDict["Elf"]/100)*0.4)+((rDict["Orc"]/100)*1.6)
