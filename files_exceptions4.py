# STORING DATA
# Using json.dump() and json.load()
import json

numbers = [2, 3, 5, 7, 11, 13, 17]
filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    num = json.load(f)

print(num)

# Saving and Reading User-Generated Data
username = input("What is your name? ")
filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!\n")


with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!\n")


try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename) as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")


# Refactoring
print('----------REFACTORING--------------')
"""Often, you’ll come to a point where your code will work, but you’ll 
recognize that you could improve the code by breaking it up into a series
of functions that have specific jobs. This process is called refactoring. 
Refactoring makes your code cleaner, easier to understand, and easier to 
extend."""

"""Here for convenience we'll use 'name' for what was 'username' and 
 'file' for 'filename' in previous cases."""
print('1')


def greet_user():
    """Greet the user by name."""
    file = 'username.json'
    try:
        with open(file) as f:
            name = json.load(f)
    except FileNotFoundError:
        name = input("What is your name? ")
        with open(file, 'w') as f:
            json.dump(name, f)
            print(f"We'll remember when you come back!")
    else:
        print(f"Welcome back, {name}!")


greet_user()
print('2')


def get_stored_username():
    """Get stored username if available!"""
    file = 'username.json'
    try:
        with open(file) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name


def greet_user():
    """Greet user by the name."""
    name = get_stored_username()
    if name:
        print(f"Welcome back, {name}!")
    else:
        name = input("What is your name? ")
        file = 'username.json'
        with open(file, 'w') as f:
            json.dump(name, f)
            print(f"We'll remember your name when you come back, {name}!")


greet_user()
print('3')


def get_stored_username():
    """Get stored username if available!"""
    file = 'text_files/username.json'
    try:
        with open(file) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name


def get_new_username():
    """Prompt for a new username."""
    name = input("What is your name? ")
    file = 'text_files/username.json'
    with open(file, 'w') as f:
        json.dump(name, f)
        return name


def greet_user():
    """Get the user by name."""
    name = get_stored_username()
    if name:
        print(f"Welcome back, {name}!")
    else:
        name = get_new_username()
        print(f"We'll remember you when you come back, {name}!")


greet_user()
