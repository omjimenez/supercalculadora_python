import unittest
import supercalculadora
import test_calculadora
import test_expr_aritmetica
import expr_aritmetica


class TestsSupercalculadora(unittest.TestCase):

    def setUp(self) -> None:
        self.sc = supercalculadora.Supercalculadora(expr_aritmetica.ExprAritmetica())

    def test_sumar(self):
        self.failUnlessEqual("4", self.sc.calcular("2 + 2"))

    def test_resta(self):
        self.failUnlessEqual("0", self.sc.calcular("2 - 2"))
