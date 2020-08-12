from pessoa import Pessoa

p1 = Pessoa('Luis',29)
p2 = Pessoa('Joao',32)

print(f'{p1.nome} posui {p1.idade} anos e naceu em {p1.get_ano_nacimento()}.')
print(f'{p2.nome} posui {p2.idade} anos e naceu em {p2.get_ano_nacimento()}.')