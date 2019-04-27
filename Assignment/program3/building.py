from passenger import Passenger
from elevator import Elevator
from time import sleep

class Building:
    def __init__(self, nf, np):
        self.num_floors = nf
        self.elevator = Elevator(nf)
        self.passenger_list = [Passenger(nf) for _ in range(np)]

    def keep_running(self):
        for p in self.passenger_list:
            if not p.is_done() :
                return True
        return False

    def vist_floor(self, floor):
        return [p for p in self.passenger_list if p.get_cur_floor() == floor and not p.is_done]

    def run(self):
        print(self.elevator.cur_floor)
        # do the simulation
        while self.keep_running() :
            exit_list = self.elevator.want_to_exit()
            for p in exit_list:
                self.elevator.exit_pass(p)
            board_list = [p for p in self.passenger_list if p.src_floor == self.elevator.cur_floor and not p.done and p.direction == self.elevator.direction]
            for p in board_list:
                self.elevator.reg_pass(p)

            print("{},{}".format(self.elevator.cur_floor, [str(p) for p in board_list]))
            self.elevator.move()
            sleep(1)
            self.output()

    def output(self):
        print('----------------------------------------------------------------------------------------------------')
        print('{:^5} {:^80} {:^5}'.format("Floor","Customers","Elevator"))
        for i in range(self.num_floors, 0, -1):
            print('----------------------------------------------------------------------------------------------------')
            print('{:^5} {:^80} {:^5}'.format(i, [str(p) for p in self.passenger_list if p.get_cur_floor() == i], "x" if self.elevator.get_cur_floor() == i else ""))
        print('----------------------------------------------------------------------------------------------------')
        print('####################################################################################################')
