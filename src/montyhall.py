# Monty Hall Problem, by Al Sweigart al@inventwithpython.com
# A simulation of the Monty Hall Problem.
# More info at https://en.wikipedia.org/wiki/Monty_Hall_problem

import random, sys

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT  = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT  = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT  = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

print('THE MONTY HALL PROBLEM')
print('By Al Sweigart al@inventwithpython.com')
print()
print('In the Monty Hall game show, you can pick one of three doors. One door')
print('has a brand new car for a prize. The other two doors have worthless goats:')
print(ALL_CLOSED)
print('Say you pick Door #1.')
print('Before the door you choose is opened, another door with a goat is opened:')
print(THIRD_GOAT)
print('You can choose to either open the door you originally picked, or switch')
print('to the other unopened door.')
print()
print('It may seem like it doesn\'t matter if you switch or not, but your odds')
print('do improve if you switch doors! This program demonstrates the Monty Hall')
print('problem by letting you do repeated experiments.')
print()
print('You can read an explanation of why switching is better at')
print('https://en.wikipedia.org/wiki/Monty_Hall_problem')
print()
input('Press Enter to start...')



switchWins = 0
switchLosses = 0
notSwitchWins = 0
notSwitchLosses = 0
while True:
    doorThatHasCar = random.randint(1, 3) # The computer picks which door has the car.

    # Ask the player to pick a door:
    print(ALL_CLOSED)
    while True: # Keep asking the player until they enter a valid door.
        print('Pick a door 1, 2, or 3 (or "quit" to stop):')
        doorPick = input().upper()
        if doorPick == 'QUIT':
            # End the game.
            print('Thanks for playing!')
            sys.exit()

        if doorPick == '1' or doorPick == '2' or doorPick == '3':
            break
    doorPick = int(doorPick)

    # Figure out which goat door to show the player.
    while True: # Select a door that is a goat and not picked by the player.
        goatDoorOpened = random.randint(1, 3)
        if goatDoorOpened != doorPick and goatDoorOpened != doorThatHasCar:
            break

    # Show this goat door to the player:
    if goatDoorOpened == 1:
        print(FIRST_GOAT)
    elif goatDoorOpened == 2:
        print(SECOND_GOAT)
    elif goatDoorOpened == 3:
        print(THIRD_GOAT)

    print('Door %s contains a goat!' % (goatDoorOpened))

    # Ask the player if they want to switch:
    while True: # Keep asking until the player enters Y or N.
        print('Do you want to switch doors? Y/N')
        switch = input().upper()
        if switch == 'Y' or switch == 'N':
            break

    # Switch the player's door if they wanted to switch:
    if switch == 'Y':
        if doorPick == 1 and goatDoorOpened == 2:
            doorPick = 3
        elif doorPick == 1 and goatDoorOpened == 3:
            doorPick = 2
        elif doorPick == 2 and goatDoorOpened == 1:
            doorPick = 3
        elif doorPick == 2 and goatDoorOpened == 3:
            doorPick = 1
        elif doorPick == 3 and goatDoorOpened == 1:
            doorPick = 2
        elif doorPick == 3 and goatDoorOpened == 2:
            doorPick = 1

    # Open all the doors:
    if doorThatHasCar == 1:
        print(FIRST_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 2:
        print(SECOND_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 3:
        print(THIRD_CAR_OTHERS_GOAT)

    print('Door %s has the car!' % (doorThatHasCar))

    # Record wins and losses for switching and not switching:
    if doorPick == doorThatHasCar:
        print('You won!')
        if switch == 'Y':
            switchWins += 1
        elif switch == 'N':
            notSwitchWins += 1
    else:
        print('Sorry, you lost.')
        if switch == 'Y':
            switchLosses += 1
        elif switch == 'N':
            notSwitchLosses += 1

    # Calculate success rate of switching and not switching:
    if (switchWins + switchLosses) != 0: # Prevent zero-divide error.
        switchSuccess = round(switchWins / (switchWins + switchLosses) * 100, 1)
    else:
        switchSuccess = 0.0
    if (notSwitchWins + notSwitchLosses) != 0: # Prevent zero-divide error.
        notSwitchSuccess = round(notSwitchWins / (notSwitchWins + notSwitchLosses) * 100, 1)
    else:
        notSwitchSuccess = 0.0
    print()
    print('Switching:     %s wins, %s losses, success rate %s%%' % (switchWins, switchLosses, switchSuccess))
    print('Not switching: %s wins, %s losses, success rate %s%%' % (notSwitchWins, notSwitchLosses, notSwitchSuccess))
    print()
    print('Press Enter repeat the experiment again!')
    input()

