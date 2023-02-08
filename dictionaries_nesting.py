# NESTING
# A List of Dictionaries 
hen = {'age': 12, 'group': 'small'}
goat = {'age': 24, 'group': 'medium'}
cow = {'age': 32, 'group': 'adult'}
my_farm = [hen, goat, cow]
print(my_farm)
for animals in my_farm:
    print(animals)
print('\n')

# Make an empty list for storing new hens details
my_farm = []
# Add 30 new hens details 
for hen_number in range(30):
    new_hen = {'age': 15, 'group': 'medium'}
    my_farm.append(new_hen)
# Show first 5 hens details  
for hen in my_farm[:5]:
    print(hen)
print('......')
# Show the number of new hens purchased 
print(f'The number of new hens purchased is : {len(my_farm)}.')
# but later you changed mind, and took 3 large grouped hens, update
for hen in my_farm[:3]:
    if hen['group'] == 'medium':
        hen['age'] = 26
        hen['group'] = 'large'
for hen in my_farm[:6]:
    print(hen)
print('......\n')

# A List in a Dictionary 
fav_subjects = {
    'alex': ['maths'],
    'jason': ['c++'],
    'ganesh': ['java', 'javascript'],
    'virat': ['python'],
    'zak': ['geography'],
    'steve': ['python'],
    'jhye': ['r', 'maths'],
    'pratik': ['sql', 'history'],
    'chris': ['oracle', 'c#'],
    'glenn': ['python', 'aws'],
}

for students, subjects in fav_subjects.items():
    if len(subjects) == 1:
        print(f'\nThe favourite subject of {students.title()} is : {subjects[0].title()}.')
    else:
        print(f'\nThe favourite subject of {students.title()} is :')
        for subject in subjects:
            if subject == 'sql' or subject == 'aws':  # you can use 'or' in such instances
                print(f'\t{subject.upper()}')
            else:  # if not understanding close these corresponding if,else
                print(f'\t{subject.title()}')

#  A Dictionary in a Dictionary
users = {'pmohite': {'first': 'pratik', 'last': 'mohite', 'location': 'pune'},
         'sgill': {'first': 'shubhman', 'last': 'gill', 'location': 'jalandar'},
         'klr': {'first': 'lokesh', 'last': 'rahul', 'location': 'bangalore'}
         }
for username, user_info in users.items():
    print(f"\nUsername : {username}")
    name = f"{user_info['first']} {user_info['last']}"
    print(f'\tFullname :{name.title()}')
    print(f"\tLocation :{user_info['location'].title()}")
print('\n..................')

# Do It Yourself 
# 1: People 
myself = {'first_name': 'Pratik', 'last_name': 'Mohite', 'age': 19, 'city': 'Pune'}
friend1 = {'first_name': 'Virat', 'last_name': 'Kolhi', 'age': 32, 'city': 'Delhi'}
friend2 = {'first_name': 'Rohit', 'last_name': 'Sharma', 'age': 33, 'city': 'Mumbai'}
people = [myself, friend1, friend2]
for person in people:
    fullname = f"{person['first_name']} {person['last_name']}"
    print(f'\nFullname : {fullname.title()}')
    print(f"\tAge : {person['age']}")
    print(f"\tCity : {person['city'].title()}")
print('\n.............................')

# 2: Pets 

# 3: Favourite Places
favourite_places = {
    'lewis': ['london', 'san fransisco'],
    'gordon': ['paris'],
    'riley': ['mussorie', 'dubai', 'new york'],
}
for names, places in favourite_places.items():
    if len(places) == 1:
        print(f'''\nThe favourite place to visit of {names.title()} is : {places[0].title()}''')
    else:
        print(f'\nThe favourite places to visit of {names.title()} is :')
        for place in places:
            print(f'\t{place.title()}')
print('\n...................................')

# 4: Favourite Numbers
fav_numbers = {
    'karan': [14, 45],
    'kshitij': [52, 99, 12],
    'ashok': [98],
    'sarang': [74, 68, 99],
    'shubham': [27],
}
for student, number in fav_numbers.items():
    if len(number) == 1:
        print(f"\nThe favourite number of {student.title()} is : {number[0]}")
    else:
        print(f"\nThe favourite number of {student.title()} is :")
        for num in number:
            print(f"\t{num}")
print('\n....................................')

# 5: Cities
cities = {
    'mumbai': {'country': 'india', 'population': 20, 'fact': 'Busiest city in the world.'},
    'new york': {'country': 'america', 'population': 80, 'fact': 'More than 800 languages are spoken.'},
    'colombo': {'country': 'sri lanka', 'population': 5.6, 'fact': 'Largest city in Sri Lanka'},
}
for city, info in cities.items():
    print(f'\n{city.upper()}')
    print(f"\tCountry : {info['country'].title()}")
    print(f"\tPopulation : {info['population']} million")
    print(f"\tFact : {info['fact']}")
print('\n...........................')

# 6: Extensions/
