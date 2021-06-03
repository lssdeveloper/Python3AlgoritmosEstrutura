class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def obterNome(self):
        return self.nome

    def obterIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def __str__(self):
        return 'Nome: %s ' % self.nome


# criando um objeto do tipo pessoa

pessoa = Pessoa('Leandro', 45)
print(pessoa.obterIdade())
print(pessoa.obterNome())
print(type(pessoa))
print(pessoa)
print('Nome: %s' % pessoa.nome)
print('Idade: %d' % pessoa.idade)

p1 = Pessoa('Amanda', 23)
p2 = Pessoa('Leana', 16)
p3 = Pessoa('Carlos', 15)
p4 = Pessoa('Silvia', 20)

pessoas = [p1, p2, p3, p4]
for pessoa in pessoas:
    print('Nome: '+ pessoa.obterNome() +', Idade: '+str(pessoa.obterIdade()))

p1.setIdade(58)

print(p1.obterNome() + ' ' + str(p1.obterIdade()))
