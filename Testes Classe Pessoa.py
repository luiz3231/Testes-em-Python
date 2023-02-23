class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    
    @staticmethod
    def metedo_estatico():
        return 42
    
    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'
    
### Herança ###
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Piscar 3° olho.'

if __name__ == '__main__':
    anne = Homem(nome='Anne')
    Luiz = Homem(anne, nome='Luiz')
    Natan = Mutante(nome='Natan')
    print(Pessoa.cumprimentar(Luiz))
    print(id(Luiz))
    print(Luiz.cumprimentar())
    print(Luiz.nome)
    print(Luiz.idade)
    for filho in Luiz.filhos:
        print(filho.nome)
    Luiz.sobrenome = 'Rodrigues'
    print(Luiz.sobrenome)
    Luiz.olhos = 1
    del Luiz.olhos
    print(Luiz.__dict__)
    print(Pessoa.olhos)
    print(Luiz.olhos)
    print(anne.olhos)
    print(Pessoa.metedo_estatico(), Luiz.nome_e_atributos_de_classes())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Luiz, Homem))
    print(Luiz.olhos)
    print(Luiz.cumprimentar())
    print(Natan.cumprimentar())