import livingThing
import logic


lt = livingThing.livingThing()
thought = logic.logic()
characters = [livingThing.livingThing(), livingThing.livingThing(), livingThing.livingThing(), livingThing.livingThing(), livingThing.livingThing()]
print(characters[0].getRace())
for p in range(0, 5):
    tempList = (characters[p], characters[p+1])
    characters.append(lt.createChild(tempList))

for people in characters:
    print(people.getRace())
    print(people.getJob())

#will likely need to make a list of all entities so they can act together instead of one after the other

input("...")
