# #This is the file for the introduction to pandas

# import os

# working_directory = os.getcwd()
# print (f'I am currently on this folder: {working_directory}')

# # Making a new directory
# new_directory = 'new_dir2'
# os.makedirs(new_directory)
# print(f'The directory {new_directory} has been created successfully. \nThank you.')

# # Listing the content of a directory

# dcontent = os.listdir(working_directory)
# print(dcontent)

# # Changing the current working directory is done using the chdir() method.
# new_directory = r'            '
# print(f'The working directory has been changed succcessfully.')

# Working on files through Python
# file_object = open(filename, mode, encoding)
# Mode refers to how you want to interact with a file
# Encoding isn't always added. But we usually use UTF-8

# file_object = open("data.txt", mode="r", encoding="utf-8")
# Different modes
# w = write
# r = read
# a = append
# r+ = read and write
# w+ = write and append
# Opening a file in write mode will erase the contents of the file

file = open("data.txt", "w")
with open("data.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Day 1: Handling files; no PDF ;)\n")
    
    lines = ["Python File Handling\n", "Day 1: Handling files; no PDF ;)\n", "Writing to a file\n"]
    file.writelines(lines)
    
# Reading  afile
with open("data.txt", "r") as file:
    content = file.readlines() # Reads the entire file
    print(content[0]) #
    # while file.readlines read the file line by line
    # you can read lines and allso indexing to read specific lines
    # with open(file.readlines[0]) as file: # Reads the first line
    # for line in file:
    #     # Process one line at a time
    #     print(line) # This is lighter than readlines
    
import csv 
with open("users.csv", "w") as file:
    data = [
        ["user_id", "name", "age", "city"],
        [1, "Favour", 25, "Port Harcourt"],
        [2, "Anonymous", 23, "Somewhere"],
        [3, "Anybody", 29, "Aba"],
    ]
    with open("users.csv", "w", newline = " "):
        writer = csv.writer(file)
        writer.writerows(data)
        print("CSV created successfully!")
        
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        
        header = next(reader)
        print(f"Columns: {header}")

    for row in reader:
        user_id = row[0]
        name = row[1]
        age = row[2]
        city = row[3]
        print(f"User ID: {user_id}, Name: {name}, Age: {age}, City: {city}")
        

import pandas as pd
