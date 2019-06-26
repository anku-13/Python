import time
import threading
from random import random

class LockThread(threading.Thread):
    mutex = threading.Lock()
    
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.daemon = False
        self.name = name
        
    def run(self):
        if self.name == 'Producer':
            produce(self.name)
        elif self.name == 'Consumer':
            consume(self.name)
            

def main():
    t1 = LockThread('Producer')
    t1.start()
    
    t2 = LockThread('Consumer')
    t2.start()
    
    t1.join()
    t2.join()
    print('Final counter: {}'.format(counter))
    print('Final buffer: {}'.format(buffer))
    

def produce(name):
    global counter
    global bufsiz
    global buffer
    global in_pos
    for i in range(200):
        while counter >= bufsiz:
            print('{} waiting on counter'.format(name))

        LockThread.mutex.acquire()
        print('{} adding an item'.format(name))
        counter = counter + 1
        buffer[in_pos] = 'full'
        in_pos = (in_pos + 1) % bufsiz
        LockThread.mutex.release()
            
        time.sleep(random())
    
    
def consume(name):
    global counter
    global bufsiz
    global buffer
    global out_pos
    for i in range(200):
        while counter <= 0:
            print('{} waiting on counter'.format(name))

        LockThread.mutex.acquire()
        print('{} removing an item'.format(name))
        counter = counter - 1
        buffer[out_pos] = 'empty'
        out_pos = (out_pos + 1) % bufsiz
        LockThread.mutex.release()
        
        time.sleep(random())
        
    
if __name__ == '__main__':
    counter = 0
    in_pos = 0
    out_pos = 0
    bufsiz = 20
    buffer = ['empty'] * bufsiz
    main()
    