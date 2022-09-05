class Data:
    def __init__(self, dia: int, mes: int, ano: int) -> None:
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        # Janeiro -> 1, Fevereiro -> 2, ... , Dezembro -> 12.
        self.__diasDoMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __str__(self) -> str:
        return f'Data: {self.__dia:02d}/{self.__mes:02d}/{self.__ano}'

    @property
    def dia(self) -> int:
        return self.__dia

    @dia.setter
    def dia(self, novoDia: int) -> None:
        mesAtual = self.__mes
        if ((novoDia > 0) and (novoDia <= self.__diasDoMes[mesAtual])):
            self.__dia = novoDia

    @property
    def mes(self) -> int:
        return self.__mes

    @mes.setter
    def mes(self, novoMes: int) -> None:
        if (novoMes >= 1 and novoMes <= 12):
            self.__mes = novoMes

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, novoAno: int) -> None:
        self.__ano = novoAno
