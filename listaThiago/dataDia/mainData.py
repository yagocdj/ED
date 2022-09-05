from data import Data

dataDeHoje = Data(22, 8, 2022)

print(dataDeHoje)

print(dataDeHoje.dia)
print(dataDeHoje.mes)
print(dataDeHoje.ano)

dataDeHoje.dia = 25
dataDeHoje.mes = 12
dataDeHoje.ano = 2022

print(dataDeHoje)
