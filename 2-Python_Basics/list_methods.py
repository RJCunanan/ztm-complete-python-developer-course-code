basket = [1,2,3,4,5]

#adding

#append()
new_list = basket.append(100)
print(basket)   # basket has 100 appended to it
print(new_list) # returns None
# This is because append() just appends to the list
# without returning the result

# Need to do something like this:
new_list = basket   # point new_list to the basket
print(basket)
print(new_list)

#insert()
basket.insert(4, 100)   # At the index 4, add 100
new_list = basket.insert(4, 100)    # Doesn't work, just like append
print(basket)
print(new_list) # Doesn't work; returns None

#extend()
new_list = basket.extend([100, 101])    # Iterates over a list and adds another list to it
print(basket)
print(new_list) # Doesn't work; returns None


#removing

#pop()
basket = [1,2,3,4,5]
basket.pop()    # pops off the end of the list
basket.pop(0)   # removes item at index 0
print(basket)

new_list = basket.pop(2)    # will return the value and give it to new_list
print(new_list)

#remove()
basket = [1,2,3,4,5]
new_list = basket.remove(4)    # removes the value 4 from the list; doesn't return a value
print(basket)
print(new_list) # Doesn't work; returns None

#clear()
basket = [1,2,3,4,5]
new_list = basket.clear()   # Removes everything in the list, but doesn't return value
print(new_list)
print(basket)


# You have to be careful and know what each method returns, whether None or a value