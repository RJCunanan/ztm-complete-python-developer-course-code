user_iq = 190
print(user_iq)

"""
Variables:
- snake_case
- Start with lowercase or underscore
- Letters, numbers, underscores
- Case sensitive
- Don't overwrite keywords.
"""

# Note that variables that start with a "_" are private variables, but we'll go over this later on in the course.
_user_iq = 190
print(_user_iq)

us4er_iq3 = 190
print(us4er_iq3)

user_IQ = 190
print(user_IQ)

# You can't use keywords as variables. For example, this will cause an error:
# print = 190
# print(print)

# A good rule of thumb for variables is to make them really descriptive.
iq = 190
user_age = iq / 4
a = user_age
print(a)

# Constants: things that DON'T change in a program
# The convention is to write constant variable name in all caps to indicate that this value should not change.
PI = 3.14

# Dunder variables, indicated by two underscores "__" in the beginning, are meant to be left alone. You should NOT create a variable with two underscores.
# __hihi = 'hi'   DO NOT DO THIS!!!

# Note: Make sure your code, especially variable names, are readable and understandable to other programmers so they know what is going on.

# We can also assign multiple variables at the same time:
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)