# Creating module
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def cars(manufacturer, model_name, **car_info):
    """Make a dictionary of car storing its information"""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info
