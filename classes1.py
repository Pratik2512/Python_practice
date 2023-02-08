# CREATING AND USING A CLASS
"""Making an object from a class is called instantiation,
and you work with instances of a class."""


# Creating and Using a Class
#       Creating the Dog Class
class Dog:
    """A simple attempt to model a Class"""

    # The __init__() Method : a function that's part of a class is a method.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


"Variables that are accessible through instances are called attributes"
# Making an Instance from a Class
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#         Accessing Attributes
"""To access the attributes of an instance, you use dot notation."""
print(my_dog.name)

#         Calling Methods
my_dog.sit()
my_dog.roll_over()

#         Creating Multiple Instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 4)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# DO IT YOURSELF
# 1:Restaurant


class Restaurant:
    """An attempt to model a class."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Display the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")


my_restaurant = Restaurant("Maratha_Hotel", "night ")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 2:Three Restaurants
manjiri_hotel = Restaurant("Hotel Manjiri", "daily")
manjiri_hotel.describe_restaurant()

ganaraj_hotel = Restaurant("Hotel Ganaraj", "everyday")
ganaraj_hotel.describe_restaurant()

jw_marriot = Restaurant("JW Marriot", "all season")
jw_marriot.describe_restaurant()

# 3:Users


class User:
    """Create a profile of the user."""
    def __init__(self, name, surname, age, city):
        self.first_name = name
        self.last_name = surname
        self.age = age
        self.city = city

    def describe_user(self):
        """Display the user info."""
        print(f"name: {self.first_name} {self.last_name}")
        print(f"age: {self.age} years")
        print(f"city: {self.city}.")

    def greet_user(self):
        """Greet the user."""
        print(f"\nHello {self.first_name}!")


alice = User('Alice', 'Evram', 19, 'Durham')
alice.greet_user()
alice.describe_user()

noman = User('Noman', 'Sharma', 26, 'Bangalore')
noman.greet_user()
noman.describe_user()
