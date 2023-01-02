import unittest
import supercalculadora
import expr_aritmetica

class TestsSupercalculadora( unittest.TestCase):

    def setUp(self):
        self.calc = supercalculadora.Supercalculadora()

    def tearDown(self):
        pass

    def test_sumar_2_y_2(self):
        self.failUnlessEqual(4, self.calc.sumar(2, 2))
    
    def test_sumar_5_y_7(self):
        self.failUnlessEqual(12, self.calc.sumar(5, 7))

    def test_sumar_propiedad_conmutativa(self):
        self.failUnlessEqual(self.calc.sumar(5, 7), self.calc.sumar(7, 5))

    def test_restar_5_y_3(self):
        self.failUnlessEqual(2, self.calc.restar(5, 3))

    def test_restar_2_y_3(self):
        self.failUnlessEqual(-1, self.calc.restar(2, 3))

    def test_restar_no_propiedad_conmutativa(self):
        self.failIfEqual(self.calc.restar(5, 3), self.calc.restar(3, 5))

    def test_extraer_operandos_y_operandores_en_2_mas_2(self):
        expresion = expr_aritmetica.ExprAritmetica()
        self.failUnlessEqual({'Operandos':[2, 2] , 'Operadores': ['+']},
                                expresion.parse("2 + 2"))

if __name__ == "__main__":
    unittest.main()