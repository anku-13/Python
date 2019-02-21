#
# Code example demonstrating iteration
#
# author: David Mathias
#

from random import shuffle, randint, random

# create a few lists
L1 = ['Blue Hens', 'Hoosiers', 'Buckeyes', 'Mocs', 'Eagles']
L2 = []
L3 = []
L4 = []

print

# use of a simple while loop
print('Create L2 using a simple while loop:')
i = 0
max = 25
while i < max:
    L2.append(max - i)
    i += 1

print("   L2: {}".format(L2))
print


# use of a simple for loop
# in this case, i is only the index variable and 
# is not used in the loop
print('Create L3 and L4 using a simple for loop:')
for i in range(5):
    x = randint(0, 100)
    L3.append(x)
    L4.append(x)
    
print("   L3: {}".format(L3))
print


# processing elements of list using range and len
print("Print L3 using i in range:")
for i in range(len(L3)):
    print('   {}'.format(L3[i]))
print


# processing elements of list using iterator
print("Print L3 using e in list:")
for e in L3:
    print('   {}'.format(e))
print


# changing elements of list using range and len
print("Change L3 using i in range:")
for i in range(len(L3)):
    L3[i] += random()

# output result
for e in L3:
    print('   {}'.format(e))
print


# Changing elements of list using iterator
print("Change L4 using e in list (iterator):")
for e in L4:
    e += random()

# output result
for e in L4:
    print('   {}'.format(e))
print


# Another attempt at changing a list using an iterator
print('Another attempt to change a list in an iterator:')
print('   Our lists L1 to L4 are the elements of list L5')
L5 = [L1, L2, L3, L4]
print('   Now use an iterator to change the first element of each list to 0')
for e in L5:
    e[0] = 0

print('   First element of each of the lists:')
for e in L5:
    print('   {}'.format(e[0]))
print

print('   First elements of L1, L2, L3, L4:')
print('   {}'.format(L1[0]))
print('   {}'.format(L2[0]))
print('   {}'.format(L3[0]))
print('   {}'.format(L4[0]))
print


# enumerate gives you both an index and an element
print('Use of enumerate to process list elements:')
for i, e in enumerate(L4):
    print('   pos: {}   val: {}'.format(i, e))
print
