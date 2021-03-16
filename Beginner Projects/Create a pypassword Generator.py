#Project_5
#Create a pypassword Generator

import random

l = int(input("How Many no of length in your password..?"))
s = int(input("How Many no of symblos in your password..?"))
n = int(input("How Many no of numbers in your password..?"))

l = l - (s+n)

#characters list
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#symbols list
symbols = ["@","#","$","%","^","|","&","*","(",")"]

#number list
number = ["0","1","2","3","4","5","6","7","8","9"]

password = ""
for i in range(0,s):
    password += symbols[random.randint(0,s)]
for i in range(0,n):
    password += number[random.randint(0,n)]
for i in range(0,l):
    password += chars[random.randint(0,l)]

print(password)
