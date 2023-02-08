# READING FROM A FILE
# Reading an Entire File
with open('pi_files1.txt') as file_object:
    contents = file_object.read()
print(contents)
# print(contents.rstrip())

"""The open() function needs one argument: the name of the file 
you want to open.
Similarly, there is close() function, but it functions improperly
at times.
Hence, 'with' is used. When 'with' is used python closes the file 
on its own at appropriate time."""

# File Paths
with open('text_files/sunrise.txt') as sunrise:
    lines = sunrise.read()
print(f"\n{lines}")

"""A relative file path tells python to look for a given location relative
to the directory where the currently running program file is stored.
You can tell python exactly where the file is on your computer regardless
 of where the program that's being executed is stored. This path is 
  absolute file path. """


# Reading Line by Line
filename = 'text_files/sunrise.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
        # print(line.rstrip())


# Making a List of Lines from a File
filename = 'pi_files1.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print('\n')

# Working with a  File's Contents
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
print('\n')


pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print('\n')

# Large Files: One Million Digits
filename = 'text_files/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string_million = ''
for line in lines:
    pi_string_million += line.strip()

print(f"{pi_string_million[:52]}...")
print(len(pi_string_million))
print('\n')

# Is Your Birthday Contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string_million:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
print('\n')

# DO IT YOURSELF
# 1:Learning Python
print('READING THE ENTIRE FILE')
filename = 'text_files/learning_python.txt'
with open(filename) as file:
    content = file.read()

print(content)
print(f"\n{content}\n")


print('LOOPING OVER THE FILE OBJECT')
with open(filename) as file:
    for line in file:
        print(line.rstrip())
print('\n')


print('STORING LINES IN A LIST AND WORKING WITH THEM OUTSIDE THE WITH BLOCK')
with open(filename) as file:
    book = file.readlines()

learning = ''
for page in book:
    learning += page.lstrip()

print(f"{learning}\n")

# 2:LEARNING C
with open(filename) as file:
    book = file.readlines()

learning_c = ''
for line in book:
    a = line.replace('Python', 'C')
    learning_c += a 

print(learning_c)