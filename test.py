import player
from tkinter import *
import logic

thought = logic.logic()
p1 = player.paladin()
p1.hurt(20)
p1.heal(30)
p1.attackOther()
p1.returnStats()
p1.shield()
p1.returnStats()
thought.playerTurn(p1)
input("...")
