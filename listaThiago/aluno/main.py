from aluno import Aluno

nomeAluno = input('Digite o nome do aluno: ')
matriculaAluno = int(input(f'Digite a matrícula de {nomeAluno}: '))
notasAluno = list(
    map(float, input(f'Digite as 4 notas de {nomeAluno}:\n').split()))

aluno_x = Aluno(matriculaAluno, nomeAluno, notasAluno)

mediaAluno = aluno_x.media()

print('\nInformações sobre o aluno: ')
print(f'Nome: {aluno_x.getNome()}')
print(f'Matrícula: {aluno_x.getMatricula()}')
print(f'Média: {mediaAluno}')

print(
    'Se essa matrícula não pertence a esse aluno, digite "cn" (change name)' +
    ' para alterar seu nome. '
)

mudarNome = input().lower()

if mudarNome == 'cn':
    aluno_x.setNome(input('Novo nome: '))

print('Fim do programa!')
