# there are two types of loops: for and while

"""
1. for loops or definite loops
    - for loops has two things:
            1. when iterating in range: for loopvariable in range(n)
            2. when iterating in sequences we use: for loopvariable in sequence
                    - loop variable can be anything as any variable in python unless it is a number

2. while : Infinite loops( it runs forever until the condition is over or met)
   - it is more like an if and while can be used with else 
   - we have a condition to check to be run
   i = 10
   - while i > 0:
        print("yes")

"""

#print from o to 10
"""
1. using for loop

for i in range(11):
    print(i)

1.using while loop

i = -1
while i < 10:
    i = i + 1
    print(i)
"""
#print from 10 to 0
"""
1. for loop
for i in range(11):
    print(10 - i)

i = 11
while i > 0:
    i = i - 1
    print(i)

"""

# iterating through sequences

numbers = [1,3,2,4,6]
#1.for loop
"""
for number in numbers:
    print(number)
"""
#using while

"""
length = len(numbers)# length = 5 # finding the length of the list.
i = -1 # starting position
while i < length - 1: # loop condition: length is : 4; -1 < 4 which is True
    i = i + 1 # incrementation of one at each iteration : i now is : 0
    print(numbers[i]) # print the element at that position: numbers[0] which is 1

else:
    print(i,"Now not less")

"""