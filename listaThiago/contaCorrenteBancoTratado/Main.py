from Conta import Conta
from Banco import *

try:
    bco = Banco()
    bco.addConta(123, 'Alex')
    bco.addConta(456, 'Clodoaldo')
    bco.addConta(457, 'Yago')
    bco.addConta(458, 'Márcio')
    bco.addConta(120, 'Caio')
    bco.addConta(121, 'Felipe')

    bco.sacar(456, 10.00)
    bco.depositar(123, -1000.0)

except OperacaoInvalidaException as oie:
    print(oie)

print(bco)
