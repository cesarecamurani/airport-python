import unittest
from weather import Weather

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_stormy_is_false_on_init(self):
        self.assertFalse(self.weather.stormy)

    def test_check_if_is_stormy(self):
        self.weather.isStormy()
        self.assertTrue(self.weather.stormy)



if __name__ == '__main__':
    unittest.main()
