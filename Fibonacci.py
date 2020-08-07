Numero = int(input(':Que termo deseja encontrar: '))
ultimo = 1
penultimo = 1

if (Numero == 1) or (Numero == 2):
	print('1')
else:
	for count in range(2,Numero):
		termo = ultimo + penultimo
		penultimo = ultimo
		ultimo = termo
		count += 1
	print(termo)

