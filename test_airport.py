import unittest
from airport import Airport

class TestAirport(unittest.TestCase):

    def test_airport_has_an_hangar(self):
        airport = Airport()
        assert airport.hangar == []


if __name__ == '__main__':
    unittest.main()
