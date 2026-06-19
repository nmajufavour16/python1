# The block of code inside a function must be indented.
# A function can return data, or perform a task.

def bia():
    message = f"come here!!"
    return message
# print(bia())

# def birthday():
#     age = +1
#     return age

def add(a, b):
    return a + b
result = add(a, b)
print(result)

def greeting(name = "user"):
    print(f"Hello {name}")
greeting()

# Positional Arguments structure
def greeting(name, age, status):
    print(f"My name is {name}, and i'm {age} years old, and i'm {status}.")
# greeting(25, "Favour")

# Keyword Arguments fuctions
# greeting(age = 25, name = "Favour")
greeting("Favour", age=25, status="Single")

# Always note that Positional Arguments comes first before Keyword Arguments

# You can pass a list through a function, defining the function under the list
names = ["favour", "uche", "phayvo"]
items = ["phone", "charger", "laptop"]
def print_names(names):
    for name in names:
        print(name)
print_names(names + items)