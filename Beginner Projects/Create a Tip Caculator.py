#Project_2
#Creat a Tip Caculator

print("Welcom to the Tip Caculator")
bill = float(input("Enter the bills..? $"))
perc = int(input("Enter percentges bills..? 10, 12 or 15?"))
n=int(input("How Many people..?"))
tot_bill = (bill*(perc/100))
res = bill + tot_bill;
res=round(res/n,2);
print("Each person bill is: " + str(res)) 
