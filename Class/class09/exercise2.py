
#
# Code example demonstrating list comprehensions
#
# author: David Mathias
#

from os import listdir
from random import randint
from math import sqrt

print

# create list of only odd values from an int list
print('Create list of only the odd values from a random list of ints:')
print
data = []
for i in range(12):
    data.append(randint(0, 1000))
odds = [i for i in data if i % 2 == 1]
print('data: {}'.format(data))
print('odds: {}'.format(odds))
print
