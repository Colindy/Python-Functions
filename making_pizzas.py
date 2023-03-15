# Here, I import a function from a module and give it a nickname

from pizza import make_pizza as mp

# I can then take that nickname and use it to call the function
# from the imported module.

mp('16', 'pepperoni')
mp('22', 'sausage', 'mushroom', 'extra cheese')

