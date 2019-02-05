class Weather:

    def __init__(self):
        self.stormy = False
        self.forecast = 'Sunny'

    def isStormy(self):
        self.stormy = True
        self.forecast = 'Stormy'
