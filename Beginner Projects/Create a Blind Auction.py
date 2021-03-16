#Project_9
#Create a Blind Auction 

from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

max_no = -1
max_key = ""
blind_auction = {}
bid_finish = False
while not bid_finish:
    Name = input("Enter Your Name..?\n")
    bid = input("Enter Your bid price..? \n$")     
    blind_auction[Name] = bid
    ask = input("Is there other users wanna to bid..? yes/no\n")
    if ask == "no":
        bid_finish = True
    elif ask=="yes":
        clear()    

for i in blind_auction:
    if int(blind_auction[i]) > int(max_no) :
        max_no = blind_auction[i] 
        max_key = i  

print("The Winner: " + max_key + " with " + blind_auction[max_key] + "$")


