from typing import List


class Pais:
    def __init__(self, nome: str, capital: str, dimensao: float) -> None:
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao  # em km²
        self.__vizinhos: List[str] = list()

    def __str__(self) -> str:
        return f'{self.__nome}, capital {self.__capital}, {self.__dimensao}km².'

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def capital(self) -> str:
        return self.__capital

    @property
    def dimensao(self) -> float:
        return self.__dimensao

    @property
    def vizinhos(self) -> List[str]:
        return self.__vizinhos

    # O setter altera o conteúdo daquela propriedade. Neste caso, só queremos adicionar um país
    def addPaisDeFronteira(self, nomeDoPais: str) -> None:
        if nomeDoPais not in self.__vizinhos:
            self.__vizinhos.append(nomeDoPais)
