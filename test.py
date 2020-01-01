import player
import enemy
import logic

thought = logic.logic()
characters = [player.paladin()]
enemies = [enemy.shark()]
for p in characters:
    p.returnStats()
    print("\n")

characters = thought.liveCheck(characters)
print("\n")
for p in characters:
    p.returnStats()
    print("\n")
#will likely need to make a list of all entities so they can act together instead of one after the other
thought.playerTurn(characters)
thought.playerTurn(enemies)
input("...")
