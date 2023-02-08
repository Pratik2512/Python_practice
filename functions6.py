# STORING YOUR FUNCTIONS IN MODULES
""" You can store your functions in a separate file called a module
and then importing that module into your main program. An import
statement tells python to make the code inn the module available
in the currently running program file.
Storing your functions in a separate file allows you to hide the details
of your program's code and focus on the higher-level logic. It allows you 
 to reuse functions inn many different programs. You can also share them with
 other fellow programmers."""

# Importing an Entire Module

import functions6_module

functions6_module.make_pizza(16, 'pepperoni')
functions6_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
rohit = functions6_module.build_profile('rohit', 'sharma',
                                location='mumbai',
                                field='cricket') 
print(rohit)

# Importing Specific Functions
from functions6_module import cars

baleno = cars('tata', 'baleno',
              color='blue',
              tow_power=True)
print(baleno)

from functions6_module import make_pizza, build_profile

make_pizza(15, 'extra cheese')
tom = build_profile('tom', 'cruise')
print(tom)

# Using as to Give a Module an Alias
import  functions6_module as f6m

f6m.make_pizza(11, 'tandoor')

# Using as to Give a Function an Alias
from functions6_module import make_pizza as mp

mp(14, 'salty onion')

# Importing All Functions in a Module
from functions6_module import *

# Styling Functions
"""1. Functions should have descriptive names, and these names 
should use lowercase letters and underscores.
2. Every function should have a comment that explains concisely 
what the function does. In docstring format.
3. If you specify default value for a parameter, no spaces should
be used on either side of the equal sign.
4. Limit lines of code to 79 characters.
5. All import statements should be written at the beginning of a file.
The only exception is if you use comments at the beginning of your file."""

# DO IT YOURSELF
# 1:Printing Models
