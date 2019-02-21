
#
# Code example demonstrating several random operations
#
# author: David Mathias
#

from random import randint, shuffle, random

# randint(x, y): returns random integer in [x..y]
print("   Result of randint(0, 100): {}".format(randint(0, 100)))
print

# shuffle: permutes a list
# does not return a value -- alters parameter
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(L)
print("   L: {}".format(L))
print

# random: return float in [0..1)
print("   Result of random(): {}".format(random()))
print
