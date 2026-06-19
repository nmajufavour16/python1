# Using the args parameter the argument takes as much inputs as possible
# But without the args the function throws a error when called
def addition(*args):
    result = sum(args)
    return result

print(addition(344345, 3637378))
print(addition(3, 7, 9))

# Looping through a function 
def greeting(*names):
    for name in names:
        message = f"Hello {name}"
        print(message)
        
greeting("favour", "uche", "nmaju")

# Returning a function using key and value pairs
# **kwargs is used to returna  function as a dictionary using keywords
def build_profile(**kwargs):
    """Build a user profile from any number of fields"""
    profile = {}
    for key, values in kwargs.items():
        profile[key] = values
        print(f"{key} = {values}") # This prints the key and items in the dictionary on a new line for each of them
    return profile
    
user = build_profile(name= "gospel", age=25, city="aba", role="senior dev")
print(user)

def name_age(**kwargs):
    user_id = {}
    for key, values in kwargs.items():
        user_id[key] = values
    return user_id

userid = name_age(name= "Phayvo", age = 25)
print(userid)

print(build_profile.__doc__)