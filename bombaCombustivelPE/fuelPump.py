def mudarPrecoCombustivel(novo_preco):
    return novo_preco


def exibirPrecoCombustivel(escolha_combustivel):
    print(f'Preço por litro: R${escolha_combustivel:.2f}')


def calcularValorTotal(litros_abastecidos, tipo_combustivel):
    if tipo_combustivel == 'alcool':
        valorToltal = litros_abastecidos * tipo_combustivel
    else:
        valorToltal = litros_abastecidos * tipo_combustivel
    return valorToltal
