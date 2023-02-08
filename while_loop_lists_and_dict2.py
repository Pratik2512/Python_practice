# Do It Yourself
# 1:Deli Restaurant
sandwich_orders = ['tuna', 'pastrami', 'fried egg', 'grilled cheese',
                   'pastrami', 'ham', 'pastrami', 'meat ball']
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
print(f"finished_sandwiches = {finished_sandwiches}")
print("\nThe following sandwiches are completed:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich} sandwich")

# 2:No Pastrami
sandwich_orders = ['tuna', 'pastrami', 'fried egg', 'grilled cheese',
                   'pastrami', 'ham', 'pastrami', 'meat ball']
finished_sandwiches = []
print("\nThe Deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)
print("Only the following sandwiches will be made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich} sandwich")

# 3:Dream Vacation
dream_vac = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name dude? ")
    vacation = input("And what's your dream vacation? ")
    dream_vac[name] = vacation
    another_poll = input("Next ? (yes/ no) ")
    if another_poll == 'no':
        polling_active = False
print('\n')
for name, vacation in dream_vac.items():
    print(f"{name.title()}'s dream vacation is {vacation.title()}")
