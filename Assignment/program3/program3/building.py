from passenger import Passenger
from elevator import Elevator
from time import sleep

class Building:
    def __init__(self, nf, np, d):
        self.num_floors = nf
        self.elevator = Elevator(nf)
        self.passenger_list = [Passenger(nf,d) for _ in range(np)]
        self.debug = d

    def keep_running(self):
        for p in self.passenger_list:
            if not p.is_done() :
                return True
        return False

    def vist_floor(self, floor):
        return [p for p in self.passenger_list if p.get_cur_floor() == floor and not p.is_done]

    def run(self, ver, output):
        print(self.elevator.cur_floor)
        # do the simulation
        while self.keep_running() :
            exit_list = self.elevator.want_to_exit()
            for p in exit_list:
                self.elevator.exit_pass(p)
            board_list = [p for p in self.passenger_list if p.src_floor == self.elevator.cur_floor and not p.done and p.direction == self.elevator.direction]
            for p in board_list:
                self.elevator.reg_pass(p)
            if self.debug :
                print("{},{}".format(self.elevator.cur_floor, [str(p) for p in self.elevator.register_list]))
            if ver == 1 :
                self.elevator.move()
            else:
                self.elevator.move2(self.passenger_list)
            if output:
                sleep(1)
                self.output()
        print("Moves: {}".format(self.elevator.move_count))

    def output(self):
        print('----------------------------------------------------------------------------------------------------')
        print('{:^5} {:^80} {:^5}'.format("Floor","Customers","Elevator"))
        for i in range(self.num_floors, 0, -1):
            print('----------------------------------------------------------------------------------------------------')
            print('{:^5} {:^80} {:^5}'.format(i, [str(p) for p in self.passenger_list if p.get_cur_floor() == i], "x" if self.elevator.get_cur_floor() == i else ""))
        print('----------------------------------------------------------------------------------------------------')
        print('####################################################################################################')
