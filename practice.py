""""
Jerome Bizimana
Things to use : loops, if, useinput
1. ask a user to enter how many times to get asked to enter his name 
2. The check if the second input is eual to the third input
3. print a message of what it is : equal or not
"""
userInput = int(input('Trial Number: '))

# lastName = ""
# secondLastName = ""

# for i in range(1,userInput + 1):
#     name = input("Name: ")
#     lastName = name
#     if i == userInput - 1:
#         secondLastName = name

# if secondLastName == lastName:
#     print("Names are the same")
# else:
#     print("Names are different")

names = []

for i in range(userInput):
    name = input("Name: ")
    names.append(name)
    for name in names:
        if name[userInput-1] == name[userInput]:
            print('Names are same')
        else:
            print('Names are different')

#to access an element in list, we use indexes
#elements in lists are ordered
"""
which means each element has its positions from 0 to n-1
name = [1,2,3,4,5]
ex: to get the nth element we do , name[n-1]
we can also use slicing, 3rd element : name[3-1:3]
"""

#for i in range(0,userInput + 5,5):
    #print(i)
"""
general ways :
for i in range(start,stop,step)
"""
     