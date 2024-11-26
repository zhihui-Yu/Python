import unittest

from Test.test_exercise import str_to_bool


class TestAssertions(unittest.TestCase):
    def test_equals(self):
        self.assertEqual("one string", "one string")

class TestStrToBool(unittest.TestCase):
    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)
    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)


if __name__ == '__main__':
    unittest.main()