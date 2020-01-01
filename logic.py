import player
import enemy
class logic:
    def playerTurn(self, assets):
        for lifeForm in assets:
            if issubclass(type(lifeForm), player.player):
                print("This is a paladin")
            elif issubclass(type(lifeForm), enemy.enemy):
                print("This is an enemy ", type(lifeForm))
            else:
                print("This is", type(lifeForm))

    def liveCheck(self, assets):
        for character in assets:
            if not character.isAlive():
                print(str(character), " is dead!")
                assets.remove(character)
        return assets
