# EXCEPTIONS
# Handling the ZeroDivisionError Exception
"""print(5/0)"""

#   Using try-except Blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!\n")

#    Using Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number)/int(second_number)
    print(answer)

#    The else Block
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# Handling the FileNotFound Exception
print('\n')
filename = 'alice.txt'
"""with open(filename) as f:
    contents = f.read()"""

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the {filename} does not exist.\n")


# Analyzing Text
title = "Alice in Wonderland"
print(title.split(), '\n')

filename = 'text_files/alice.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the {filename} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has {num_words} words.\n")


# Working with Multiple Files
def count_words(filename):
    """Count the appropriate no. of words in the file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words.")


filename = 'text_files/alice.txt'
count_words(filename)
print('\n')

book_file = ['text_files/Moby Dick.txt', 'text_files/Siddhartha.txt',
             'text_files/Little Women.txt']

for file in book_file:
    count_words(file)
print('\n')


# Failing Silently - stop the traceback
def count_words(filename):
    """Count the appropriate no. of words in a file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words.")


book_file = ['text_files/Moby Dick.txt', 'text_files/Siddhartha.txt',
             'text_files/Little Women.txt', 'text_files/alice.txt']

for file in book_file:
    count_words(file)


# Deciding Which Errors to Report
"""How do you know when to report an error to your users and when to fail 
silently? If users know which texts are supposed to be analyzed, they might 
appreciate a message informing them why some texts were not analyzed. If 
users expect to see some results but don’t know which books are supposed 
to be analyzed, they might not need to know that some texts were unavail-
able. Giving users information they aren't looking for can decrease the 
usability of your program. Python’s error-handling structures give you fine-
grained control over how much to share with users when things go wrong; 
it’s up to you to decide how much information to share.
Well-written, properly tested code is not very prone to internal errors, 
such as syntax or logical errors. But every time your program depends on 
something external, such as user input, the existence of a file, or the avai-
lability of a network connection, there is a possibility of an exception
being raised. A little experience will help you know where to include
exception handling blocks in your program and how much to report to users 
about errors that arise."""