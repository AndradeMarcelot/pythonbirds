class Pessoa:
    olhos = 2

    def __init__(self, nome = None, idade = 30, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    marcelo = Pessoa('Marcelo', 35)
    marcela = Pessoa('Marcela', 29)
    reginaldo = Pessoa('Reginaldo', 35, marcelo, marcela)
    print(Pessoa.cumprimentar(marcelo))
    print(marcelo.cumprimentar())
    print(marcelo.nome)
    print(marcelo.idade)
    for filho in reginaldo.filhos:
        print (filho.nome)
    reginaldo.sobrenome = 'Andrade'
    del reginaldo.filhos
    print(reginaldo.__dict__)
    print(marcelo.__dict__)
    print(id(Pessoa.olhos), id(marcelo.olhos), id(reginaldo.olhos))