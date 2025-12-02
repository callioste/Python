from math import gcd

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):

        if y == 0:
            raise ValueError("Mianownik nie może być równy 0.")

        if isinstance(x, float):
            num, den = x.as_integer_ratio()
            x = num
            y = y * den

        if isinstance(y, float):
            num, den = y.as_integer_ratio()
            x = x * den
            y = num

        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Ułamek musi składać się z liczb.")

        self.x = x
        self.y = y

        self.normalize()

    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return f'{self.x}'
        else:
            return f'{self.x}/{self.y}'

    def __repr__(self):         # zwraca "Frac(x, y)"
        return f'Frac({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, Frac):
            other = Frac(other)

        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Frac):
            other = Frac(other)

        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        if not isinstance(other, Frac):
            other = Frac(other)

        return self.x * other.y <= other.x * self.y

    def __add__(self, other):   # frac1+frac2, frac+int
        if not isinstance(other, Frac):
            other = Frac(other)

        return Frac(self.x * other.y + other.x * self.y, self.y * other.y).normalize()

    __radd__ = __add__              # int+frac

    def __sub__(self, other):   # frac1-frac2, frac-int
        if not isinstance(other, Frac):
            other = Frac(other)

        return Frac(self.x * other.y - other.x * self.y, self.y * other.y).normalize()

    def __rsub__(self, other):      # int-frac
        if not isinstance(other, Frac):
            other = Frac(other)
        return other.__sub__(self)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if not isinstance(other, Frac):
            other = Frac(other)

        return Frac(self.x * other.x, self.y * other.y).normalize()

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):   # frac1/frac2, frac/int, Py2
        if not isinstance(other, Frac):
            other = Frac(other)

        return self.__mul__(~other)

    def __rdiv__(self, other): # int/frac, Py2
        if not isinstance(other, Frac):
            other = Frac(other)
        return other.__div__(self)


    def __truediv__(self, other):  # frac1/frac2, frac/int, Py3
        if not isinstance(other, Frac):
            other = Frac(other)
        return Frac(self.x * other.y, self.y * other.x).normalize()

    def __rtruediv__(self, other):   # int/frac, Py3
        if not isinstance(other, Frac):
            other = Frac(other)
        return other.__truediv__(self)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):         # -frac = (-1)*frac
        return self.__mul__(-1)

    def __invert__(self):      # odwrotnosc: ~frac
        return Frac(self.y, self.x).normalize()

    def __float__(self):        # float(frac)
        return float(self.x / self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs

    def normalize(self):
        if self.y < 0:
            self.x = -self.x
            self.y = -self.y
        g = gcd(self.x, self.y)

        self.x //= g
        self.y //= g

        return self

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.f1 = Frac(2, 3)
        self.f2 = Frac(3, 4)
        self.f3 = Frac(4, 1)

    # --- Testy podstawowe ---

    def test_str(self):
        self.assertEqual(str(self.f1), "2/3")
        self.assertEqual(str(self.f3), "4")

    def test_repr(self):
        self.assertEqual(repr(self.f1), "Frac(2, 3)")

    # --- Testy ValueError ---

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Frac(1, 0)

    def test_invalid_types(self):
        with self.assertRaises(ValueError):
            Frac("a", 5)
        with self.assertRaises(ValueError):
            Frac(1, "b")

    # --- Testy porównań ---

    def test_eq_frac(self):
        self.assertTrue(self.f1 == Frac(2, 3))
        self.assertFalse(self.f1 == self.f2)

    def test_neq_frac(self):
        self.assertTrue(self.f1 != self.f2)
        self.assertFalse(self.f1 != Frac(2, 3))

    def test_lt_frac(self):
        self.assertTrue(self.f1 < self.f2)

    def test_le_frac(self):
        self.assertTrue(self.f1 <= self.f2)
        self.assertTrue(self.f1 <= Frac(2, 3))

    # --- Testy działań arytmetycznych ---

    def test_add_frac(self):
        self.assertEqual(self.f1 + self.f2, Frac(17, 12))

    def test_add_int(self):
        self.assertEqual(self.f1 + 1, Frac(5, 3))
        self.assertEqual(1 + self.f1, Frac(5, 3))

    def test_sub_frac(self):
        self.assertEqual(self.f1 - self.f2, Frac(-1, 12))

    def test_sub_int(self):
        self.assertEqual(self.f1 - 1, Frac(-1, 3))
        self.assertEqual(1 - self.f1, Frac(1, 3))

    def test_mul_frac(self):
        self.assertEqual(self.f1 * self.f2, Frac(1, 2))

    def test_mul_int(self):
        self.assertEqual(self.f1 * 2, Frac(4, 3))
        self.assertEqual(2 * self.f1, Frac(4, 3))

    def test_div_frac(self):
        self.assertEqual(self.f1 / self.f2, Frac(8, 9))

    def test_div_int(self):
        self.assertEqual(self.f1 / 2, Frac(1, 3))
        self.assertEqual(2 / self.f1, Frac(3, 1))

    # --- Testy floatów ---

    def test_float_cast(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertAlmostEqual(float(Frac(2, 3)), 2/3)

    def test_float_in_constructor(self):
        self.assertEqual(Frac(0.75, 1), Frac(3, 4))
        self.assertEqual(Frac(1, 0.25), Frac(4, 1))

    def test_float_operations(self):
        self.assertEqual(self.f1 + 0.5, Frac(2, 3) + Frac(1, 2))
        self.assertEqual(self.f1 * 0.5, Frac(2, 3) * Frac(1, 2))
        self.assertEqual(0.5 * self.f1, Frac(1, 2) * Frac(2, 3))

    # --- Operatory jednoargumentowe ---

    def test_pos(self):
        self.assertEqual(+self.f1, self.f1)

    def test_neg(self):
        self.assertEqual(-self.f1, Frac(-2, 3))

    def test_invert(self):
        self.assertEqual(~self.f1, Frac(3, 2))
