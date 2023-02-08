# WRITING TO A FILE
# Writing to an Empty File
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# Try
file = 'text_files/hobbies.txt'
with open(file, 'r') as file_object:
    # reset the file to some other text initially
    text = file_object.read()
print(text)


with open(file, 'w') as file_object:
    file_object.write("I love to draw.")


with open(file, 'r') as file_object:
    text = file_object.read()
print(f"\n{text}")


# Writing  Multiple Lines
with  open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")


with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.")


# Appending to a File
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n ")


# DO IT YOURSELF
# 1:Guest
name = input("What's your name? \n")
filename = 'text_files/guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(f"My name is {name}.")

# 2:Guest Book
filename = 'text_files/guest_book.txt'
print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"My name is {name}.\n")
        print(f"Hi {name}, you've been added to the quest-book.")

# 3:Programming Poll
filename = 'text_files/responses.txt'
with open(filename, 'w') as f:
    f.write("I like programming because:\n")

print("\nEnter 'quit' if you're finished.")
while True:
    response = input("\nWhy do you like programming? ")
    if response == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"\t{response}\n")
        print("Your response noted successfully.")



