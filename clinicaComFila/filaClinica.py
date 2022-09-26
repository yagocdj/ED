from filaSequencialCircular import *
from Paciente import Paciente

fila_pacientes = Fila(2)
id_count = 0
qtd_pacientes_atendidos = 0

INCLUIR_PACIENTE = 1
REALIZAR_CHAMADA = 2
CONSULTAR_POSICAO_ATUAL = 3
LISTAR_QTD_ATENDIDOS = 4
SAIR = 5

while True:

    print("""\n\rClínica médica - Atendimento
    \r=============
    \r1. Incluir paciente
    \r2. Realizar chamada
    \r3. Consultar a posição atual
    \r4. Listar a quantidade de pacientes atendidos
    \r5. Sair
    """)

    escolha_usuario = int(input('Escolha uma das opções acima > '))

    if escolha_usuario == INCLUIR_PACIENTE:
        try:
            id_count += 1
            informacoes_paciente = list(input("""Informe nome, CPF e plano de saúde do paciente
            \r> """).split())
            paciente = Paciente(informacoes_paciente[0], informacoes_paciente[1], informacoes_paciente[2], id_count)
            fila_pacientes.enfileira(paciente)
            print(fila_pacientes)
        except FilaException as fe:
            print(f"""Não foi possível adicionar o paciente.
            \rDescrição do erro: {fe}""")

    if escolha_usuario == REALIZAR_CHAMADA:
        try:
            paciente_chamado = fila_pacientes.desenfileira()
            print(f'Paciente a ser chamado: {paciente_chamado.nome}, {paciente_chamado.id_number}')
            qtd_pacientes_atendidos += 1
        except FilaException as fe:
            print(f"""\nNão foi possível chamar um paciente
            \rDescrição do erro: {fe}""")

    if escolha_usuario == CONSULTAR_POSICAO_ATUAL:
        pass

    if escolha_usuario == LISTAR_QTD_ATENDIDOS:
        print('\nQuantidade de pacientes atendidos até o momento:', qtd_pacientes_atendidos)

    if escolha_usuario == SAIR:
        break

print('Fim')
