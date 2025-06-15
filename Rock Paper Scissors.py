import random
import modul1

print("Welcome to Rock Paper Scissors Python version! Ready to challenge the computer? 😏")
what_to_play = int(input("Choose wisely: 0 for Rock, 1 for Paper, and 2 for Scissors: "))

computing_play = random.randint(0, 2)

# Rock (0) beats Scissors (2), loses to Paper (1)
if what_to_play == 0:
    print("Your play is:\n")
    print(modul1.rock)
    if computing_play == 2:
        print("Computer play is:\n")
        print(modul1.scissors)
        print('You win! 🎉🎉🎉')
    elif computing_play == 0:
        print("Computer play is:\n")
        print(modul1.rock)
        print("It's a draw! 🔥")
    elif computing_play == 1:
        print("Computer play is:\n")
        print(modul1.paper)
        print("You lose! 😈😈😈")

# Paper (1) beats Rock (0), loses to Scissors (2)
elif what_to_play == 1:
    print("Your play is:\n")
    print(modul1.paper)  # Fixed: was showing rock instead of paper
    if computing_play == 2:
        print("Computer play is:\n")
        print(modul1.scissors)
        print('You lose! 😈😈😈')
    elif computing_play == 0:
        print("Computer play is:\n")
        print(modul1.rock)
        print("You win! 🎉🎉🎉")
    elif computing_play == 1:
        print("Computer play is:\n")
        print(modul1.paper)
        print("It's a draw! 🔥")

# Scissors (2) beats Paper (1), loses to Rock (0)
elif what_to_play == 2:
    print("Your play is:\n")
    print(modul1.scissors)  # Fixed: was showing rock instead of scissors
    if computing_play == 2:
        print("Computer play is:\n")
        print(modul1.scissors)
        print("It's a draw! 🔥")
    elif computing_play == 0:
        print("Computer play is:\n")
        print(modul1.rock)
        print("You lose! 😈😈😈")
    elif computing_play == 1:
        print("Computer play is:\n")
        print(modul1.paper)
        print("You win! 🎉🎉🎉")
else:
    print("Invalid choice! Please enter 0, 1, or 2.")
