import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):        # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(pow(self.x,2) + pow(self.y,2))

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(2, 3)
        self.p2 = Point(7,5)

    def test_str_point(self):
        self.assertEqual(str(self.p1), "(2, 3)")

    def test_repr_point(self):
        self.assertEqual(repr(self.p2), "Point(7, 5)")

    def test_eq_point(self):
        self.assertTrue(self.p1 == self.p1)
        self.assertFalse(self.p1 == self.p2)

    def test_ne_point(self):
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p2 != self.p2)

    def test_add_point(self):
        self.assertEqual(self.p1 + self.p2, Point(9, 8))

    def test_sub_point(self):
        self.assertEqual(self.p1 - self.p2, Point(-5, -2))

    def test_mul_point(self):
        self.assertEqual(self.p1 * self.p2, 29)

    def test_cross_point(self):
        self.assertEqual(self.p1.cross(self.p2), -11)

    def test_length_point(self):
        self.assertEqual(self.p1.length(), math.sqrt(13))