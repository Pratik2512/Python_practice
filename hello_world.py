{
	"cmd":["python3","-u","$file"],
}
print('Hello Python interpreter!')
message = 'Hello Python world'
print(message)
message = 'Hello Python Crash Course World'
print(message)

# Variables and literals 
village = 'goshegaon'
# here 'village' is variable and 'goshegaon' is a literal. 
# numeric literals 
# integers : 5, 0, -23
# floats : 1.32, 1.525e2 = 1.525*10^2
# complex numbers : 1.5j, 2+3.4j 

# Use triple quotes for multiline string
multiline_string = """Name: Pratik
Salary : 50000 
Age : 19 """
print(multiline_string)

# input() FUNCTION 
name = input("Enter here :")
print("Hello", name)
a = input("keep silence :")
print(a)