# Create a variable (username & password)
# Check if username = username and password = password
# If login details match, print login succesful, else print login failed.

import getpass
import stdiomask

username = input("Create your username: ").lower()
password = stdiomask.getpass("Create your password: ")

while True:
    username_auth = input("Enter your username: ").lower()
    password_auth = stdiomask.getpass("Enter your password: ")

    if username_auth == username and password_auth == password:
        print(f"Welcome, {username}, login successful!")
        break
    else:
        print(f"Sorry, login failed! Check your details and try again.")