
#
# Code example demonstrating list comprehensions
#
# author: David Mathias
#

from os import listdir
from random import randint
from math import sqrt

print

# create a list of temps in deg F from list of temps in deg C
# first we create a list of temps in deg C
print('Create a list of deg F from a list of deg C temperatures:')
print
dC = [-40, 0, 10, 20, 30, 40, 100]
dF = [1.8 * c + 32 for c in dC]
print('dC: {}'.format(dC))
print('dF: {}'.format(dF))
print

# in this version, we use a list comprehension to create the
# list of degrees C -- a comprehension inside a comprehension
print('Create a list of deg F from a list of degC temperatures.')
print('deg C temps generated randomly by list comprehenstion')
print('within the conversion list comprehension:')
print
dF = [int(1.8 * c + 32) for c in [randint(0, 100) for i in range(8)]]
print('deg F for random deg C: {}'.format(dF))
print

