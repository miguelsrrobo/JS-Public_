frase = str(input('Digite uma frase: ')).upper().strip()
# noinspection PyInterpreter
print('A letra A aparece {} veses na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))