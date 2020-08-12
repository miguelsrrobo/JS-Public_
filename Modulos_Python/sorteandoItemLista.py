from random import choice

numero1 = str(input('Primeiro Aluno: '))
numero2 = str(input('Segundo Aluno: '))
numero3 = str(input('Terceiro Aluno: '))
numero4 = str(input('Quarto Aluno: '))

lista = [numero1, numero2, numero3, numero4]
escolha = choice(lista)
print(f'O aluno escolhido foi {escolha}')