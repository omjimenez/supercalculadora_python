import unittest
import supercalculadora

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

if __name__ == "__main__":
    unittest.main()