nome = str(input('Digite seu nome completo: '))
nome2 = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeior nome é {}\nSeu último nome é {}'.format(nome2[0], nome2[len(nome2)-1]))
