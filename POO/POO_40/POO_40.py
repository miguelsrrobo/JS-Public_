from math import sqrt

class BaseDeDados:
   def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'cliente' not in self.dados:
            self.dados['cliente'] = {id: nome}
        else:
            self.dados['cliente'].update({id: nome})

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
print(bd.dados)
