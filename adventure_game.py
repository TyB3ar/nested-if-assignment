# Task 1: Code Correction 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":               # Task 2: Setting the Scene
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch": 
        print("We find a tunnel to explore!")
    else: 
        print("It's too dark to see anything!") 
else:                               # Task 3: Default Path
    pass

