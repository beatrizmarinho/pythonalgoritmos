#9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.

import math
raio = float(input('Informe o raio do círculo:'))
area = math.pi*raio**2
perimetro = 2*math.pi*raio
print(f'A área do círculo é: {area}.')
print(f'O perímetro do círculo é: {perimetro}.')