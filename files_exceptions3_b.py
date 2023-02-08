# DO IT YOURSELF
# 1:Addition
print(4 + 5)
"""print(5 + int('y'))"""

# 2:Addition Calculator
print("\nGimme two numbers and I'll add them.")
print("Enter 'q' to quit.\n")
while True:
    first_number = input("First number: ")
    if first_number == 'q':
        print('\n')
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        print('\n')
        break
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Uh, uh letters and words can't be added!\n")
    else:
        print(result, '\n')


# 3:Cats and Dogs
def open_file(filename):
    """Read the contents in the file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Pratik, kindly check the existence of the file {filename}.")
    else:
        print(contents, '\n')


animals = ['text_files/cats.txt', 'text_files/dogs.txt']
for animal in animals:
    open_file(animal)


# 4:Silent Cats and Dogs
print('\n')


def open_file(filename):
    """Read the contents in the file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents, '\n')


animals = ['text_files/cats.txt', 'text_files/dogs.txt']
for animal in animals:
    open_file(animal)


# 4:Common Words
def count_words(filename, word='the '):
    """Count the no. of times a word repeats itself in the book."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Please check {filename}'s root directory.")
    else:
        no_of_words = contents.lower().count(word)
        print(f"The file {filename} contains word '{word}', "
              f"{no_of_words} times.")


alice_book = 'text_files/alice.txt'
count_words(alice_book, 'alice')
count_words(alice_book)
print('\n')

books_words = {
    'text_files/alice.txt': 'alice',
    'text_files/Moby Dick.txt': 'moby',
    'text_files/Siddhatha.txt': 'siddhartha',
    'text_files/Little Women.txt': 'women',
    }

for books, words in books_words.items():
    count_words(books, words)
print('\n')

for books in books_words:
    count_words(books)
