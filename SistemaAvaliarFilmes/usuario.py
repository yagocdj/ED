class Usuario:
    # construtor
    def __init__(self, id, nome, logado, email):
        self.id = id
        self.nome = nome
        self.logado = logado
        self.email = email

    def __str__(self):
        return f'{self.id}-{self.nome}, {self.email}'
