import expr_aritmetica
import calculadora

class Supercalculadora:
    def __init__(self, parser):
        self.calc = calculadora.Calculadora()
        self.parser = parser


    def calcular(self, expression):
        expr_descompuesta = self.parser.parse(expression)
        if expr_descompuesta['operadores'][0] == '+':
            return str(self.calc.sumar(
                expr_descompuesta['operandos'][0],
                expr_descompuesta['operandos'][1]))
        elif expr_descompuesta['operadores'][0] == '-':
            return str(self.calc.restar(
                expr_descompuesta['operandos'][0],
                expr_descompuesta['operandos'][1]))

