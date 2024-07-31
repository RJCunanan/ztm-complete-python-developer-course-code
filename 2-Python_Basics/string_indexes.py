# Strings are stored in memory as an ordered sequence of characters.

'me me me'     # 'm' is located at 0, 'e' at 1, ' ' at 2, etc.
# 01234567

selfish = 'me me me'
         # 01234567

# If we want to get a specific character from the string:
print(selfish[0])
print(selfish[1])
print(selfish[2])
print(selfish[3])

# [start:stop] Note: the character at the 'stop' is not taken
selfish = '01234567'
print(selfish[0:2])

# [start:stop:stepover] Note: stepover will skip over characters
print(selfish[0:8:2])


# What if we did the following, what would happen?

print(selfish[1:])  
# Answer: will start at the beginning and go all the way to the end

print(selfish[:5]) 
# Answer: will start at default 0 and end at 5

print(selfish[::1]) 
# Answer: you get the default behavior

print(selfish[-1]) 
# Answer: you get 7
# In python, a negative index means start at the end of the string

print(selfish[-2])  #6
print(selfish[-3])  #5

print(selfish[::-1]) 
# Answer: We get the reverse of the string

print(selfish[::-2]) 