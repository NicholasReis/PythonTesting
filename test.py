import livingThing
import logic


thought = logic.logic()

round = 1
while round < 30 and not thought.liveCheck():
    print("Round: ", str(round))
    thought.playerTurn()
    thought.evaluations()
    round = round +1
    if round == 15:
        thought.repopulate()

input("...")
