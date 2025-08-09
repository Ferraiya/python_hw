import pytest

from calculator import *


class TestMath:

    def test_addition(self):
        assert add(17.7, -33876987.239) == -33876969.539

    def test_substraction(self):
        assert substract(0, -5) == 5

    def test_multiplying(self):
        assert multiply(3, 0) == 0

    def test_division(self):
        assert divide(-1468.999, -0.25) == 5875.996

    def test_divide_by_zero(self):
        with pytest.raises(ValueError) as exc_info:
            divide(5, 0)
        assert str(exc_info.value) == "На нуль ділити не можна!"

    def test_adding_symbol(self):
        with pytest.raises(TypeError) as type_info:
            add(5, "!")
        assert str(type_info.value) == "Можна додавати тільки числа!"

    def test_adding_nothing(self):
        with pytest.raises(TypeError) as type_info:
            add(5, "")
        assert str(type_info.value) == "Можна додавати тільки числа!"

    def test_multiply_with_comma(self):
        with pytest.raises(TypeError) as type_info:
            multiply(5,"5,5")
        assert str(type_info.value) == "Можна множити тільки числа!"

    def test_divide_with_dot(self):
        with pytest.raises(TypeError) as type_info:
            divide("957.5", 7.8)
        assert str(type_info.value) == "Можна ділити тільки числа!"
