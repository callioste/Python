from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        for value in (x1, y1, x2, y2, x3, y3):
            if not isinstance(value, (int, float)):
                raise ValueError("Triangle coordinates must be numbers.")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        if self.area() == 0:
            raise ValueError("Triangle cannot be degenerate (three points are collinear).")

    @classmethod
    def from_points(cls, pts):
        if len(pts) != 3:
            raise ValueError("Wrong number of vertices. To create a triangle you need exactly 3 vertices.")

        p1, p2, p3 = pts
        return cls(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):
       return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

    def __ne__(self, other):
        return not self == other

    @property
    def center(self):
        s = self.pt1 + self.pt2 + self.pt3
        return Point(s.x / 3, s.y / 3)

    def area(self):
        return abs((self.pt2 - self.pt1).cross(self.pt3 - self.pt1)) / 2

    def move(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("move() requires numeric x and y.")

        v = Point(x, y)
        p1 = self.pt1 + v
        p2 = self.pt2 + v
        p3 = self.pt3 + v
        return Triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

