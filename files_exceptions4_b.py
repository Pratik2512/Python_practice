# DO IT YOURSELF
# 1:Favourite Number
import json
favourite_num = input("What's your favourite number? ")
filename = 'text_files/favourite_number.json'

with open(filename, 'w') as f:
    json.dump(favourite_num, f)

with open(filename) as f:
    num = json.load(f)
    print(f"I know your favourite number! It's {num}")


# 2:Favourite Number Remembered
print('\n-------Favourite Number Remembered----------')
try:
    with open(filename) as f:
        num = json.load(f)
except FileNotFoundError:
    favourite_num = input("What is your favourite number? ")
    with open(filename, 'w') as f:
        json.dump(favourite_num, f)
        print("Thanks, I'll remember your fav number.")
else:
    print(f"I know your favourite number! It's {num}")


# 3:Verify User
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
    verify_name = input("VERIFICATION, Please enter your name: ")
    name = get_stored_username()
    if name == verify_name:
        print(f"Welcome back, {name}!")
    else:
        name = get_new_username()
        print(f"We'll remember you when you come back, {name}!")


greet_user()
