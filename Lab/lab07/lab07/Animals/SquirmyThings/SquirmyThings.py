
class SquirmyThings:
    num_squirm = 1
    def __init__(self):
        # create some member animals
        self.members = ['Worm?']

    def add_member(self, new_m):
        self.members.append(new_m)
        SquirmyThings.num_squirm += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            SquirmyThings.num_squirm -= 1
