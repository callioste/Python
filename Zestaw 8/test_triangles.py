import pytest
from triangle import Triangle
from points import Point

def test_from_points():
    pt1 = Point(2, 3)
    pt2 = Point(5, 6)
    pt3 = Point(9, 7)

    tri = Triangle.from_points((pt1, pt2, pt3))
    assert tri == Triangle(2, 3, 5, 6, 9, 7)

def test_str_triangle():
    t = Triangle(2, 3, 5, 6, 9, 7)
    assert str(t) == "[(2, 3), (5, 6), (9, 7)]"

def test_repr_triangle():
    t = Triangle(2, 3, 5, 6, 9, 7)
    assert repr(t) == "Triangle(2, 3, 5, 6, 9, 7)"

def test_eq_triangle():
    t1 = Triangle(2, 3, 5, 6, 9, 7)
    t2 = Triangle(9, 7, 2, 3, 5, 6)
    t3 = Triangle(4, 8, 3, 7, 0, -2)

    assert t1 == t2
    assert t1 != t3

def test_center_triangle():
    t = Triangle(2, 3, 5, 6, 9, 7)
    c = t.center

    assert c.x == pytest.approx(16 / 3)
    assert c.y == pytest.approx(16 / 3)

def test_area_triangle():
    t = Triangle(2, 3, 5, 6, 9, 7)
    assert t.area() == pytest.approx(4.5)

def test_move_triangle():
    t = Triangle(2, 3, 5, 6, 9, 7)
    moved = t.move(2, 2)
    assert moved == Triangle(4, 5, 7, 8, 11, 9)

def test_bounding_box_values():
    t = Triangle(4, 8, 3, 7, 0, -2)

    assert t.left == 0
    assert t.right == 4
    assert t.top == 8
    assert t.bottom == -2
    assert t.width == 4
    assert t.height == 10

def test_bounding_box_points():
    t = Triangle(4, 8, 3, 7, 0, -2)

    assert t.topleft == Point(0, 8)
    assert t.topright == Point(4, 8)
    assert t.bottomleft == Point(0, -2)
    assert t.bottomright == Point(4, -2)
