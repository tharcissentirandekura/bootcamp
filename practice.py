""""
Things to use : loops, if, useinput, 
1. ask a user to enter how many times to get asked to enter his name 
2. The check if the second input is eual to the third input
3. print a message of what it is : equal or not
"""
userInput=int(input('Enter the number of times you want to print your name'))
currentName = ""
for i in range(userInput):
    name = input("Enter the name")
    currentName = name
    
     