import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        # Позитивный тест умножения числа на число
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        # Позитивный тест деления числа на число
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self):
        # Позитивный тест вычитания одного числа из другого
        assert self.calc.subtraction(self, 10, 3) == 7

    def test_adding_calculate_correctly(self):
        # Позитивный тест сложения двух чисел
        assert self.calc.adding(self, 2, 1) == 3

    def teardown(self):
        print("Выполнение метода Teardown")
