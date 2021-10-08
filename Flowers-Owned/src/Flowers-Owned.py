# This program is to check which flowers I have bought from Nook's Cranny
# in Animal Crossings: New Horizons. If I don't have the flower and I decide
# to buy it, the list of flowersOwned will be updated

# If this is your first time using this program, change the "r" to "x" in order to create the .txt file
# After using this program for the first time, change the "x" back to an "r"
flowersOwnedFile = open("Flowers-Owned.txt", "r")

flowersOwned = []

for line in flowersOwnedFile.readlines():
    line = line.strip()
    flowersOwned.append(line)

flowerBeingChecked = input("Which flower are you looking to buy?\n")

if flowerBeingChecked in flowersOwned:
    print("You already have this flower")
else:
    print("You don't have this flower")
    purchase = input("Did you buy " + flowerBeingChecked + "?\n")
    if purchase in ["Yes", "y", "Y", "yes"]:
        flowersOwnedFile = open("Flowers-Owned.txt", "w")
        flowersOwned.append(flowerBeingChecked)
        flowersOwned.sort(key=str.lower)
        for i in range(len(flowersOwned)):
            flowersOwnedFile.write(flowersOwned[i] + "\n")
        print("Done, see ya!")
    else:
        print("Ok, bye")


flowersOwnedFile.close()
