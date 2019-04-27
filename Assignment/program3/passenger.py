from random import randint

class Passenger:
    num_passengers = 1
    def __init__(self, max_floor):
        self.src_floor = randint(1,max_floor)
        self.dest_floor = randint(1,max_floor)
        while self.dest_floor == self.src_floor :
            self.dest_floor = randint(1,max_floor)
        self.id = Passenger.num_passengers
        Passenger.num_passengers += 1
        self.direction = "U" if self.dest_floor > self.src_floor else "D"
        self.in_elevator = False
        self.done = False

    def __str__(self):
        return str(self.id)+self.direction+"->"+str(self.dest_floor)

    def get_dest(self):
        return self.dest_floor

    def get_cur_floor(self):
        if self.in_elevator:
            return -1
        return self.dest_floor if self.done else self.src_floor

    def is_done(self):
        return self.done
