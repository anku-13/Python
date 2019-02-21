
## make list of f to class
# df = [(9/5)*i +32 for i in dc]
# fc = [i*1.8 +32 for i in dc]
from random import randint
import math
df = [1.8 * c +32 for c in [randint(0,100) for i in range(10)]]
# print df

roots = [math.sqrt(i) for i in [randint(-100,100) for i in range(10)] if i >0]
# print roots

# roots = [math.sqrt(i) for i in [randint(-100,100) for i in range(10)] if i >0]
rand = [randint(0,100) for i in range(10)]
odd = [j for j in [randint(0,100) for i in range(10)] if j%2]
# print odd

print("rand:\t{}".format(rand))

pairs = [(x, y) for x in rand for y in rand]
print("cross:\t{}".format(pairs))

pairs = [(x, y) for x in rand for y in rand if x == y]
print("equal:\t{}".format(pairs))

data = [[0,1],[2,3]]
# bigData = [ x for x in d for d in data]
bigData = [x for sub in data for x in sub]
print bigData
