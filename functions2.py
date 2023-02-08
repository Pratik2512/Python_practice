# PASSING ARGUMENTS
# Positional Arguments
""" Passing the arguments in the order of asked parameters """


def describe_dog(dog_type, dog_name):
    """Display information about the dog"""
    print(f"I have a {dog_type}.")
    print(f"My {dog_type}'s name is {dog_name.title()}.\n")


describe_dog('labrador', 'cooper')

# Multiple Function Calls
describe_dog('poodle', 'charlie')

""" Order matters in Positional Arguments"""

# Keyword Arguments
""" A keyword argument is a name-value pair that 
    you pass to a function. """
describe_dog(dog_type='chow chow', dog_name='bella')
"Here order of keyword arguments doesn't matter"


# Default Values


def describe_dog(dog_name, dog_type='labrador'):
    """Display using default values"""
    print(f"I have a {dog_type}.")
    print(f"My {dog_type}'s name is {dog_name.title()}.\n")


describe_dog('stella')
describe_dog('max', 'chihuahua')

# Equivalent Function Calls
describe_dog('lucy')
describe_dog(dog_name='lucy')


# Avoiding Argument Errors
# describe_dog()


# DO IT YOURSELF
# 1:T-Shirt


def make_shirt(size, message):
    """Displays the size and message on shirt to be made"""
    print(f"The size of the shirt is {size},"
          f" with '{message.title()}' printed on it.\n")


make_shirt('S', 'wanderlust')
make_shirt(message='explorer', size='L')


#  2:Large Shirts
def make_shirt(size='L', message='i love python'):
    """Display using default values"""
    print(f"The size of the shirt is {size},"
          f" with message '{message.title()}' printed on it.\n")


make_shirt()
make_shirt('M')
make_shirt('XL', 'haqq se single')


# 3:Cities
def describe_city(city, country='india'):
    """Displays the city and its country"""
    print(f"{city.title()} is in {country.title()}.\n")


describe_city('mumbai')
describe_city('hiroshima', 'japan')
describe_city('london', 'england')