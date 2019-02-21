
#
# Various examples related to the use of variables.
#
# author: David Mathias
#

x = 20
print type(x)
print

y = 20.0
print type(y)
print

s = "a"
print type(s)
print

c = 'a'
print type(c)
print
 
b = True
print type(b)
print

print('8/11 = {}'.format(8/11))
print

print('8.0/11 = {}'.format(8.0/11))
print

print('float(8)/11 = {}'.format(float(8)/11))
print

s = '12'
print('int(s) = '.format(int(s)))
print('int(s) + 10 = {}'.format(int(s) + 10))
# the next line would give an error
# print('s + 10 = {}'.format(s+10))
print

pi = 3.14159
print('int(pi) = {}'.format(int(pi)))
print

s1 = 'This is '
s2 = 'a test.'
print 's1 = ' + s1
print 's2 = ' + s2
print('s1 + s2 = {}'.format(s1 + s2))
print

s3 = s1 + s2
print('s3 = s1 + s2. s3 = ' + s3)
print

s = 'Spam '
print('s = Spam. s*4 = ' + s*4)
print

