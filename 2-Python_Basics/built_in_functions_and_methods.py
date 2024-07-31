"""
Some built-in functions we've already used:

str()
int()
float()
type()
print()
"""

greet = 'hellloooo'
print(greet[:])

# What if we used len()?
print(greet[0:len(greet)])

# It's the same as...
print(greet[0:9])
# because the length of greet is 9

# Methods are similar to functions but they are owned by something.
# Ex. String has several methods that only be performed on a string.

# We've actually seen one method before. Remember .format()?

quote = 'to be or not to be'
print(quote.upper())    # Will change the string to all caps.
print(quote.capitalize())   # Capitalizes the beginning of the sentence.
print(quote.find('be'))     # Finds the index of the first occurence
print(quote.replace('be', 'me')) # Replaces all occurrences of 'be' with 'me'

# If we print the quote again, what do you think will happen?
print(quote)
# Answer: Remember strings are immutable so the original string remains.
# Even though we used .replace(), we didn't assign it to anything.

quote = 'to be or not to be'
quote2 = quote.replace('be', 'me')
print(quote2)
print(quote)