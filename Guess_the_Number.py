#Task: Guess the Number
import random

count=0
yes=0
number = random.randint(1, 100)

print("Welcome to the Guess the Number game!")
print ("I'm thinking of a number between 1 and 100.")
guess = int(input("Take a guess: "))

while yes==0:
    if guess < number:
        print("too low")
        count = count + 1
        guess = int(input("Take a guess: "))
    elif guess > number:
        print("too high")
        count = count + 1
        guess = int(input("Take a guess: "))
    elif guess == number:
        print("Congratulations! You guessed the number in", count, "attempts.")
        yes = yes + 1
    else:
        print("out of range!")
        count = count + 1
        guess = int(input("Take a guess: "))
