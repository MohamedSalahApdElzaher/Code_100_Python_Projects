#Project_12
#Create a Guessing Game

import random
from replit import clear

print("Welcome To The Number Guessing Game")
print("Iam thinking a number between 1 and 100")
guessed_number = random.randint(1,100)
level = input("Choose a diffeculty level. Type 'easy' or 'hard':")

def play_easy():
    print("You have a 10 attempts..good luck!")
    for i in range(1,10):
        print(f"You have attempets No {i} to guess")
        guess = int(input("Make a guess:"))
        if guessed_number > guess:
            print("TOO LOW\nGuess again")
        elif guessed_number < guess:
             print("TOO HIGH\nGuess again")  
        elif i == 5 and guessed_number != guess: 
            print("You fail :(") 
        else:
            print("You Get it! Congrats")  
            return
              

def play_hard():
     print("You have a 5 attempts..good luck!")
     for i in range(1,5):
        print(f"You have attempets No {i} to guess")
        guess = int(input("Make a guess:"))
        if guessed_number > guess:
            print("TOO LOW\nGuess again")
        elif guessed_number < guess:
             print("TOO HIGH\nGuess again") 
        elif i == 5 and guessed_number != guess: 
            print("You fail :(") 
        else:
            print("You Get it! Congrats")
            return  
          

if level == "easy":
    play_easy()
else:
    play_hard()

print("Correct answer:"+str(guessed_number))    
