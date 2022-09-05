class ContaCorrente:
    def __init__(self, numeroConta: int, saldoConta: float, nomeDoTitular: str) -> None:
        self.__numeroConta = numeroConta
        self.__saldo = saldoConta
        self.__nomeDoTitular = nomeDoTitular

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def numeroConta(self) -> int:
        return self.__numeroConta

    def sacarDinheiro(self, quantiaSaque: float) -> bool:
        if self.__saldo >= quantiaSaque:
            self.__saldo -= quantiaSaque
            return True
        return False

    def depositarDinheiro(self, quantiaDeposito: float) -> None:
        self.__saldo += quantiaDeposito

    def __str__(self) -> str:
        return f'Número: {self.__numeroConta}\nSaldo: R${self.__saldo:.2f}\nTitular: {self.__nomeDoTitular}'
