# INTRODUCING WHILE LOOPS
# The while Loop in Action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
print('\n')

# Using a Flag
prompt = "\nTell me something :"
prompt += "\nEnter 'quit' to exit"
message = ""
active = True  # flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
print('\n')

# Using break to Exit a Loop
prompt = "\nPlease enter the city name you visited :"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}.")
print('\n')

# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue   # python ignores rest of the loop and returns to the start
    print(current_number)
print('\n')

# Avoiding Infinite Loops
x = 1
while x <= 5:
    print(x)
    x += 1




