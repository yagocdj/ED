import fuelPump

escolhaCombustivel = input(
    '''Informe o combustível que você deseja abastecer
    ("alcool" ou "gasolina"):''').lower()

precoGasolina = 0.0
precoAlcool = 0.0

if escolhaCombustivel == 'alcool':
    precoAlcool = float(input('Preço atual do álcool em reais: '))
else:
    precoGasolina = float(input('Preço atual da gasolina em reais: '))

litrosAbastecidos = int(
    input(f'Informe quantos Litros de {escolhaCombustivel} vai abastecer: '))

valorTotal = fuelPump.calcularValorTotal(litrosAbastecidos, escolhaCombustivel)
print(f'Você abasteceu {litrosAbastecidos}L de {escolhaCombustivel}.')
print(f'Isso lhe custou R${valorTotal:.2f}')
