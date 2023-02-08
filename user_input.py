# USER INPUT
# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)

# Writing clear prompts
name = input('Please enter your name :')
print(f"Hello, {name.title()}!")
print('\n')

prompt = 'If you tell us who you are, we can personalize messages for you.'
prompt += '\nWhat is your name ?'
user = input(prompt)
print(f'Hello, {user}!')
print('\n')

# Using int() to Accept Numerical Input
height = input("How tall are you ?")
height = int(height)
if height >= 150 :
    print("You're tall enough to ride a bike.")
else :
    print("You can't ride yet.")
print('\n')

# The Modulo Operator
number = input("Tell me a number and I'll tell you if it's even or odd :")
number = int(number)
if number % 2 == 0 :
    print(f"The number {number} is even.")
else :
    print(f"The number {number} is odd.")
print('\n')

# Do it Yourself
# 1: Rental Car
car = input('Which car do you want? :')
print(f'Let me see if I can find you a {car.title()}.')
print('\n')

# 2: Restaurant Seating
no_of_seats = input('How many people are in your dinner group? :')
no_of_seats = int(no_of_seats)
if no_of_seats >= 8 :
    print("You'll have to wait for a while.")
else :
    print("Your table is ready.")
print('\n')

# 3: Multiples of Ten
num = input("Tell me a number :")
num = int(num)
if num % 10 == 0 :
    print(f'The number {num} is a multiple of Ten')
else :
    print(f'The number {num} is not a multiple of Ten')


