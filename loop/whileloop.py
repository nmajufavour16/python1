# while <condition>:
    # this block runs repeatedly as long as condition is True
    # CRITICAL: Something in this block has to make the condition false or the loop will run forever.
    
# count = 0
# while count <= 4:
#     print("I'm hungry.")
#     count += 1


# # count in while loops ensures the loop stops after satisfying an indicated number of cycles
# command = [""]
# while command != "exit":
#     command = input("what's your command?: ")
#     print(f"user: {command}")
# else:
#     print("goodbye user")
    
# using break statements
count = 1
ages = []
while count <= 5:
    user_age = input("How old are you?: ").strip()
    if user_age.isdigit():
        ages.append(user_age)
        count += 1
    else:
        print("Write your age in figures!")
    break
print(ages)
for age in ages:
    print(f"I am {age} years old.")
    

count = 1
ages = []
while count <= 5:
    user_age = input("How old are you?: ").strip()
    if user_age.isdigit():
        ages.append(user_age)
        count += 1
    else:
        print("Write your age in figures!")
    pass
print(ages)
for age in ages:
    print(f"I am {age} years old.")
