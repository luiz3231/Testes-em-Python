class Carro:
    def __init__(self, direção, motor):
        self.direção = direção
        self.motor = motor
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()
    def calcular_direção(self):
        return self.direção.valor
    def girar_a_direita(self):
        self.direção.girar_a_direita()
    def girar_a_esquerda(self):
        self.direção.girar_a_esquerda()

class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
class Direção:
    rotação_a_direita_dct={NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotação_a_direita_dct[self.valor]

    rotação_a_esquerda_dct={NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}
    def __init__(self):
            self.valor = NORTE
    def girar_a_esquerda(self):
        self.valor = self.rotação_a_direita_dct[self.valor]

