# A Simple Example 
computer_languages = ['python','c++','java','c','ruby','oracle']
print('The popular computer languages are :')
for language in computer_languages:
	if language == 'java' :
		print(language.upper())
	else :
		print(language.title())	
print('\n')

# CONDITIONAL TESTS 
# Checking For Equality
boy = 'Harry'
print(boy == 'Harry')
print(boy == 'Garry')
print(boy == 'harry')
print(boy.lower() == 'harry') # since, testing for equality is case sensitive in python 

# Checking For Inequality
girl = 'cindrella'
if girl != 'diana' :
	print('Diana not found.')

# Numerical Comparisons
family_members = 5 
print(family_members == 6)

if family_members != 7 :
	print("It's a balanced family.")	

print(family_members < 7)
print(family_members > 7)
print(family_members <= 5)
print(family_members >= 6)
print('\n')

# CHECKING MULTIPLE CONDITIONS 
# Using and to Check Multiple Conditions 
chintu = 24
pintu = 18 
print(chintu >= 12 and pintu <= 24) # here the true, false logic comes into picture 
print(chintu <= 26 and pintu > 32)

# Using or to Check Multiple Conditions 
print(chintu < 30 or pintu > 10)
print(chintu >= 15 or pintu < 12)
print(chintu > 32 or pintu > 20)
# For 'and' if any one condition is False overall condition is False
# For 'or' if any one condition is True overall condition is True
print('\n') 

# Checking Whether a Value Is in a List 
films = ['war','thor','baaghi','heropanti','master','tiger']
print('thor' in films)
print('krrish' in films)

# Checking Whether a Value Is not in a List 
print('thor' not in films)
print('krrish' not in films)
fav_film = 'batman'
if fav_film not in films : 
	print(f"You can't watch {fav_film.title()} now.")

# Boolean Expressions 
good_boy = True
filthy = False
print("\n")

# if STATEMENTS
marks = 45 
if marks >= 35 :
	print("Congratulations! You have passed the exam.")
	print("Onto the next sem now.")

# if-else Statements 
marks = 32
if marks >= 35 :
	print("Congratulations! You have passed the exam.")
else :
	print("Ahh, ahh! You need to repeat the exam.")
print('\n')

# if-elif-else Chain
size = 50
if size <= 38 :
	print("Your shirt size is 'S'")
elif size <= 44 :
	print("Your shirt size is 'M'")
else :
	print("Your shirt size is 'L','XL','XXL'")

if size <= 38 :
	shirt_size = 'S'
elif size <= 44 : 
	shirt_size = 'M'
else : 
	shirt_size = "'L','XL' or 'XXL'"
print(f"The size of your shirt is {shirt_size}.")

# Using Multiple elif Blocks 
size = 56 
if size < 38 :
	shirt_size = 'S'
elif size < 44 :
	shirt_size = 'M'
elif size < 50 : 
	shirt_size = 'L'
elif size < 56 :
	shirt_size = 'XL'
elif size < 60 :
	shirt_size = 'XXL'
print(f"The size of your shirt is {shirt_size}.")

# Omitting the else Block  
#python does not require an else block at the end of an if-elif chain.
#sometimes an else block is useful ; sometimes its clearer to use an 
#additional elif statement that catches the specific condition of interest.)

# Testing Multiple Conditions 
print('\n')
favourite_fruits = ['banana','apple','strawberries']
if 'banana' in favourite_fruits :
	print('You really like bananas!')
if 'guava' in favourite_fruits :
	print('Wow, thats awesome! Guavas ha!')
if 'apple' in favourite_fruits :
	print('You love apples, too!')
if 'mango' in favourite_fruits :
	print('So you are a fan of King of Fruits, too.')
if 'strawberries' in favourite_fruits :
	print('Aww, strawberries are so sweet.Glad you like them.')
print("\n")

# USING if STATEMENTS WUTH LISTS
# Checking for Special Items 
students = ['anand','sumedh','varun','pranit','tejas','soham'] # class 6 students
for student in students : 
	print(f"{student.title()}, Present ")
print('\nFinished Attendence.')
print('\n')

for student in students :
	if student == 'sumedh':
		print(f'{student.title()}, Absent')
	else :
		print(f'{student.title()}, Present')
print(f'\nFinished Attendence')
print('\n')

# Checking That a List Is Not Empty
dance_students = []
if dance_students :
	for student in dance_students :
		print(f'Welcome to the dance class, {student.title()}.')
else :
	print('No students registered to the dance class yet.')
print('\n')

# Using Multiple Lists 
sports_students = ['shivam','varun','paresh','soham']
for student in sports_students :
	if student in students :
		print(f'Welcome to sports class, {student.title()}.')
	else :
		print(f'{student.title()} not in class 6.')
print('\n')

# Do it Yourself 
username = ['john12','joe14','ben25','admin','olly55']
for name in username :
	if name == 'admin' :
		print(f'Hello {name}, would you like to see a status report?')
	else :
		print(f'Hello {name}, thank you for logging in again.')
print('\n')
username = []
if username :
	for name in username :
		print('There are some users.')
else :
	print('We need to find some users!')
print('\n')

# checking usernames 
current_users = ['john12','stuart99','james34','shane45','glenn03']
new_users = ['stuart99','dom24','zak67','shane45','chris93']
for name in new_users :
	if name in current_users :
		print('Sorry, username already in use. Please try another.')
	else :
		print(f'Welcome {name}, we are delighted to have you on our app.')
print('\n')

# ordinal numbers 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers :
	if number == 1 :
		print(f'{number}st')
	elif number == 2 :
		print(f'{number}nd')
	elif number == 3 :
		print(f'{number}rd')
	else :
		print(f'{number}th')














