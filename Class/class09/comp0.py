
#
# Code example demonstrating list comprehensions
#
# author: David Mathias
#

from os import listdir
from random import randint
from math import sqrt

print

# a simple, first comprehension
# list of cubes of first 10 non-negative ints
print('Create a list of cubes of first 10 non-negative ints:')
print
cubes = [i**3 for i in range(10)]
print('cubes of 0..9: {}'.format(cubes))
print

