class Paciente:
    def __init__(self, nome:str, cpf:str, plano_de_saude:str, id_number:int) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__plano = plano_de_saude
        self.__id = id_number

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def plano(self) -> str:
        return self.__plano

    @property
    def id_number(self) -> int:
        return self.__id

    def __str__(self) -> str:
        return f'ID: {self.id_number}, Nome: {self.nome}, CPF: {self.cpf}, Plano de saúde: {self.plano}.'
