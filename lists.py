"""
- Lists are data types in pyton
- They are mutable( they can be changed after being created.)
- Elements are ordered


>Operations over lists:

- add elements : listname.append(element)
- remove elements: listname.remove(element)
- modify elements : listname[Elementposition] = new element

- index : to find the position of an element; lisname.index(element)

code example of index finding :

userinput = input("Your name : ")

names = ["Jerome","Tharcisse","Niyonkuru"]
print(userinput," at position ", names.index(userinput))
"""

#how to iterate through lists

"""
"""
# find all even numbers in the lists
# find all odd numbers in the lists
# find all prime numbers in the lists

numbers = [1,2,6,3,4,7,9]

#finding the even numbers and odd numbers
#1.for loop
#example

even_numbers = []
odd_numbers = []

"""
for number in numbers:
    if number % 2 ==0:
        even_numbers.append(number)
    elif number % 2 == 1:
        odd_numbers.append(number)
print("Even numbers :", even_numbers)
print("Odd numbers :", odd_numbers)
"""

#with while loop
"""
n = len(numbers) - 1 
i = -1
while i < n:
    i += 1 # i = i + 1
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    elif numbers[i] % 2 == 1:
        odd_numbers.append(numbers[i])
print("Even numbers:", even_numbers)
print("Odd numbers :", odd_numbers)

"""

# find prime numbers with for loop

primes = []

# primes numbers has divisor of 1 and itself.
# first it to find those divisors and store them
# check if there is one with exactly two divisors.
"""
for number in numbers:
    divisors = []
    # divisors = [div for div in range(1,number + 1) if number % div == 0] # list comprehension
    for div in range(1,number+1):
        if number % div == 0:
            divisors.append(div)
    if len(divisors) == 2:
        primes.append(number)
print("Prime numbers: ",primes)

"""

# prime number with while loop
"""
length = len(numbers)# length = 5 # finding the length of the list.
i = -1 # starting position
while i < length - 1: # loop condition: length is : 4; -1 < 4 which is True
    i = i + 1 # incrementation of one at each iteration : i now is : 0
     # print the element at that position: numbers[0] which is 1
    divisors = [div for div in range(1,numbers[i] + 1) if numbers[i] % div == 0]
    # print(numbers[i],divisors)
    if len(divisors) == 2:
        primes.append(numbers[i])

print("Prime numbers :",primes)

"""

# how to find the size of the list
data = [1,2,3,[1,3,"name"],{"name":"Tharcisse"}]

    


