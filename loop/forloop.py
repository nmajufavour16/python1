# for <variable> in <collection>
    # This block runs once for eah item in the collection
    # <variable> holds the current item on each iteration

# Scores = [70, 30, 50, 45, 60]
# for score in Scores:
#     if score >= 70 and <= 100:
#         print(f"your score is: {score}")
#     elif score 
    
Names = ["Favour", "Uche", "Nmaju"]
for name in Names:
    print(f"Good morning, {name}")
    
dbconfig = {
    "host": "db.techrise.ng",
    "port": 5432,
    "name": "analytics.db",
    "max_connections": 50
}

for key, values in dbconfig.items():
    print(f"{key}: {values}")
    

dbconfig = {
    "host": ["db.techrise.ng", "techrise.ng"],
    "port": [5432, 5645],
    "name": ["analytics.db", "backend.techrise.ng"],
    "max_connections": [50, 15]
}

# Nested for loops, for looping over a loop statement
for key, values in dbconfig.items():
    for value in values:
        print(value)
       
       # This prints the values in a list while looping through the value items in the dictionary  
        print(values)
        