from unittest import TestCase, main
from lesson.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2 + 2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3 - 1'), 2)

    def test_nulti(self):
        self.assertEqual(calculator('3 * 3'), 9)

    def test_divide(self):
        self.assertEqual(calculator('6 / 2'), 3.0)


if __name__ == '__main__':
    main()
