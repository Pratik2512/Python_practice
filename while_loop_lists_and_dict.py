# USING A WHILE LOOP WITH LISTS AND DICTIONARIES
# Moving Items from One List to Another
# The pop() function
# removes and returns last value from the list or thr given index value
unconfirmed_users = ['alice', 'adam', 'candice', 'davey']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying User: {current_user.title()}")
    confirmed_users.append(current_user)
print('\n')
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
pets =['dog', 'cat', 'goldfish', 'rabbit', 'cat', 'tortoise', 'dog', 'cat', 'peacock', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb?")
    responses[name] = response
    repeat = input("Would you like next person to take the poll? (yes\ no)")
    if repeat == ' no':
        polling_active = False
print("\n-------Poll Results-------")
for name, responses in responses.items():
    print(f"{name.title()} would like to climb {responses.title()}.")
