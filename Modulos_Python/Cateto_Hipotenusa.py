from math import hypot

catetoOposto = float(input('Comprimento do Cateto Oposto: '))
catetoAdjacente = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

'''
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
'''
