from typing import Any


class No:
    def __init__(self, carga: Any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return f'{self.carga}'
