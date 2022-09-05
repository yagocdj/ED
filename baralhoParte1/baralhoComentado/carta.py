class Carta:
    # construtor -> método especial invocado automaticamente ao instanciar um objeto na memória
    # self -> primeiro argumento em cada método
    def __init__(self, valor, naipe, cor):
        # definir as propriedades da classe
        # __ -> deixar o atributo privado
        self.__naipe = naipe # atributo de instância = propriedade
        self.__valor = valor
        self.__cor = cor

    def getValor(self):
        return self.__valor

    def getNaipe(self):
        return self.__naipe
    
    def getCor(self):
        return self.__cor

    # método especial para formatar uma saída no formato string do jeito que eu quiser
    def __str__(self):
        return f'{self.__valor} de {self.__naipe}'
        