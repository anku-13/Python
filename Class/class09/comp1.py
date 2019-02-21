
#
# Code example demonstrating list comprehensions
#
# author: David Mathias
#

from os import listdir
from random import randint
from math import sqrt

print

# example using os.listdir
print('List comprehension using listdir to create list of files.')
print('The comprehension prepends the path to each filename.')
print
path = '..'
files = [path + '/' + f for f in listdir(path)]
print('files:')
for f in listdir(path):
    print('   {}'.format(f))
print
print('files with path:')
for f in files:
    print('   {}'.format(f))
print
