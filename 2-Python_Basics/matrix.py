# Matrix - a way to describe 2-D or multi-dimensional lists
# Arrays inside of an array

matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]

# Why is this important?
# Well, say we have an image composed of 0s and 1s stored in matrices.
# We can use these matrices to say draw and display an X using 0s and 1s.
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# Using matrices, we can do alot of heavy calculations

# How to access a multi-dimensional array:
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]
print(matrix[0][1])