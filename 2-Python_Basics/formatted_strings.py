# Formatted strings

# Usually in the real world, we want strings to be dynamic.
# The following can be a bit cumbersome:
name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' year old')

# To do formatted strings, simply add an 'f' at the beginning and use curly brackets { }. This is a new feature of python 3 and is now the preferred method:
print(f'hi {name}. You are {age} year old')

# Before, in python 2, we did this:
print('hi {}. You are {} year old'.format('Johnny', '55'))
print('hi {}. You are {} year old'.format(name, age))

# Say we wanted to switch the order:
# Note: we always count from 0
print('hi {1}. You are {0} year old'.format(name, age))

# The following will cause an error
"""
print('hi {0}. You are {1} year old'.format(new_name='sally', age=100))
"""

# Instead, you do the following:
print('hi {new_name}. You are {age} year old'.format(new_name='sally', age=100))