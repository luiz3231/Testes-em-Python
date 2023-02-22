class Cliente:
    def __init__(self, nome:str, data_nascimento:str, cpf:str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    DEVE = 0
    def comprou(self, valor:float):
        self.valor = valor
        self.DEVE += (valor)  
    def pagou(self, valor:float):
        self.valor = valor
        self.DEVE -= (valor)

    
if __name__ == '__main__':
    Emily = Cliente('Emily','15/09/2007','123.456.789-25')
    Luiz = Cliente('Luiz Eduardo Rodrigues Santos', '31/10/2005', '149.019.496-75')

    Luiz.comprou(300)
    Luiz.pagou(5)
    
    Emily.comprou(900)
    Emily.pagou(200)

    
    print(f'Cliente: {Emily.nome}')
    print(f'Data de nascimento: {Emily.data_nascimento}')
    print(f'CPF: {Emily.cpf}')
    print(f'Deve o Valor de R${Emily.DEVE}')
    print()
    print()
    print(f'Cliente: {Luiz.nome}')
    print(f'Data de nascimento: {Luiz.data_nascimento}')
    print(f'CPF: {Luiz.cpf}')
    print(f'Deve o Valor de R${Luiz.DEVE}')
    