# The anatomy of a function (parts of a function)
#
# def        → keyword telling Python you're defining a function
# name       → meaningful identifier (use snake_case: get_user_by_id)
# parameters → inputs the fucntion needs in parantheses
# body       → the indented block of code that runs when called
# return     → sends a result back to whoever called a function

# def greet_user(name):
#     message = f"Welcome to the platform, {name}!"
#     return message ## This won't return anything on the terminal, 


# # Calling the function — provide an argument
# result = greet_user("Ada")
# print(result)


def greet_user(name):
    message = f"Welcome to the platform, {name}!"
    # return message ## This won't return anything on the terminal, 
    print(message)