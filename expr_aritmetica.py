import string

class ExprAritmetica:
    def __es_numero__(self, cadena):
        try:
           int(cadena)
           return True
        except ValueError:
            return False

    def parse( self, exp):
        operandos = []
        operadores = []
        tokens = exp.split()

        for token in tokens:
            if self.__es_numero__(token):
                operandos.append(int(token))
            else:
                operadores.append(token)
        return {'operandos': operandos, 'operadores': operadores}