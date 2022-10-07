from Marcacao import *
from Paciente import *

sm = Marcacao(60)

sm.addPaciente(Paciente('Alex',20,'OTO'))
sm.addPaciente(Paciente('Amanda',10,'OFT'))
sm.addPaciente(Paciente('Juliana',20,'OTO'))
sm.addPaciente(Paciente('Pablo',20,'DER'))
sm.addPaciente(Paciente('Haniel',10,'OTO'))  # Haniel não entrou pois o tempo máx. já foi atingido
print(sm)

sm.cancelarAgendamento('OTO')
print(sm)
