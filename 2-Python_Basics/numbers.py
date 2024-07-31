# Fundamental Data Types

# int and float:
print(type(2 + 4))   #type() tells us the datatype
print(type(2 - 4))
print(type(2 * 4))

# Notice the type of this is a float, or a number with a decimal point
print(type(2 / 4))

print(type(5.00001))    #float

print(type(0))  #int

# Why make this distinction? Because floats take up more memory than an int because floats are harder to represent as a binary number (0s and 1s) in memory than say an integer

# int + float: python will automatically convert to a float
print(type(20 + 1.1)) 

print(type(9.9 + 1.1))   #float

# to the power of (exponents):
print(2 ** 3)

# returns integer rounded down after dividing:
print(2 // 4)
print(3 // 4)
print(5 // 4)

# modulo (remainder):
print(5 % 4)
print(6 % 4)