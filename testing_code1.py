# TESTING A FUNCTION
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()


print("Enter 'q' at any time to quit." )
while True:
    first = input("\nPlease give me your first name: ")
    if first == 'q':
        break
    last = input("Please give me your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")


# Unit Tests and Test Cases
"""
The module unittest from the Python standard library provides tools for
testing your code. A unit test verifies that one specific aspect of a function’s
behavior is correct. A test case is a collection of unit tests that together prove
that a function behaves as it’s supposed to, within the full range of situa-
tions you expect it to handle. A good test case considers all the possible
kinds of input a function could receive and includes tests to represent each
of these situations. A test case with full coverage includes a full range of unit
tests covering all the possible ways you can use a function."""

#        A Passing Test
"""Refer to testing_module.py and testing_code.py"""

#        A Failing Test
"""Refer to testing_module.py and testing_code.py"""

#        Responding to a Failed Test
"""Refer to testing_module.py and testing_code.py"""

#        Adding New Tests
"""Refer to testing_module.py and testing_code.py"""

# DO IT YOURSELF
# 1:City, Country


def city_info(city, country):
    """Describe the city and its coountry neatly."""
    name = f"{city}, {country}"
    return name.title()


mumbai = city_info('mumbai', 'india')
print(mumbai)


def city_info(city, country, population):
    """Describe the city and its country neatly."""
    name = f"{city}, {country}, Population:{population}"
    return name.title()


mumbai = city_info('mumbai', 'india', 50000)
print(mumbai)