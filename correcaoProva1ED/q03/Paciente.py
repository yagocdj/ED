class Paciente:
    def __init__(self, nome:str, tempo_atendimento:int, especialidade:str):
        self.nome = nome
        self.tempo_atendimento = tempo_atendimento
        self.especialidade = especialidade

    def __str__(self):
        return f'{self.nome}, tempo Atend.: {self.tempo_atendimento}, espec.: {self.especialidade}'