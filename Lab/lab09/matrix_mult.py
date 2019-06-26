import time
import threading
from random import random, randint

# global constants
size = 20       # matrix size in each dimension
factor = 2      # number of threads is size/factor

# class for threads to do matrix multiplication
class MultThread(threading.Thread):
    num_threads = size/factor

    # id is simply an integer identifier
    # should be assigned sequentially starting at 0
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.daemon = False
        self.id = id

    def run(self):
        multiply(self.id)


# let's do some matrix multiplication using threads.
# we need to know which thread so that we know which rows
# it will calculate.
def multiply(id):
    global size
    global factor
    global m1
    for i in range (factor*id, factor*id +1) :
        for j in range(size) :
            ls = []
            for j in range(size):
                
            # m1[i][j] = sum(m1[i]) + sum([x for x in ])

# 1120 apt f

def main():
    print('\nmain is starting\n')

    # create the threads and run them

    global size
    global factor
    tlist = []
    for i in range(size/factor) :
        tlist.append(MultThread(i))
    for t in tlist:
        t.start()
    for t in tlist:
        t.join()

    # output the result
    print(m3)

    print('\nmain is finishing\n')


if __name__ == '__main__':
    # create global matrices
    # m1 and m2 contain random data and are the operands
    # m3 contains all 0 and is the result
    m1 = [[randint(0, 100) for _ in range(size)] for _ in range(size)]
    m2 = [[randint(0, 100) for _ in range(size)] for _ in range(size)]
    m3 = [[0 for _ in range(size)] for _ in range(size)]

    main()
