import livingThing
import logic


h = livingThing.hero()
thought = logic.logic()
characters = [livingThing.hero(), livingThing.hero()]
for p in range(0, 1):
    tempList = (characters[p], characters[p+1])
    characters.append(h.createChild(tempList))

for people in characters:
    print(people.getRace())
    print(people.getJob())

#will likely need to make a list of all entities so they can act together instead of one after the other

input("...")
