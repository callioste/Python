from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):   # obsługa tr1 == tr2
       return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

       # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
       # niezależnie od kolejności pt1, pt2, pt3.


    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca środek (masy) trójkąta
        s = self.pt1 + self.pt2 + self.pt3
        return Point(s.x / 3, s.y / 3)

    def area(self):             # pole powierzchni
        return abs((self.pt2 - self.pt1).cross(self.pt3 - self.pt1)) / 2

    def move(self, x, y):
        v = Point(x, y)
        p1 = self.pt1 + v
        p2 = self.pt2 + v
        p3 = self.pt3 + v
        return Triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(2, 3, 5, 6, 9, 7)
        self.t2 = Triangle(9, 7, 2, 3, 5, 6)
        self.t3 = Triangle(4,8, 3, 7, 0, -2)

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
        c = self.t1.center()
        self.assertAlmostEqual(c.x, 16 / 3)
        self.assertAlmostEqual(c.y, 16 / 3)

    def test_area_triangle(self):
        self.assertAlmostEqual(self.t1.area(), 4.5)

    def test_move_triangle(self):
        moved = self.t1.move(2, 2)
        self.assertEqual(moved, Triangle(4, 5, 7, 8, 11, 9))
