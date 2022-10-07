def clone(self) -> 'Pilha':
    pclone = Pilha()
    for posicao in range(1, len(self) + 1):
        pclone.empilha(self.elemeto(posicao))
    return pclone

