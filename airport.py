from plane import Plane

class Airport:

    def __init__(self):
        self.hangar = []

    def permit_landing(self, plane):
        plane.land()
        self.hangar.append(plane)

    def permit_takeoff(self, plane):
        self.hangar.remove(plane)
