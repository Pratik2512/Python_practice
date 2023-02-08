# Do it Yourself
# 1: Pizza Toppings
prompt = "\nWhich topping would you like to add to your pizza?"
prompt += "\n(enter 'quit' to end):"
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"Your topping {topping} will be added shortly.")
print("\n")

# 2: Movie Tickets
prompt = "\nTell me ur age and I'll tell u ur movie ticket cost."
prompt += "\n(enter '222' to end :)"
age = ""
active = True
while active:
    age = input(prompt)
    age = int(age)
    if age == 222:
        active = False
    elif age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
print('\n')

# Three Exits :

