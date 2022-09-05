from typing import Any, Dict


class Calculadora:
    def __init__(self) -> None:
        self.__registrador: Dict[str, Any] = {'Atual': 0.0,
                                              'Anterior': 0.0}

    def adicionar(self, valorSoma: float) -> None:
        self.__registrador['Anterior'] = self.__registrador.get('Atual')
        self.__registrador['Atual'] += valorSoma

    def subtrair(self, valorSubtracao) -> None:
        self.__registrador['Anterior'] = self.__registrador.get('Atual')
        self.__registrador['Atual'] -= valorSubtracao

    def dividr(self, valorDivisao) -> None:
        # valorDivisao deve ser diferente de zero
        try:
            assert valorDivisao != 0
            self.__registrador['Anterior'] = self.__registrador.get('Atual')
            self.__registrador['Atual'] /= valorDivisao
        except AssertionError:
            self.__registrador['Atual'] = 0.0
            raise ZeroDivisionError('Error: o denominador não pode ser zero.')

    def multiplicar(self, valorMultiplicacao) -> None:
        self.__registrador['Anterior'] = self.__registrador.get('Atual')
        self.__registrador['Atual'] *= valorMultiplicacao

    def reset(self) -> None:
        self.__registrador['Anterior'] = 0.0
        self.__registrador['Atual'] = 0.0

    def undo(self):
        self.__registrador['Atual'] = self.__registrador.get('Anterior')

    def __str__(self):
        return f"Valor atual do registrador: {self.__registrador['Atual']}"


if __name__ == '__main__':

    try:
        calc = Calculadora()
        print(calc)
        calc.adicionar(10.0)
        print(calc)
        calc.reset()
        calc.adicionar(10.0)
        print(calc)
        calc.adicionar(100.0)
        print(calc)
        calc.reset()
        calc.adicionar(20.0)
        calc.dividr(0.0)

    except ZeroDivisionError as ae:
        print(ae)
