import stdiomask

username = input("Create your username: ").lower()
password = stdiomask.getpass("Create your password: ")

count = 0

while count < 3:
    username_auth = input("Enter your username: ").lower()
    
    if username_auth == username:
        break 
        
    elif username_auth != username:
        print("Incorrect username! Please try again.")
        count += 1

if count < 3:
    count = 0
    
    while count < 3:
        password_auth = stdiomask.getpass(f"Welcome, {username}, enter your password: ")
        
        if password_auth == password:
            print("Login Successful, Welcome!!")
            break

        elif password_auth != password:
            print("Sorry, login failed! Check your password and try again.")
            count += 1
            
if count == 3:
    print("Sure say na your account, ehh?")
    print("Login failed, too many failed attempts!")