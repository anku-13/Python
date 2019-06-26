import time
import threading
from random import random


class ClockThread(threading.Thread):
    
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.daemon = False
        self.interval = interval
        
    def run(self):
        for i in range(10):
            print('Thread: {}  The time is: {}'.format(self.name, time.ctime()))
            time.sleep(self.interval)
    

def main():
    print('\nmain is starting\n')
    t1 = ClockThread(2)
    t1.start()
    
    t2 = ClockThread(3)
    t2.start()
    
    t1.join()
    t2.join()
    
    print('\nmain is finishing\n')
    
if __name__ == '__main__':
    main()
    