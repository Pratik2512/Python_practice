# LOOPING THROUGH AN ENTIRE LIST
# for loop 
cities_to_visit = ['mysore','paris','new york','london','dubai','birmingham','las vegas','tiruvanathpuram']
for city in cities_to_visit :
	print(city)
print('----------------------------------------------')	
# doing more work within a loop 
for city in cities_to_visit :
    print(f"I visited {city.title()}, and it was an amazing one.")
    print(f"Can't wait to visit you again {city.title()}.\n")
# doing something after a loop     
print("On and on, onto the next tour now.")
print('---------------------------------------------')
# keep indention in mind whenever you code
# forgetting to indent some lines 
for city in cities_to_visit :
	print(f"\nI visited {city.title()}, and it was an amazing one.")
print(f"Can't wait to visit you again {city.title()}.")	
# ^ this is an logical error. The syntax is valid, but the code does not produce desired result. 
print('-------------------------------------------------')

# NUMERICAL LISTS 
# Range function
for number in range(6) :
	print(number)
print('-----------------------------------------------')	
for number in range(2,6) :
    print(number)	
print('------------------------------------------------') 
for number in range(0,8,2) :
    print(number)  
print('-----------------------------------------------')
for value in range(1,11) :
    print(f"{value} * {value} = {value ** 2}")
# using range to make lists oof numbers
print("\n\n")
whole_numbers = list(range(7))
print(whole_numbers)
even_numbers = list(range(0,12,2)) 
print(even_numbers)
squares = []
for value in range(1,11) :
	square = value ** 2
	squares.append(square)
print(squares)

# Simple statistics with lists of numbers 
digits = [1, 12, 34, 4, 19, 23, 15, 62]
print(max(digits))
print(min(digits))
print(sum(digits))

# List Comprehensions 
squares = [ value ** 2 for value in range(1,11)]
print(squares)

# Do It Yourself
#1
for number in range(1,21) :
	print(number)
#2
million = list(range(1,1000001))
#print(million)
#3 
print(min(million))
print(max(million))
print(sum(million))	
#4
for odd_number in range(1,20,2) :
	print(odd_number)
#5
multiples_3 = [3,6,9,12,15,18,21,24,27]
for num in multiples_3 :
	print(num)
#6 
cubes = []
for value in range(1,11) :
    cubes.append(value ** 3)
print(cubes)
#7
cubes_1 = [ value ** 3 for value in range(1,11)]
print(cubes_1) 
print('\n\n')   	

# WORKING WITH PART OF A LIST 
# Slicing a list 
print(cities_to_visit[1:4]) # slices values from index 1 to index 3 
print(cities_to_visit[:5]) # slices values upto index 4
print(cities_to_visit[3:]) # slices values from index 3 to end 
print(cities_to_visit)
print(cities_to_visit[1:7:2]) # the third argument, here :2, skips the values in between 2 printed values  
print(cities_to_visit[0::2])
print(cities_to_visit[::2]) # the argument [:], is the same as [0:], prints all values in the list 
print(cities_to_visit[-3:]) # slices from index -3 to end 
print(cities_to_visit[:-3]) # slices upto index -3
print('\n ')

# Looping through a slice
print("These are my top 4 cities to visit.")
for city in cities_to_visit[0:4] :
	print(city.title())
print('\n')

# Copying a list
my_fav_books = ['rich dad poor dad','atomic habits','the alchemist','the secret']
frnds_fav_books = my_fav_books[:]  # the slicing ,i.e. [:], here is imp to tell python that both lists are not exactly the same
# frnds_fav_books = my_fav_books    ,here this means that both lists are exactly the same 
my_fav_books.append('the subtle art of not giving a fuck')
frnds_fav_books.append('you can win')
print(my_fav_books)
print(frnds_fav_books)
del(frnds_fav_books[2])

# Do It Yourself
print("\nMy favourite books are:")
for book in my_fav_books :
	print(book.title())
print("\nDhiraj's favourite books are:")
for book in frnds_fav_books :
	print(book.title())

# TUPLES
# Do It Yourself 
menu = ('shev bhaji','kaju curry','paneer tikki','tej kolhapuri','dal tadka')
# menu[3] = 'matar paneer'  # TypeError: 'tuple' object does not support item assignment
print('\nToday`s menu at "Baba Ka Dhaba" :')
for food in menu :
	print(food.title())
menu = ('shev bhaji','kaju curry','aalu sabji','veg kolhapuri','dal tadka' )
print('\nToday`s (revised) menu at "Baba Ka Dhaba" :')
for food in menu :
	print(food.title())
print('\n  ')  # for adding extra blank lines between 2 consequent code answers

# STYLING YOUR CODE
# read PEP 8 for details, gives guidelines for styling in python
# this line is added in intellij idea edu

