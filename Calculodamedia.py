nota = [0,0,0,0,0] #lista notas criada

soma = 0

x = 0

while x < 5:
	nota[x] = float(input("Nota %d:" % x)) #aqui é uma estrutura de repetição para variar o valor de 'x'
	soma += nota[x]
	x += 1

x = 0 #adicionamos o valor de notas[0] à soma e depois notas[1],2,3 e 4, um elemento a cada recepição

while x < 5: #utilizamos o valor de x no índice e o incrementamos de 1
	print("Nota : {0:.2f}".format(nota[x]))
	x+=1
print("Média: {0:.2f}".format(soma/x))
