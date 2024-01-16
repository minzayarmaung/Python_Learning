# Using 'pprint' in Python

# ppprint function allows us to display long , complicated nested data structures in
# a easily-readable format.

x = [
  {'apple': [1,2,3], 'orange':[4,5,6]},
  {'pear': [7,8,9], 'pineapple':[10,11,12]},
  {'durian':[13,14,15], 'banana':[16,17,18]}
]

# if we use print : 

print(x)

print()

# if we use pprint (Data pretty printer) :
# We can install it by using ( pip install pprintpp ) and import pprint

from pprint import pprint

pprint(x)

# It makes complex data structures into a more friendly human readable form.