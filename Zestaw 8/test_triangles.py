import unittest
from triangle import Triangle
from points import Point

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(2, 3, 5, 6, 9, 7)
        self.t2 = Triangle(9, 7, 2, 3, 5, 6)
        self.t3 = Triangle(4,8, 3, 7, 0, -2)

    def test_from_points(self):
        self.pt1 = Point(2, 3)
        self.pt2 = Point(5, 6)
        self.pt3 = Point(9, 7)

        self.assertTrue(Triangle.from_points((self.pt1, self.pt2, self.pt3)) == self.t1)

    def test_str_triangle(self):
        self.assertEqual(str(self.t1), '[(2, 3), (5, 6), (9, 7)]')

    def test_repr_triangle(self):
        self.assertEqual(repr(self.t1), "Triangle(2, 3, 5, 6, 9, 7)")

    def test_eq_triangle(self):
        self.assertTrue(self.t1 == self.t2)
        self.assertFalse(self.t1 == self.t3)

    def test_ne_triangle(self):
        self.assertTrue(self.t2 != self.t3)
        self.assertFalse(self.t2 != self.t1)

    def test_center_triangle(self):
        c = self.t1.center
        self.assertAlmostEqual(c.x, 16 / 3)
        self.assertAlmostEqual(c.y, 16 / 3)

    def test_area_triangle(self):
        self.assertAlmostEqual(self.t1.area(), 4.5)

    def test_move_triangle(self):
        moved = self.t1.move(2, 2)
        self.assertEqual(moved, Triangle(4, 5, 7, 8, 11, 9))

    def test_bounding_box_values(self):
        self.assertEqual(self.t3.left, 0)
        self.assertEqual(self.t3.right, 4)
        self.assertEqual(self.t3.top, 8)
        self.assertEqual(self.t3.bottom, -2)
        self.assertEqual(self.t3.width, 4)
        self.assertEqual(self.t3.height, 10)

    def test_bounding_box_points(self):
        self.assertEqual(self.t3.topleft, Point(0, 8))
        self.assertEqual(self.t3.topright, Point(4, 8))
        self.assertEqual(self.t3.bottomleft, Point(0, -2))
        self.assertEqual(self.t3.bottomright, Point(4, -2))
