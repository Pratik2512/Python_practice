# Do It Yourself


class Restaurant:
    """An attempt to model a class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe restaurant's name is {self.restaurant_name.title()}.")
        print(f"The cuisine type is {self.cuisine_type.title()}.")

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


class IceCreamStand(Restaurant):
    """Represent aspects of restaurant, particular to ice cream stand"""

    def __init__(self, restaurant_name, cuisine):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to ice cream stand
        """
        super().__init__(restaurant_name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'custard', 'strawberry']

    def display_flavors(self):
        """Display the flavors available."""
        print(f"The available flavors are:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


bharkadevi = IceCreamStand('bharkadevi', 'indian')
bharkadevi.describe_restaurant()
bharkadevi.display_flavors()

# 2:Admin
print('\n')


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
        print(f"name: {self.first_name.title()} {self.last_name.title()}")
        print(f"age: {self.age} years")
        print(f"city: {self.city.title()}.")

    def greet_user(self):
        """Greet the user."""
        print(f"\nHello {self.first_name}!")

    def increment_login_attempt(self):
        """Add the number of attempts to the original tally."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the no of login attempts."""
        self.login_attempts = 0


class Admin(User):
    """Inherit special user, Admin"""

    def __init__(self, name, surname, age, city):
        """Initialize attributes of parent class as well as of admin."""
        super().__init__(name, surname, age, city)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the privileges enjoyed by the admin."""
        print('The following privileges are enjoyed by the admin:')
        for privilege in self.privileges:
            print(f"\t{privilege}")


pratik = Admin('pratik', 'mohite', 19, 'pune')
pratik.describe_user()
pratik.show_privileges()

# 3:Privileges
print('\nPrivileges')


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


pratik = Admin('pratik', 'mohite', 19, 'pune')
pratik.describe_user()
pratik.privileges.show_privileges()

# 4:Battery Upgrade
print('\n--Battery Upgrade--')


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
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Warn the driver to fill the gas tank."""
        print(f"Please fill your tank soon!")


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

    def upgrade_battery(self):
        """Upgrade the electric car's battery."""
        self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize the attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
