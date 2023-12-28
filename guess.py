import random


repetion_num = int(input("How many trials: "))
for i in range(repetion_num):
    userchoice = int(input("guess a number: "))
    if userchoice == random.randint(0,repetion_num):
        print("you won")
        break
    else:
        print("Lose")
    




