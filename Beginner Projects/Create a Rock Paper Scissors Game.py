#Project_4
#Creat a Rock Paper Scissors Game

#import random module
import random

user_select = int(input("What do you choose ? 0 Rock, 1 Paper, 2 Scissors"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#make list of choicess
ch = [rock,paper,scissors]
computer_select = random.randint(0,len(ch)-1) 
print("\nYou_select:")
print(ch[user_select])
print("computer_select:")
print(ch[computer_select])
if user_select == 0 and computer_select == 2:
    print("You win!")
elif computer_select == 0 and user_select == 2:
    print("You lose")
elif computer_select > user_select:
    print("You lose")
elif user_select > computer_select:
    print("You win!")
elif computer_select == user_select:
    print("It's a draw")
 
