"""
minha_lista = ['Lista 1', 2, 'Teste', 'Banana', 'Laranja']
print(type(minha_lista))
print(minha_lista)

# modificando o primeiro elemento da lista
minha_lista[0] = 'Leandro'
print(minha_lista)

# TUPLAS () - não podem ser modificadas, imutável

minha_tupla = ('Leandro', 'Amanda', 'Leana')
print(minha_tupla)

# Acessando os seus elementos
print(minha_tupla[0])
print(minha_tupla[1])

# Dicionários  {} 'chave':valor

dic = {'leandro':100, 'Amanda':51, 'Leana':49 }
print(dic)
print(dic['leandro'])


dic2 = {'xwy': 1, 'kxy': 2}
print(dic2['kxy'])
print(type(dic))

# percorrendo um dicionário
for chave in dic:
    print(dic[chave])

# retornando um número par ou ímpar
num_impar = 11
num_par = 10

if num_par % 2 == 0:
    print('Esse é um número par!')
else:
    print('Esse é um número ímpar!')

if num_impar % 2 == 0:
    print('Esse é um número par!')
else:
    print('Esse é um número ímpar!')

# comando while imprime de 0 a 10
num = 0
while num < 11:
    print(num)
    num += 1
"""
# imprimindo elementos de uma lista
minha_lista = [1, 'teste', 2, 'ovo', 3, 'cachorro', 4, 'casa']
"""
for i in minha_lista:
    print(i)
    
"""
"""
# imprimindo pelo index
for i in range(0, len(minha_lista)):
    print(i)
"""
# o mesmo que
for i in range(0, 10, 2):
    print(i)
