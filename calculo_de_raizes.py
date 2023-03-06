"""
Este é um codigo bem basico que fiz para me auxiliar em um
trabalho de matematica da escola.

Formulas
Δ=b²-4ac
x=-b-+√Δ 

""" 
import math
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
delta = b**2-4*a*c
if delta < 0:
    print('SØ')
elif delta >= 0:
    x = ((b * -1) + math.sqrt(delta)) / 2
    print(f'Δ = {delta}')
    if x < 0:
        X = x * (-1)
        print(f'x = {X}')
    else:
        print(f'x = {x}')
else:
    pass