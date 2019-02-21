
#
# Code example demonstrating a couple of simple file methods
#
# author: David Mathias
#

from os import listdir

# open a file and read contents into a list of strings
fn = open('random_ex.py', 'r')
lines = fn.readlines()
fn.close()
for line in lines:
    print line
print

# create a list of the files in a directory
# stores all files names in a directory in a list
path = '.'
files = listdir(path)
for f in files:
    print f
print
