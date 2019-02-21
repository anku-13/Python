
#
# Generate a list of random ints and sum them.
#
# author: David Mathais
#

from random import randint

randoms = [randint(0, 100) for _ in range(50)]

# this is a brief block of code to sum the elements
total = 0
for e in randoms:
    total += e
print("\nSum of the numbers: {}\n".format(total))

# this is an even briefer way to tdo the same thing
# note that sum is a built-in function
print("\nSum of the numbers: {}\n".format(sum(i for i in randoms)))
