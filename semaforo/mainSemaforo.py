from semaforo import Semaforo
from clearSemaforo import clearTerminal

quantidadeDeCiclos = int(input('Digite quantos ciclos o semáforo fará: '))
semaforo = Semaforo(20, 20, 3, 2)

for ciclo in range(quantidadeDeCiclos):

    clearTerminal()

    # primeira transição
    semaforo.exibirEstadoAtual()
    semaforo.contagemRegressiva()
    clearTerminal()
    semaforo.mudarEstadoAtual()

    # segunda transição
    semaforo.exibirEstadoAtual()
    semaforo.contagemRegressiva()
    clearTerminal()
    semaforo.mudarEstadoAtual()

    # terceira transição
    semaforo.exibirEstadoAtual()
    semaforo.contagemRegressiva()
    clearTerminal()
    semaforo.mudarEstadoAtual()

    # quarta transição
    semaforo.exibirEstadoAtual()
    semaforo.contagemRegressiva()
    clearTerminal()
    semaforo.mudarEstadoAtual()

print('Fim do(s) ciclo(s).')
