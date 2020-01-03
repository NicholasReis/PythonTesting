import livingThing
import logic


thought = logic.logic()
maxRounds = 100
round = 1
while round < maxRounds and not thought.liveCheck():
    print("Round: ", str(round))
    print("Fighters: ", str(thought.numOfFighters()))
    thought.playerTurn()
    round = round +1
    if round%10 == 0 and round != maxRounds:
        thought.repopulate()
        thought.evaluations()

if round == maxRounds:
    print("Time has run out!")
    print("WINNERS: ")
else:
    print("We have a winner after ", str(round) ," rounds!")

thought.evaluations();

input("...")
