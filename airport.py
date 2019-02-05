class Airport:

    def __init__(self):
        self.hangar = []

    def permit_landing(self, plane):
        self.hangar.append(plane)

    def permit_takeoff(self, plane):
        self.hangar.remove(plane)
