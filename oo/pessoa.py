class Pessoa:
    olhos = 2

    def __init__(self, nome = None, idade = 30, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    Pessoa.olhos = 3
    print(Pessoa.metodo_estatico(), reginaldo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), reginaldo.nome_e_atributos_de_classe())
