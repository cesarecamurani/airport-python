from plane import Plane
from weather import Weather

class Airport:

    def __init__(self):
        self.hangar = []

    def permit_landing(self, plane):
        plane.land()
        self.hangar.append(plane)

    def permit_takeoff(self, plane):
        if plane not in self.hangar:
            raise Exception('Plane is not in the hangar')
        plane.takeoff()
        self.hangar.remove(plane)
