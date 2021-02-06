class Pessoa:
    def __init__(self, nome = None, idade = 30):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Marcelo', 35)
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)