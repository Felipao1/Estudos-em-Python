print('************************************')
print('Alunos da Turma de Informática')

turma = []

while True:
    aluno = input('Digite um nome:\n')
    turma.append(aluno)
    quantidadeAlunos = input('Há mais alunos? [S|N]\n')
    if quantidadeAlunos.upper() == 'N':
    
        break
    elif quantidadeAlunos.upper() != 'N' and quantidadeAlunos.upper() != 'S':
        print('OPÇÃO INVÁLIDA!')
    
for aluno in turma :
    print(aluno)

