import expr_aritmetica
import calculadora

class Supercalculadora:
    def __init__(self, parser):
        self.calc = calculadora.Calculadora()
        self.parser = parser


    def calcular(self, expression):
        expr_descompuesta = self.parser.parse(expression)
        res = 0
        for i in range(len(expr_descompuesta['operadores'])):
            if i == 0:
                res = expr_descompuesta['operandos'][0]
            
            if expr_descompuesta['operadores'][i] == '+':
                res = self.calc.sumar(res, expr_descompuesta['operandos'][i + 1])

            elif expr_descompuesta['operadores'][i] == '-':
                res = self.calc.restar(res, expr_descompuesta['operandos'][i + 1])
        
        return str(res)

