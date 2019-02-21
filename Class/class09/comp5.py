
#
# Code example demonstrating list comprehensions
#
# author: David Mathias
#

from os import listdir
from random import randint
from math import sqrt

print

# create list of pairs from two lists - result is cross product
print('Create list of pairs from two lists of ints.  Pairing is positional:')
print
xcoords = [randint(0, 100) for i in range(4)]
ycoords = [randint(0, 100) for i in range(4)]
pairs = [(x, y) for x in xcoords for y in ycoords]
print('pairs:')
for p in pairs:
    print('   {}'.format(p))
print

# create list of pairs from two lists - result is cross product
# this time with sorting on both keys
print('Create list of pairs from two lists of ints.  Pairing is positional.')
print('In this version, the pairs are sorted by both keys: first x then y:')
print
xcoords = [randint(0, 100) for i in range(4)]
ycoords = [randint(0, 100) for i in range(4)]
pairs = sorted([(x, y) for x in xcoords for y in ycoords], key=lambda p: (p[0], p[1]))
print('pairs:')
for p in pairs:
    print('   {}'.format(p))
print

