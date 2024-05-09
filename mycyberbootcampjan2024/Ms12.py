# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in yes_no:
    response = input("Are you ready for more of the adventure?\nyes/no\n")
    if response == "yes":
        print("You start your journey, searching for materials to build your house.")
        print("The forest is huge, and there are many paths to explore.\n")
    elif response == "no":
        print("You decide to stay put for now. Maybe another time, " + name + ".")
        quit()
    else: 
        print("Sorry, I didn't understand that.\n")
response = ""
while response not in directions:
    response = input("You come to a crossroads. Which direction will you choose?\nleft/right/forward/backward\n")
    if response == "left":
        print("You take the left path and find a field of straw.")
        print("It's lightweight and easy to gather. Do you want to use it to build your house?\n")
        choice = input("yes/no\n")
        if choice == "yes":
            print("You quickly build a house out of straw. It's not very sturdy, but it will do for now.")
        elif choice == "no":
            print("You decide to look for stronger materials.")
    elif response == "right":
        print("You choose the right path and discover a pile of sticks.")
        print("They are stronger than straw but still not very sturdy. Do you want to use them?\n")
        choice = input("yes/no\n")
        if choice == "yes":
            print("You use the sticks to build your house. It's stronger than straw, but still not very safe.")
        elif choice == "no":
            print("You continue your search for better materials.")
    elif response == "forward":
        print("You decide to go straight ahead, deeper into the forest.")
        print("You stumble upon a pile of bricks.")
        print("Bricks are heavy and hard to work with, but they make the sturdiest houses.")
        print("Do you want to use bricks to build your house?\n")
        choice = input("yes/no\n")
        if choice == "yes":
            print("You spend time building a sturdy house out of bricks. It's strong and safe from the Big Bad Wolf!")
            print("Congratulations, " + name + "! You have built a secure home and escaped the wolf!")
            quit()
        elif choice == "no":
            print("You decide to keep searching for other materials.")
    elif response == "backward":
        print("You turn back, feeling uncertain about the path ahead.")
        print("Perhaps it's best to retrace your steps and choose a different path.")
print("As you're busy building your house, you hear a growl behind you.")
print("You turn around and see the Big Bad Wolf approaching!")
print("What do you do?\n")
choice = input("fight/run\n")
if choice == "fight":
    print("You gather your courage and decide to stand your ground against the wolf.")
    print("You throw rocks and sticks at the wolf, but it's no match for its strength.")
    print("The wolf easily blows down your house and chases you away!")
    print("You run for your life, hoping to find safety somewhere else.")
    quit()
elif choice == "run":
    print("You panic and decide to run away as fast as you can.")
    print("You abandon your house and flee into the forest, hoping to outrun the wolf.")
    print("You manage to escape for now, but you know the wolf will keep chasing you.")
    print("You need to find a safer place to build your house!")
    print("You continue your journey through the forest.")
response = ""
while response not in directions:
    response = input("You come to another crossroads. Which direction will you choose?\nleft/right/forward/backward\n")
    if response == "left":
        print("You take the left path and stumble upon a cozy cave.")
        print("It seems like a safe place to build your house. Do you want to use it?\n")
        choice = input("yes/no\n")
        if choice == "yes":
            print("You decide to make the cave your new home. It's secure and sheltered from the wolf!")
            print("Congratulations, " + name + "! You have found a safe haven and escaped the wolf!")
            quit()
        elif choice == "no":
            print("You decide to keep searching for a better location.")
    elif response == "right":
        print("You choose the right path and find a friendly beaver building a dam.")
        print("The beaver offers to help you build a house out of wood from the forest.")
        print("Do you accept the beaver's offer?\n")
        choice = input("yes/no\n")
        if choice == "yes":
            print("You accept the beaver's help and work together to build a sturdy wooden house.")
            print("The house is strong and secure, and the beaver warns you if the wolf ever approaches.")
            print("You feel safe and protected in your new home.")
            print("Congratulations, " + name + "! You have built a safe house and escaped the wolf!")
            quit()
        elif choice == "no":
            print("You decide to decline the beaver's offer and continue your search for a suitable location.")
    elif response == "forward":
        print("You decide to go straight ahead, deeper into the forest.")
        print("You come across a group of friendly animals building a village.")
        print("They invite you to join them and offer to help you build a house.")
        print("Do you accept their offer?\n")
        choice = input("yes/no\n")
        if choice == "yes":
            print("You accept the animals' offer and work together to build a beautiful house.")
            print("The house is well-protected, and you have many friends to keep you company.")
            print("You feel happy and secure in your new home.")
            print("Congratulations, " + name + "! You have built a house and escaped the wolf!")
            quit()
        elif choice == "no":
            print("You decide to continue your journey alone, hoping to find a better place to build your house.")
    elif response == "backward":
        print("You turn back, feeling uncertain about the path ahead.")
        print("Perhaps it's best to retrace your steps and choose a different path.")
print("After a series of adventures and challenges, you finally find the perfect spot to build your house.")
print("The house is secure, and you feel safe from the Big Bad Wolf.")
print("Congratulations, " + name + "! You have successfully built a safe house and escaped the wolf's clutches.")

