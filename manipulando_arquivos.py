"""
Métodos utilizados
read(), readline(), readlines()

read() => retorna o conteúdo do arquivo como uma única string
readline() => retorna uma linha do texto a cada chamada
readlines() => retorna uma lista de valores de string do arquivo
"""
"""
# read()
manipulador = open('arquivo.txt', 'r')
print("\nMétodo read() : \n")
print(manipulador.read())

manipulador.seek(0)  # volta para o ínicio do arquivo

# readline()
print("\nMétodo readline() : \n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

# readlines()
print("\nMétodo readlines() : \n")
print(manipulador.readlines())

manipulador.close()
"""
"""
Manipulação do arquivo com o laço for
EXEMPLO 1
"""
"""
manipulador = open('arquivo.txt', 'r')

for linha in manipulador:
    linha = linha.rstrip()  # remove linha em branco do print
    print(linha)

manipulador.close()
"""
"""
Manipulação do arquivo com o laço for
EXEMPLO 2 - contando quantas linhas tem o arquivo
"""
print('\nContando as linhas do aruqivo de texto\n')
contador = 0
arquivo = open('arquivo.txt', 'r')
for linha in arquivo:
    contador += 1
    print('Número de linhas do arquivo:', contador)

print('\nTotal de linhas:', contador)
arquivo.close()

"""
Manipulação do arquivo com o laço for
EXEMPLO 3 - Retornando somente as linhas que possuem a palavra Python
"""
print('\nEXEMPLO 3 - Retornando somente as linhas que possuem a palavra Python\n')
arquivo = open('arquivo.txt', 'r')
contador = 0
for linha in arquivo:
    linha = linha.rstrip()
    if 'python' in linha.lower():
        contador += 1
        print(linha)
print('\nForam retornadas ', contador, 'linhas')
arquivo.close()

"""
Manipulação do arquivo com o laço for
EXEMPLO 4 - Retornando somente as linhas que possuem a palavra informada pelo usuário.
"""

print('\nEXEMPLO 4 - Retornando somente as linhas que possuem a palavra digitada\n')
arquivo = open('arquivo.txt', 'r')
contador = 0
palavra = input('Digite a palavra a buscar:')
for linha in arquivo:
    linha = linha.rstrip()
    if palavra.lower() in linha.lower():
        contador += 1
        print(linha)
print('\nForam retornadas ', contador, 'linhas')
arquivo.close()