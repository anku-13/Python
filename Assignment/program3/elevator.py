from random import randint
from passenger import Passenger

class Elevator:

    def __init__(self, nf):
        self.num_floors = nf
        self.cur_floor = randint(1, nf)
        self.direction = "U"
        self.register_list = []
        self.move_count = 0
        # self.stops = 0

    def move(self):
        self.move_count += 1
        if self.direction == "U":
            self.cur_floor += 1
            if self.cur_floor >= self.num_floors:
                self.direction = "D"
        else:
            self.cur_floor -= 1
            if self.cur_floor <= 1:
                self.direction = "U"

    def move2(self, all_pass):
        self.move_count += 1
        if self.direction == "U":
            self.cur_floor += 1
            # start moving donwn if no one above and no one wants to go up
            if self.cur_floor >= self.num_floors:
                self.direction = "D"
        else:
            self.cur_floor -= 1
            # start moving up if no one below and no one wants to go below
            if self.cur_floor <= 1 or ():
                self.direction = "U"

    def reg_pass(self, passenger):
        self.register_list.append(passenger)
        passenger.in_elevator = True

    def exit_pass(self, passenger):
        self.register_list.remove(passenger)
        passenger.in_elevator = False
        passenger.done = True

    def want_to_exit(self):
        return [p for p in self.register_list if p.dest_floor == self.cur_floor]

    def get_cur_floor(self):
        return self.cur_floor

    def continue_up(self, all_pass) :
        for p in self.register_list:
            if p.dest_floor > self.get_cur_floor :
                return True
        # for p in self.all_pass
