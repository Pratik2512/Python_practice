# IMPORTING CLASSES
# Importing a Single Class
from classes4_module import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print('\n')

# Storing Multiple Classes in a Module

from classes4_module import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print('\n')


# Importing Multiple Classes from a Module
from classes4_module import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla2 = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla2.get_descriptive_name())
print('\n')

# Importing an Entire Module
import classes4_module

my_beetle = classes4_module.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = classes4_module.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print('\n')

# Importing All Classes from a Module
from classes4_module import *

# Importing a Module into a Module
from classes4_module import Car
from classes4_module2 import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print('\n')

# Using Aliases
from classes4_module2 import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print('\n')

# Finding your Own Workflow
