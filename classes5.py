# THE PYTHON STANDARD LIBRARY
from random import randint

print(randint(2, 8))
print(randint(2, 8))
print(randint(2, 8))
print('\n')

from random import choice

players = ['rohit', 'rahul', 'virat', 'sky', 'rishabh', 'hardik',
           'jadeja', 'varun', 'yuzi', 'natarajan', 'jasprit']
man_of_the_match = choice(players)
man_of_the_series = choice(players)
print(man_of_the_match)
print(man_of_the_series)
print('\n')


# DO IT YOURSELF
# 1:Dice


class Die:
    """Make a model of real-world die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize attributes of the class."""
        self.sides = sides

    def roll_die(self):
        """Roll the die to get any random number b/w 1 and no. of sides."""
        from random import randint
        return randint(1, self.sides)

    def update_die(self, new_sides):
        """Update the no of sides a die has."""
        self.sides = new_sides


d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die.")
print(results)

d10 = Die()
d10.update_die(10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print('\n10 rolls of a 10-sided die.')
print(results)

d20 = Die(sides=20)
results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)

print('\n10 results of a 20-sided die.')
print(results)

# 2:Lottery
from random import choice

tickets = [1, 5, 34, 'k', 55, 9, 'p', 89, 'l', 0, 44, 38, 'a', 13, 'b']
winning_tickets = []
print("\nLets see what the winning ticket is....")

while len(winning_tickets) < 4:
    pulled_item = choice(tickets)

    if pulled_item not in winning_tickets:
        print(f"We pulled a {pulled_item}")
        winning_tickets.append(pulled_item)

print(f"\nLottery entries matching {winning_tickets} wins the prize.")
print('\n')


# 3:Lottery Analysis


def get_winning_ticket(tickets):
    """Return a winning ticket from a set of tickets."""
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(tickets)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    """Check all tickets in the played tickets. If winning ticket return false."""
    for element in played_ticket:
        if element not in winning_tickets:
            return False

    # We must have a winning ticket!
    return True


def make_random_ticket(tickets):
    """Return a random ticket from the set of tickets."""
    random_ticket = []
    while len(random_ticket) < 4:
        pulled_item = choice(tickets)

        if pulled_item not in random_ticket:
            random_ticket.append(pulled_item)

    return random_ticket


tickets = [1, 5, 34, 'k', 55, 9, 'p', 89, 'l', 0, 44, 38, 'a', 13, 'b']
winning_ticket = get_winning_ticket(tickets)
plays = 0
won = False
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(tickets)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket. ;)")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_tickets}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_tickets}")


# 3:Python Module of the Week
"""https://pymotw.com/"""

# Styling Classes
"""1. Class names written in CamelCase.
Don't use underscores. 
Instance and module names should be written in lowercase 
with underscores b/w words. """

"""2. Every class should have a docstring following the class definition.
Each module should also have a docstring describing what the classes
in a module can be used for."""

"""3. Use blank lines to organize code, but not excessively.
1 blank line b/w methods ans 2 lines b/w separate classes."""

"""4. Import a standard library module first, then a blank line
and the import statement for the module you wrote."""
