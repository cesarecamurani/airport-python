class Airport:

    def __init__(self):
        self.hangar = []

    def permit_landing(self, plane):
        self.hangar.append(plane)
