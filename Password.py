



import random
import string
from os import system


lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "~@#$%^&*()_+=-\|]{}?/"
numbers = "0123456789"

all = lower + upper + symbols + numbers

system('cls')
while True :
    print("1) Create Password\n2) Exits")
    menu = input("Enter your Choice : ")
    system('cls')

    if menu == "1" :
        length = int(input("Enter the Length of Password : "))
        password = "".join(random.sample(all, length))
        system('cls')
        print(password)

    elif menu == "2" :
        print("Exits ...")
        break

    else :
        print("Wrong Choice!!!")

