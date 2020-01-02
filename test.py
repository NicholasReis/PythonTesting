import livingThing
import logic


thought = logic.logic()

round = 1
while round < 30 and not thought.liveCheck():
    print("Round: ", str(round))
    thought.playerTurn()
    thought.evaluations()
    round = round +1

# for p in range(0, 1):
#     tempList = (characters[p], characters[p+1])
#     characters.append(h.createChild(tempList))
#
# for people in characters:
#     people.getStats()
# characters[1].attackOther(characters[0])
# print("\n")
# thought.liveCheck(characters)
# for people in characters:
#     people.getStats()
#will likely need to make a list of all entities so they can act together instead of one after the other

input("...")
