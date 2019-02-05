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

    def test_permit_takeoff_calls_plane_takeoff(self):
        self.airport.permit_landing(self.plane)
        self.airport.permit_takeoff(self.plane)
        self.plane.takeoff.assert_called_with()

    def test_takeoff_not_allowed_if_plane_not_in_hangar(self):
        with self.assertRaisesRegexp(Exception, 'Plane is not in the hangar'):
            self.airport.permit_takeoff(self.plane)

if __name__ == '__main__':
    unittest.main()
