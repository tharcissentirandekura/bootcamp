""""
Things to use : loops, if, useinput, 
1. ask a user to enter how many times to get asked to enter his name 
2. The check if the second input is eual to the third input
3. print a message of what it is : equal or not
"""
userInput=int(input('Trial Number: '))

lastName = ""
secondLastName = ""

for i in range(1,userInput + 1):
    name = input("Name: ")
    lastName = name
    if i == userInput - 1:
        secondLastName = name

if secondLastName == lastName:
    print("Names are the same")
else:
    print("Names are different")

    
     