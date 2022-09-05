from typing import List


class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list) -> None:
        self.__matricula = matricula
        self.__nome = nome
        self.__notas: List[float] = notas

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.__nome = novoNome

    @property
    def matricula(self) -> str:
        return f'Matrícula de {self.__nome}: {self.__matricula}'

    def adicionarNota(self, nota: float) -> None:
        self.__notas.append(nota)

    def media(self) -> float:
        somaNotas = sum(self.__notas)
        quantidadeDeNotas = len(self.__notas)
        mediaNotas = somaNotas / quantidadeDeNotas
        return mediaNotas
