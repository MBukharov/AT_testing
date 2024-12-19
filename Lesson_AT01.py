import unittest

def residue(a,b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a % b


class TestMath(unittest.TestCase):
    def test_value(self):
        self.assertEqual(residue(7, 5),2)

    def test_raise(self):
        self.assertRaises(ValueError,residue,4,0)

if __name__ == '__name__':
    unittest.main()
