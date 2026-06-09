users = {
    'obi':'1234',
    'ada':'5678',
    'gospel': '0987',
    'timothy': '1457'
}

username = input("What is your username?: ")
password = input("Enter your password: ")

for key, value in users.items():
    if username == key and password == value:
        print("Login Successful")
        break
else:
    print("Invalid username and password")