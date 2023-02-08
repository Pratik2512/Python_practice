# WORKING WITH CLASSES AND INSTANCES
#         The Car Class


class Car:
    """A simple attempt to display a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a cleanly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
print('\n')

# Setting a Default Value for an Attribute


class Car:
    """A simple attempt to display a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a cleanly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"The car has {self.odometer_reading} miles on it.")


print("'Setting a default value.'")
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying Attribute Values
#       Modifying an Attribute's Value Directly
print("\n'Modifying an Attribute's Value Directly'")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#       Modifying an Attribute's Value Through a Method
print("\n'Modifying an Attribute's Value Through a Method'")


class Car:
    """A simple attempt to display a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a cleanly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(144)
my_new_car.read_odometer()

#      Incrementing an Attribute's Value Through a Method
print("\n'Incrementing an Attribute's Value Through a Method'")


class Car:
    """A simple attempt to display a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a cleanly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(24_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

# DO IT YOURSELF
# 1:Number Served


class Restaurant:
    """An attempt to model a class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """Display the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")

    def show_number_served(self):
        """Display the number of plates served."""
        print(f"\n{self.number_served} plates are served.")

    def set_number_served(self, plates):
        """Set the number of plates served."""
        self.number_served = plates

    def increment_number_served(self, plates):
        """Add to the no of plates served."""
        self.number_served += plates


ganaraj_hotel = Restaurant('ganaraj hotel', 'indian')
ganaraj_hotel.describe_restaurant()
ganaraj_hotel.open_restaurant()

ganaraj_hotel.show_number_served()

ganaraj_hotel.set_number_served(25)
ganaraj_hotel.show_number_served()

ganaraj_hotel.increment_number_served(15)
ganaraj_hotel.show_number_served()

# 2:Login Attempts


class User:
    """Create a profile of the user."""
    def __init__(self, name, surname, age, city):
        self.first_name = name
        self.last_name = surname
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Display the user info."""
        print(f"name: {self.first_name} {self.last_name}")
        print(f"age: {self.age} years")
        print(f"city: {self.city}.")

    def greet_user(self):
        """Greet the user."""
        print(f"\nHello {self.first_name}!")

    def increment_login_attempt(self):
        """Add the number of attempts to the original tally."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the no of login attempts."""
        self.login_attempts = 0


alex = User('alex', 'hales', 27, 'surrey')
alex.describe_user()
alex.greet_user()
alex.increment_login_attempt()
alex.increment_login_attempt()
alex.increment_login_attempt()
alex.increment_login_attempt()
alex.increment_login_attempt()
alex.increment_login_attempt()
print(f"\nAlex's login attempts are {alex.login_attempts}.")
alex.reset_login_attempts()
print(f"Alex's login attempts are {alex.reset_login_attempts()}.")
