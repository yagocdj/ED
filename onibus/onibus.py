class Onibus:
    def __init__(self, lugares, marca):
        self.lugares = lugares
        self.marca = marca
        self.velocidade = 0
        self.direcao = 0
        # 0: reto, 1: esq, 2: dir

    def acelerar(self, valor):
        self.velocidade = valor

    def frear(self):
        self.velocidade = 0

    def buzinar(self):
        print('Bi Biiiiiiii')
