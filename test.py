import player
from tkinter import *
import logic

thought = logic.logic()
characters = [player.paladin(), player.paladin()]
for p in characters:
    p.returnStats()
    print("\n")
characters[0].hurt(120)

characters = thought.liveCheck(characters)
print("\n")
for p in characters:
    p.returnStats()
    print("\n")
#thought.playerTurn(p1)
input("...")
