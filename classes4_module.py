"""A class that can be used to represent a car."""


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
            print("You can't roll the odometer back.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Warn the driver to fill the gas tank."""
        print(f"Please fill your tank soon!")

# Storing Multiple Classes in a Module


"""A set of classes used to represent gas and electric cars."""


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize the attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


# User, Admin, Privileges class
from classes4_module3 import User


class Privileges:
    """An attempt to model the privileges of the admin."""

    def __init__(self):
        """Initialize the attributes of the class."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the privileges"""
        print('The following privileges are enjoyed by the admin:')
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
    """Inherit special user, Admin"""

    def __init__(self, name, surname, age, city):
        """Initialize attributes of parent class as well as of admin."""
        super().__init__(name, surname, age, city)
        self.privileges = Privileges()
