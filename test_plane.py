import unittest
from mock import Mock
from plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.airport = Mock()
        self.plane = Plane()

    def test_flyingStatus_is_true_on_init(self):
        self.assertTrue(self.plane.flyingStatus)

    def test_land_change_flyingStatus_to_false(self):
        self.plane.land()
        self.assertFalse(self.plane.flyingStatus)

    def test_takeoff_change_flyingStatus_to_true(self):
        self.plane.land()
        self.plane.takeoff()
        self.assertTrue(self.plane.flyingStatus)

    def test_plane_cannot_takeoff_if_flying(self):
        with self.assertRaisesRegexp(Exception, 'Plane is not in the hangar'):
            self.plane.takeoff()

if __name__ == '__main__':
    unittest.main()
