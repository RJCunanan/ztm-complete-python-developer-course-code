# Immutability
# Strings in Python are immutable, meaning they cannot change.

selfish = '01234567'

# selfish = 100
# print(selfish)

# Below will produce an error because you can't change part of selfish.
# The only way to change selfish is the comepletely replace the value.
selfish[0] = '8'
print(selfish)

# You can however add to a string like the following:
selfish = selfish + '8'
print(selfish)