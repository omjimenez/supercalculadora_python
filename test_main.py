import unittest
import test_calculadora
import test_expr_aritmetica


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_calculadora.TestsCalculadora))
    
    suite.addTest(unittest.makeSuite(test_expr_aritmetica.TestsExprAritmetica))

    unittest.TextTestRunner(verbosity=3).run(suite)