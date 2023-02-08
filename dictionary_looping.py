# LOOPING THROUGH A DICTIONARY
# Looping Through All Key-Value Pairs
fav_subjects = {
	'alex': 'maths',
	'jason':'c++',
	'ganesh':'java',
	'virat':'python',
	'zak':'geography',
	'steve':'python',
    }
print('Favourite subjects for each student is as follows :')
for name, subject in fav_subjects.items() :
	print(f'\nName : {name.title()}')
	print(f'Subject : {subject.title()}')
	#print('\nName :', name.title())
	#print('Subject :', subject.title())
print('\n')
for name, subject in fav_subjects.items() :
	print(f"{name.title()}'s favourite subject is {subject.title()}.")
print('\n')

# Looping Through All the Keys in a Dictionary 
print('The list of students who submitted the poll is :')
for name in fav_subjects.keys() : # the keys() method here is used to ask the python only for keys, not using it is also fine 	
	print(name.title())
print('\n')

friends = ['steve','monty','micheal','virat','rohit','david']
for name in fav_subjects :
	print(f'Hi, {name.title()}.')
	if name in friends :
		subject = fav_subjects[name].title()
		print(f'{name.title()}, I see you love {subject}.')
print('\n')

for name in friends :
	if name not in fav_subjects.keys() :
		print(f'{name.title()}, please submit your poll.')
print('\n')

# Looping Through a Dictionary's Keys in a Particular Order 
for name in sorted(fav_subjects) :
	print(f'{name.title()}, thank you for taking the poll.')
print('\n')

# Looping Through All Values in a Dictionary 
print('The following subjects are mentioned by students :')
for subject in fav_subjects.values() :
	print(subject.title())
# here the subject 'Python' is repeated twice, to avoid these we use set()
print('\n')
print('The following subjects are mentioned by students :')
for subject in set(fav_subjects.values()) : 
	print(subject.title())
print('\n')

# Do it Yourself 
# 1: Glossary 2 
glossary = {
    'print()':'print() : displays whatever asked in its parentheses on the screen',
	'sum()':'sum() : provides with the sum of entities present in the said list',
	'max()':'max() : provides with the greatest number present in the said list',
	'upper()':'upper() : makes the asked word capitalize',
	}
for value in glossary.values() :
	print(value)
print('\n')
glossary['lower()'] = 'lower() : makes the asked word in lower case'
glossary['title()'] = 'title() : makes the first letter of an asked word capital'
glossary['remove()'] = 'remove() : removes the asked word permanently from the list'
glossary['count()'] = 'count() : returns the number of elements'
glossary['index()'] = 'index() : returns the index of asked element'
print(glossary)
print('\n')
for uses in glossary.values() :
	print(uses)
print('\n')

# 2: Rivers 
rivers = {
'ganga':'india', 
'indus':'pakistan',
'nile':'egypt',
'amazon':'usa',
'thames':'england',
'murray':'australia',
'brahmaputra':'bangladesh',
'mahaveli ganga':'sri lanka',
}
for river, country in rivers.items() :
	if country == 'usa' :
		print(f'The {river.title()} runs through {country.upper()}.')
	else :
		print(f'The {river.title()} runs through {country.title()}.')
print('\n')
print('The rivers included in the list are :')
for river in rivers.keys() :
	print(river.title())
print('\n')
print('The major rivers of the following countries are mentioned :')
for country in rivers.values() :
	print(country.title())
print('\n')

# 3: Polling 
fav_subjects = {
	'alex': 'maths',
	'jason':'c++',
	'ganesh':'java',
	'virat':'python',
	'zak':'geography',
	'steve':'python',
    }
take_poll = ['shree','jhye','kane','steve','joe','virat','ollie','mark','david']
for name in take_poll :
	if name in fav_subjects : # or fav_subjects.keys() 
		print(f'\tThank you for taking the poll {name.title()}.')
	else :
		print(f'Please submit your poll, {name.title()}.')
