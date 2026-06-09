"""
1. Take Num1 and Num2
2. Take an input asking the user what operation to carry out
3. Check if selected operation exists and carry out arithemtic operation
"""

print("Calculate Anything!")

num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second Number: "))

print("Select an option below: \nA)> Addition\nB). Subtraction\nC). Division \nD). Multiplication")
option = input("==> ").upper()

if option == "A":
    print(f"The Sum of {num1} and {num2} is {num1 + num2}")
elif option == "B":
    print(f"The Difference of {num1} and {num2} is {num1 - num2}")
elif option == "C":
    print(f"The Quotient of {num1} and {num2} is {num1 / num2}")
elif option == "D":
    print(f"The Product of {num1} and {num2} is {num1 * num2}")
else:
    print(f"Invalid Option {option}")