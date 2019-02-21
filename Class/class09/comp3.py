
#
# Code example demonstrating list comprehensions
#
# author: David Mathias
#

from os import listdir
from random import randint
from math import sqrt

print

# create list of square roots using filtering to ensure we 
# don't take the square root of a negative number
print('Create list of square roots using comprehension with')
print('filtering to prevent taking root of negative:')
print
nums = [16, 144, -25, 10000, 81, 121, -100, 625]
roots = [sqrt(i) for i in nums if i >= 0]
print('nums: {}'.format(nums))
print('roots: {}'.format(roots))
print

