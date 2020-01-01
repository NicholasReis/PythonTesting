import player
class logic:
    def playerTurn(self, charType):
        if type(charType) == player.paladin:
            print("This is a paladin")
        else:
            print("This is", type(charType))
    def liveCheck(self, assets):
        for character in assets:
            if not character.isAlive():
                assets.remove(character)
        return assets
