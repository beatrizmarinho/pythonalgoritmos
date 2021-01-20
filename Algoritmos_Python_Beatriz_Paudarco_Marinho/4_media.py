# 4. Elabore um algoritmo em Python que leia, calcule e escreva a média aritmética entre quatro números;

a = float(input('Digite o primeiro número:'))
b = float(input('Digite o segundo número:'))
c = float(input('Digite o terceiro número:'))
d = float(input('Digite o quarto número:'))
media = sum([a,b,c,d])/4
print(f'A média será: {media}')