# WORKING WITH DICTIONARIES 
india = {'capital':'new delhi','population':'1.25 billion','gdp':'2.8 trillion'}

# Accessing Values in a Dictionary 
print(india['capital'])
print(india['population'])

# Adding New Key-Value Pairs
india['area'] = '3.29 million sqkm'
india['area_rank'] = 7
print(india)
print('\n')

# Removimg Key-Value Pairs
del india['area_rank']
print(india) 
print('\n')

# Editing values 
india['population'] = '1.38 billion'
print(india)
# A Dictionary of Similar Objects 
fav_subjects = {
	'alex': 'maths',
	'jason':'c++',
	'ganesh':'java',
	'virat':'python',
	'zak':'geography',
	'steve':'python',
    }
subject = fav_subjects['zak'].title()
print("Zak's favourite subject is",subject,'.')

# Using get() to Access Values
#print(fav_subjects['axar'])
sub_axar = fav_subjects.get('axar','axar is not mentioned in the list.')
sub_alex = fav_subjects.get('alex','alex is not mentioned in the list.')
print(sub_axar)
print(sub_alex)
print('\n')

# Do it Yourself 
# 1: Person
myself = {'first_name':'Pratik', 'last_name':'Mohite', 'age':19, 'city':'Pune'}
print(myself['first_name']) 
print(myself['last_name'])
print(myself['age'])
print(myself['city'])
print('\n')

# 2: Favourite Numbers
fav_numbers = {'karan':14, 'kshitij':52, 'ashok':98, 'sarang':74, 'shubham':27}
print("Karan's favourite number is", fav_numbers['karan'])
print("Kshitij's favourite number is", fav_numbers['kshitij'])
print("Ashok's favourite number is", fav_numbers['ashok'])
print("Sarang's favourite number is", fav_numbers['sarang'])
print("Shubham's favourite number is", fav_numbers['shubham'])
print('\n')

# 3: Glossary 
glossary = {
    'print()':'print() : displays whatever asked in its parentheses on the screen',
	'sum()':'sum() : provides with the sum of entities present in the said list',
	'max()':'max() : provides with the greatest number present in the said list',
	'upper()':'upper() : makes the asked word capitalize',
	}
print(glossary['print()'])
print('\n')
print(glossary['sum()'])
print('\n')
print(glossary['max()'])
print('\n')
print(glossary['upper()'])