import datetime

date = datetime.datetime.now()
hour = int(date.strftime("%H"))

message = "Good"
name = input("What's your name?: ").strip().capitalize()

if hour < 12:
    message += " Morning."
elif hour < 16:
    message += " Afternoon."
elif hour < 18:
    message += " Evening."
else:
    message += " Night."
    
print (f"Hello, {name}, {message}")