import unittest
from mock import Mock
from plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.airport = Mock()
        self.plane = Plane()

    def test_flyingStatus_is_true_on_init(self):
        self.assertTrue(self.plane.flyingStatus)

if __name__ == '__main__':
    unittest.main()
