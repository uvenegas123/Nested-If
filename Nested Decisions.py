#Assignment 1 Task 1

place = input("Choose a place: forest or cave? ")

if place == 'forest':
    action = input('climb a tree or cross a river?') == 'climb a tree'
    if action:
        print("You found a bird's nest!")
    elif not action:
        print("You found a boat!")
else:        
    print("You find a hidden treasure!")



# Assignment 1 Task 2
place = input("Choose a place: forest or cave? ")

if place == 'forest':
    action = input('climb a tree or cross a river?') == 'climb a tree'
    if action:
        print("You found a bird's nest!")
    elif not action:
        print("You found a boat!")
if place == 'cave':
    light = input('Do you want to light a torch or proceed in the dark? (light/dark)') == 'light'
    if light:
        print('With the torch lit, the path becomes clear. Proceed.\n\n\nYou find a hidden treasure!')
    elif not light:
        print('This is a risky move. Proceed if you dare.')
        


#Assignment 1 Task 3

place = input("Choose a place: forest or cave? ")

if place == 'forest':
    action = input('climb a tree or cross a river?') 
    if action== 'climb a tree':
        print("You found a bird's nest!")
    elif action== 'cross a river':
        print("You found a boat!")
    else:
        pass
if place == 'cave':
    light = input('Do you want to light a torch or proceed in the dark? (light/dark)') 
    if light== 'light':
        print('With the torch lit, the path becomes clear. Proceed.\n\n\nYou find a hidden treasure!')
    elif light =='dark':
        print('This is a risky move. Proceed if you dare.')
    else:
        pass
