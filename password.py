import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = upper_case.lower()
digits = "0123456789"
symbols = "!@#$%^&*"

inp1 = input("Do you want an upper case in your password? (y/n)")
inp2 = input("Do you want lower case in your password? (y/n)")
inp3 = input("Do you want numbers in your passwrod? (y/n)")
inp4 = input("Do you want symbols in your password? (y/n)")

all = " "

if inp1 == "y":
    all += upper_case
if inp2 == "y":
    all+= lower_case
if inp3 == "y":
    all += digits
if inp4 == "y":
    all+= symbols

length = int(input("Length of password: "))
amount = int(input("Number of passwords you want: "))

for i in range(amount):
    password = "".join(random.sample(all,length))
    print(password)
