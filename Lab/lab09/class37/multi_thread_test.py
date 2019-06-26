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
    
    tlist = []
    for i in range(20):
        tlist.append(ClockThread(random() * 4))
        
    for t in tlist:    
        t.start()
    
    for t in tlist:
        t.join()
        
    print('\nmain is finishing\n')
    
if __name__ == '__main__':
    main()
    