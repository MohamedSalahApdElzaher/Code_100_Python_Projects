#Project_10
#Create a Calculator App

from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def calculate():
    print(logo)
    n1 = float(input("Enter First number..?\n"))
    print("\n+\n-\n*\n/\n\npick an operand..?\n")
    operand = input()
    n2 = float(input("Enter Second number..?\n"))
    if operand == "+":
        res = n1+n2
    elif operand=="-":
        res=n1-n2
    elif operand=="*":
        res=n1*n2
    elif operand=="/":
        res=n1/n2
    return str(n1) + " " + operand +" "+ str(n2) + " = " + str(res)    

isContinue = False
while not isContinue:
    print(calculate())
    res = input("Run another calculation ? y/n\n")
    if res=="n":
        isContinue=True
    else:
        clear()