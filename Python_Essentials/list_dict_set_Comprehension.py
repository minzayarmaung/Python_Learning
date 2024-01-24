# List , Dict and Set Comprehension

# As I'm also the one who currently learning Python , they are quite confusing for me.

# Here is the explanation I found from Medium

# list  = [expression for i in iterable if condition]
# dict = {key:value for i in iterable if condition}
# set = {value for i in iterable if condition}

# Example: Create a list of squares for even numbers from 0 to 9
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(even_squares)
# Output: [0, 4, 16, 36, 64]

# Example: Create a dictionary of squares for even numbers from 0 to 9
even_squares_dict = {i: i**2 for i in range(10) if i % 2 == 0}
print(even_squares_dict)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Example: Create a set of squares for odd numbers from 0 to 9
odd_squares_set = {i**2 for i in range(10) if i % 2 != 0}
print(odd_squares_set)
# Output: {1, 9, 25, 49, 81}

