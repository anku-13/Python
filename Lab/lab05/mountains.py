class Mountain :
    num_mountains = 0
    def __init__(self, name, e, p, lat, lon):
        self.name = name
        self.elevation = e
        self.prominence = p
        self.latitude = lat
        self.longitude = lon
        self.climbed = False
        Mountain.num_mountains += 1

    def __del__(self) :
        Mountain.num_mountains -= 1
        # delete other stuff?

    def mprint(self):
        print("Name: {}".format(self.name))
        print("Elevation: {}".format(self.elevation))
        print("Prominence: {}".format(self.prominence))
        print("Latitude: {}".format(self.latitude))
        print("Longitude: {}".format(self.longitude))
        print("Climbed: {}".format(self.climbed))

    def is_higher(self, m) :
        return self.elevation > m.elevation

    def climb(self) :
        self.climbed = True
