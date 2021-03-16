#Project_7
#Create a Hangman Game

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
word_list = ["apple","ardvark", "baboon","sports","camel","colors","airplane","programming"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)
print("Chosen word: "+chosen_word)
#creat an impty display list with dashs
display_list = []
for dash in chosen_word:
    display_list.append("-")
print("The Final Correct word should fit with this dash list")
print(display_list)

#list of stages of hangman :) 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

flag = False
lives = 6
while not flag:
    guess = input("Guess a letter: ").lower() 
    i=0  
    for letter in chosen_word:
        if letter == guess:
            display_list[i]=guess   
        i+=1  
    
    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            flag=True
            print("You Lose :(")
        print(stages[lives])             
   
    print(display_list) 
   
    if "-" not in display_list:
        flag=True
        print("You Finally Wins :)")
  
