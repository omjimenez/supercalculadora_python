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

    def test_expresion_compleja_sin_parentisis_sin_precedencia(self):
        self.failUnlessEqual("6", self.sc.calcular("5 + 4 - 3"))

    # def test_expresion_compleja_sin_paretensis_con_precedencia(self):
    #     self.failUnlessEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))
