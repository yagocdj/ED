from conta import ContaCorrente

conta1 = ContaCorrente(10, 1000.0, 'Fulano')
conta2 = ContaCorrente(11, 2000.0, 'Sicrano')

listaContas = [conta1, conta2]

sacou = listaContas[1].sacarDinheiro(5000.0)

print(sacou)
