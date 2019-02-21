
#
# Several addiional loop operations
#
# author: David Mathias
#

cs224 = ['Johnny', 'Sally', 'Billy', 'Bobby', 'Janie']
print('   cs224: {}'.format(cs224))
print

# example using in to check list membership
if 'Billy' in cs224:
    print('   Billy is present')
else:
    print('   Billy is absent')
print


# the range command
# returns a Python list
#    range(x): [0..x-1]
#    range(x, y): [x..y-1]
print("   Result of range(15): {}".format(range(15)))
print
print("   Result of range(10, 30): {}".format(range(10, 30)))
print


# assignment of a list creates an alias
print('Demo of list assignment creating an alias:')
L2 = cs224
print('   cs224 assigned to L2')
L2[0] = 'Tommy'
print('   change an element of L2: L2[0] = Tommy')
print('   cs224: {}'.format(cs224))
print
