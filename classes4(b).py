# DO IT YOURSELF
# 1:Imported Restaurant
from classes4_module2 import Restaurant

hotel_manjiri = Restaurant('hotel manjiri', 'indian')
hotel_manjiri.describe_restaurant()
hotel_manjiri.open_restaurant()
print('\n')

# 2:Imported Admin
from classes4_module2 import Admin

jason = Admin('jason', 'roy', 27, 'birmingham')
jason.describe_user()
jason.privileges.show_privileges()
print('\n')

# 3:Multiple Modules
from classes4_module import Admin

jason = Admin('jason', 'roy', 27, 'birmingham')
jason.describe_user()
jason.privileges.show_privileges()
