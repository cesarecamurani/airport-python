class Plane:

    def __init__(self):
        self.flyingStatus = True

    def land(self):
        self.flyingStatus = False

    def takeoff(self):
        if self.flyingStatus == True:
            raise Exception('Plane is not in the hangar')
        self.flyingStatus = True
