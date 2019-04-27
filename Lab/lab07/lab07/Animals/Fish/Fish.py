
class Fish:
    num_fish = 3
    def __init__(self):
        # create some member animals
        self.members = ['Carp', 'Catfish', 'Sun Fish']

    def add_member(self, new_m):
        self.members.append(new_m)
        Fish.num_fish += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            Fish.num_fish -= 1
