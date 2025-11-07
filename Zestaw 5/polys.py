def add_poly(poly1, poly2):
    result_poly = []
    for i in range(max(len(poly1), len(poly2))):
        coef1 = poly1[i] if i < len(poly1) else 0
        coef2 = poly2[i] if i < len(poly2) else 0
        result_poly.append(coef1 + coef2)
    return result_poly

def sub_poly(poly1, poly2):
    result_poly = []
    for i in range(max(len(poly1), len(poly2))):
        coef1 = poly1[i] if i < len(poly1) else 0
        coef2 = poly2[i] if i < len(poly2) else 0
        result_poly.append(coef1 - coef2)
    return result_poly

def mul_poly(poly1, poly2):
    result_poly = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result_poly[i+j] += poly1[i] * poly2[j]
    return result_poly

def is_zero(poly):
    return all(coef == 0 for coef in poly)

def eq_poly(poly1, poly2):
    while len(poly1) > 0 and poly1[-1] == 0:
        poly1.pop()
    while len(poly2) > 0 and poly2[-1] == 0:
        poly2.pop()
    return poly1 == poly2

def eval_poly(poly, x0):
    result = poly[-1]
    for i in range(len(poly) - 2, -1, -1):
        result = result * x0 + poly[i]
    return result

def combine_poly(poly1, poly2):
    result = [poly1[-1]]
    for i in range(len(poly1) - 2, -1, -1):
        result = mul_poly(result, poly2)
        result = add_poly(result, [poly1[i]])
    return result

def pow_poly(poly, n):
    result = [1]
    for _ in range(n):
        result = mul_poly(result, poly)
    return result

def diff_poly(poly):
    if len(poly) <= 1:
        return [0]

    result = []

    for i in range(1, len(poly)):
        result.append(i * poly[i])
    return result

# Tests

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2
        self.p3 = [0, 0, 0, 0]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])

    def test_is_zero(self):
        self.assertFalse(is_zero(self.p2))
        self.assertTrue(is_zero(self.p3))

    def test_eq_poly(self):
        self.assertFalse(eq_poly(self.p1, self.p2))
        self.assertTrue(eq_poly(self.p1, self.p1))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 3), 3)
        self.assertEqual(eval_poly(self.p2, 3), 9)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p2, 3), [0, 0, 0, 0, 0, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])
        self.assertEqual(diff_poly(self.p2), [0,2])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()