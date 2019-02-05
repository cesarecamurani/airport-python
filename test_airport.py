import unittest
from mock import Mock
from airport import Airport

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Mock()

    def test_airport_has_an_hangar(self):
        airport = Airport()
        assert airport.hangar == []

    def test_permit_landing(self):
        self.airport.permit_landing(self.plane)
        self.assertIn(self.plane, self.airport.hangar)

    

if __name__ == '__main__':
    unittest.main()
