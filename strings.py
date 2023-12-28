# string methods in python. What can we do with strings or what operations can we carry on it
# string is a sequence of characters and that is why it accepts this tyoes of operations

# how to check the length of the string

# firstname = "burundibwiza is here"
# print(len(firstname))

# count how many a thing appeared 

# print(firstname.count('is'))
# # find position

# print(firstname.index("is"))
# print("Positions :",firstname[1]) # indexing or acccessing items of a string.
# age = 20
# print(str(age).count('2'))

# #slicing
# print(firstname[0:7])
# # firstname[staring : stoping -1]

# # reverse
# print("reverse :",firstname[::-1]) # firstname[start:step:stop]

name = "burundi"

reverseword = ""
stop = len(name)

# while  stop >= 1:
#     stop = stop - 1
#     reverseword = reverseword + name[stop]

for i in range(stop): # this gives from 0 to 6
    index = stop - i
    reverseword = reverseword + name[index-1]
print(reverseword)

