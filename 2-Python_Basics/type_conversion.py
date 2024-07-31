# Type Conversion:
# int()
# str()
# float()
# etc.

# Is the following an int or a string?
print(str(100))

# Let's find out:
print(type(str(100)))   # Answer: string

print(type(int(str(100))))   # int

# Note: the above code is the same as doing the following:
a = str(100)
b = int(a)
c = type(b)
print(c)

