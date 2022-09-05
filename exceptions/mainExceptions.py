notas = [7.0, 8.0, 9.0, 10.0]

# exceções -> objetos especiais

while True:
    
    index = int(input('Digite o índice referente à nota: '))

    if index < 0:
        break
    if index >= (len(notas)):
        continue

    print('Nota: ', notas[index], '\n')
    
    if index == 0:
        print('Não é possível dividir a nota por 0.')
    else: 
        print('Nota dividindo pelo índice: ', notas[index] / index)
