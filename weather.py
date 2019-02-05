import random

class Weather:

    def isStormy(self, status = False):
        if status is False: status = random.choice([True, False])
        return 'stormy' if status == True else 'sunny'
