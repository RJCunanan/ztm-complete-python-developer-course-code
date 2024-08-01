# List slicing

# Remember string slicing?
string = 'helllooo'
string[0:2:1]

# We can do the same with lists:
amazon_cart = [
    'notebooks', 
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])

# However, unlike strings, you can change individual items in a list:
amazon_cart[0] = 'laptop'
print(amazon_cart[1:3])
print(amazon_cart)   # Original cart remains unchanged even after slicing

# Notice that by slicing, we are NOT changing the original list.
# With list slicing, you are actually creating a new list

new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# But what if we did this?
amazon_cart[0] = 'laptop'
new_cart = amazon_cart   # Notice we are not slicing
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Answer, we are modifying both new_cart and the original amazon_cart.
# This is because the first line "new_cart = amazon_cart" is pointing
# to the original cart's place in memory and modifying it.

# To preven this, we can do the following:
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]   # Use list slicing to create a copy
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
