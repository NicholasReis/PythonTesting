import player
from tkinter import *
import logic

thought = logic.logic()
p1 = player.paladin()
p2 = player.paladin()
characters = [p1, p2]
for p in characters:
    p.returnStats()
    print("\n")
p1.hurt(120)

characters = thought.liveCheck(characters)
print("\n")
for p in characters:
    p.returnStats()
    print("\n")
#thought.playerTurn(p1)
input("...")
