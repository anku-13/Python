class Character:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.evil_count = 0

    def increment_evil(self):
        self.evil_count+=1

    def get_evil(self):
        return self.evil_count

    def get_name(sef):
        return self.first_name+" "+self.last_name

    def __str__(self) :
        return self.first_name+" "+self.last_name+" "+str(self.evil_count)
