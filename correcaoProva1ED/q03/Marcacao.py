from FilaEncadeada import *

class Marcacao:
    def __init__(self, tempo_max_minutos:int):
        self.fila = Fila()
        self.tempo_max = tempo_max_minutos

    def addPaciente(self, paciente:'Paciente'):
        acc = 0
        for pos in range(1,len(self.fila)+1):
            # pac = self.fila.elemento(pos)
            # acc += pac.tempo_atendimento
            acc += self.fila.elemento(pos).tempo_atendimento
        if acc <= self.tempo_max:
            self.fila.enfileira(paciente)

    def addPacientePablo(self, paciente:'Paciente'):
        try:
            assert self.tempo_max > 0
            self.enfileira(paciente)
            self.tempo_max -= paciente.tempo_atendimento
            return True
        except:
            return False

    def cancelarAgendamento(self, especialidade:str):
        for pos in range(len(self.fila)):
            paciente = self.fila.desenfileira()
            if paciente.especialidade != especialidade:
                self.fila.enfileira(paciente)

    def __str__(self):
        s = ''
        for pos in range(1,len(self.fila)+1):
            s+= f'{self.fila.elemento(pos).nome}, {self.fila.elemento(pos).especialidade}\n'
        return s
