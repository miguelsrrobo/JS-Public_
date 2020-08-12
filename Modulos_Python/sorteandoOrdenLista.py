from random import shuffle
Aluno1 = str(input('Primeiro Aluno: '))
Aluno2 = str(input('Segundo Aluno: '))
Aluno3 = str(input('Terceiro Aluno: '))
Aluno4 = str(input('Quarto Aluno: '))

lista_de_alunos = [Aluno1, Aluno2, Aluno3, Aluno4]
shuffle(lista_de_alunos)

print('A ordem de apresentação será: ')
print(lista_de_alunos)