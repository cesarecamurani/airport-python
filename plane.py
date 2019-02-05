class Plane:

    def __init__(self):
        self.flyingStatus = True

    def land(self):
        self.flyingStatus = False

    def takeoff(self):
        self.flyingStatus = True
