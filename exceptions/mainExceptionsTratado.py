notas = [7.0, 8.0, 9.0, 10.0]

# exceções -> objetos especiais

try:
    while True:
        index = int(input('Digite o índice referente à nota: '))

        if index < 0:
            break

        if index == 1:
            raise FileNotFoundError('Erro na abretura do arquivo.')

        print('Nota: ', notas[index], '\n')

        # raise FileNotFoundError('Yago criou sem precisão')

        print('Nota dividindo pelo índice: ', notas[index] / index)

    print('Vamos para a próxima iteração.')

except ValueError as ve:
    print('Índice inválido. Digite um número inteiro.')
    print('Mensagem embutida', ve)
    print(ve)
except IndexError as ie:
    print(f'Erro: digite um número entre 0 e {len(notas)}.')
    print('Mensagem embutida:', ie)
except ZeroDivisionError as zde:
    print('Erro. A divisão não pode ser realizada com denominador 0.')
    print('Mensagem embutida:', zde)
except BaseException as e:
    print('Aconteceu algum problema. Nossa equipe de suporte irá resolver.')
    print('Exceção responsável', e.__class__.__name__)
    print('Mensagem da exceção:', e)
    # e.__class__.__name__ -> variável de ambiente
    # BaseException -> mãe de todas as exceções (pode ser omitido)
finally:
    print('Se ocorrer except ou não, eu entro aqui.')

print('FIM DO PROGRAMA')
