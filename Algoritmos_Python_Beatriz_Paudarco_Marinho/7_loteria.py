#7. Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou)

import random
nome_usuario = input('Digite o seu nome:')
numero = input('Digite o número escolhido:')
lista = list(range(0, 101))
numero_premiado = random.choice(lista)
print(f'{nome_usuario}, o número sorteado foi {numero_premiado}!')
if numero == numero_premiado:
    print('Parabéns, você ganhou!')
else:
    print('Infelizmente você não ganhou!')