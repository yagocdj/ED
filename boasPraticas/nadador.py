class Nadador:
    def __init__(self, nome: str, tempo: float) -> None:
        self.__nome = nome
        self.__tempo = tempo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def tempo(self) -> float:
        return self.__tempo


if __name__ == "__main__":
    nadadores = [Nadador('Nayara', 37.025), Nadador(
        'Alex', 36.128), Nadador('Matheus', 36.321), Nadador('Yago', 35.040)]
    for atleta in nadadores:
        print(atleta.nome)
        print(atleta.tempo)
