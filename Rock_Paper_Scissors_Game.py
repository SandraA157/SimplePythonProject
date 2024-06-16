#Task: Rock, Paper, Scissors Game!

import random
print("Welcome to the Rock, Paper, Scissors Game!")

player_choice=input("Enter your choice (rock, paper, or scissors):")
mylist = ["rock", "paper", "scissors"]
computer_choice= random.choice(mylist)

print("Player chose: ",player_choice)
print("Computer chose: ", computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("Player wins! {} beats {}.".format(player_choice, computer_choice))
else:
    print("Computer wins! {} beats {}.".format(computer_choice, player_choice))
