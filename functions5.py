# PASSING AN ARBITRARY NUMBER OF ARGUMENTS
"""Python allows a function to collect an arbitrary number of
 arguments from the calling statement in form of *args."""


def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"The syntax works no matter how many arguments the function receives"


# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
print('\n')


# Using Arbitrary Keyword Arguments


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


albert = build_profile('albert', 'einstein',
                       location='princetown',
                       field='physics')
print(albert)
"This case of creating dictionary is **kwargs, and tuple is *args"

# DO IT YOURSELF
# 1:Sandwiches


def make_sandwiches(*items):
    """Summarize the sandwich we ordered"""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"-{item}")


make_sandwiches('tomato sauce')
make_sandwiches('onion slices', 'peas', 'tomato slices')
make_sandwiches('spinach', 'coconut crush')
print('\n')

# 2:User Profile
pratik = build_profile('pratik', 'mohite',
                       location='goshegaon',
                       field='computer science',
                       hobby='drawing')
print(pratik)
print('\n')

# 3:Cars


def cars(manufacturer, model_name, **car_info):
    """Make a dictionary of car storing its information"""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info


mercedes = cars('mercedes', 'benz',
                color='black',
                tow_package=True)
print(mercedes)
subaru = cars('subaru', 'outback',
              color='blue',
              tow_package=True)
print(subaru)
bmw = cars('bmw', 'arnault',
           color='red',
           tow_package=False)
print(bmw)