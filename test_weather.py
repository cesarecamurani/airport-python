import unittest
from weather import Weather

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_isStormy(self):
        assert self.weather.isStormy(True) == 'stormy'

if __name__ == '__main__':
    unittest.main()
