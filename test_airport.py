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

    def test_permit_takeoff(self):
        self.airport.permit_landing(self.plane)
        self.airport.permit_takeoff(self.plane)
        self.assertNotIn(self.plane, self.airport.hangar)

    def test_permit_landing_calls_plane_land(self):
        self.airport.permit_landing(self.plane)
        self.plane.land.assert_called_with()

if __name__ == '__main__':
    unittest.main()
