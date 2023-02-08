# RETURN VALUES
"""A function doesn't always have to display its output directly.
Instead, it can process some data and then return a value or set of values."""


# Returning a simple value


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()


cricketer = get_formatted_name('rohit', 'sharma')
print(cricketer)

# Making an Argument Optional
""" You can use default values to make an argument optional"""


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


prime_minister = get_formatted_name('narendra', 'modi', 'damodardas')
print(prime_minister)
cricketer = get_formatted_name('rohit', 'sharma', 'gurunath')
print(cricketer)
actor = get_formatted_name('tiger', 'shroff')
print(actor)
print('\n')


# Returning a Dictionary


def built_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


president = built_person('ramnath', 'kobind', age=72)
print(president)
actor = built_person('salman', 'khan')
print(actor)


# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' to exit the code.")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")

print('\n')


# DO IT YOURSELF
# 1:City Names


def city_country(city, country):
    """Return the name of city and its country."""
    c_c = f'"{city.title()}, {country.title()}"'
    return c_c


city1 = city_country('mumbai', 'india')
print(city1)
city2 = city_country('malibu', 'america')
print(city2)
city3 = city_country('santiago', 'chile')
print(city3)


# 2:Album


def make_album(artist_name, album_title, no_of_songs=None):
    """Return the artist and his album dictionary."""
    artist = {'name': artist_name, 'title': album_title }
    if no_of_songs:
        artist = {'name': artist_name, 'title': album_title, 'no_of_songs': no_of_songs}
    return artist


artist1 = make_album('dhvani', 'leja re', 4)
print('\n')
print(artist1)
artist2 = make_album('darshan', 'tera zikr')
print(artist2)
artist3 = make_album('arjit', 'phir kabhi')
print(artist3)


# 3:User Album


def make_album(artist_name, album_title, no_of_songs):
    """Return the artist and his album dictionary."""
    artist = {'name': artist_name, 'title': album_title}
    if no_of_songs:
        artist = {'name': artist_name, 'title': album_title, 'no_of_songs': no_of_songs}
    return artist


while True:
    print(f"\nGive artist's details:")
    print("Enter 'q' to exit anytime.")
    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    a_title = input("Album title: ")
    if a_title == 'q':
        break
    a_songs = input("No of songs: ")
    if a_songs == 'q':
        break
    elif a_songs == ' ':
        a_artist = make_album(a_name, a_title)
        print(a_artist)
    else:
        a_artist = make_album(a_name, a_title, a_songs)
        print(a_artist)

