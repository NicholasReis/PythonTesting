import player
class logic:
    def playerTurn(self, charType):
        if type(charType) == player.paladin:
            print("This is a paladin")
        else:
            print("This is", type(charType))
