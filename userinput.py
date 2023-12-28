# getting the input from the user.
# a simple calculator

number1 = int(input("First number :"))
operand = input("Operand :")
number2 = int(input("Second number :"))


if operand == "+":
    print(number1," + " ,number2, " = ", number1 + number2)

elif operand == "-":
    print(number1," - " ,number2, " = ", number1 - number2)
elif operand == "*":
    print(number1," * " ,number2, " = ", number1 * number2)

elif operand == "/":
    try:
        print(number1," / " ,number2, " = ", number1 / number2)
    except:
        print("No division by zero")
else:
    print("No such operand ")

