import unittest
from quadtree import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.x1 = 11
        self.y1 = -21
        self.point1 = Point(self.x1, self.y1, payload=None)

        self.x2 = -33
        self.y2 = 49
        self.point2 = Point(self.x2, self.y2, payload=None)

        self.euclid_dist_p1_p2 = 82.6801
    
    def test_init_x_y(self):        
        self.assertIsInstance(self.point1.x, float)
        self.assertIsInstance(self.point1.y, float)
        self.assertEqual(self.point1.x, self.x1)
        self.assertEqual(self.point1.y, self.y1)
        self.assertEqual(self.point1.payload, None)

    def test_points_string(self):
        self.assertEqual(str(self.point1), f'P({self.x1:.2f}, {self.y1:.2f})')
        self.assertEqual(str(self.point2), f'P({self.x2:.2f}, {self.y2:.2f})')

    def test_points_repr(self):
        self.assertEqual(repr(self.point1), f'P({self.x1:.2f}, {self.y1:.2f}): {self.point1.payload}')
        self.assertEqual(repr(self.point2), f'P({self.x2:.2f}, {self.y2:.2f}): {self.point2.payload}')
    
    def test_p1_distanace_p2(self):
        self.assertAlmostEqual(self.point1.distance_to(self.point2), self.euclid_dist_p1_p2, 3)


if __name__ == "__main__":
    unittest.main()