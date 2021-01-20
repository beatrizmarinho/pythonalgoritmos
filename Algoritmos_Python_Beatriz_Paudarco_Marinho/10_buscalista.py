#10. Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca)

tupla = tuple(range(0,21))
print(f'A lista é:{tupla}')
elemento_busca = int(input('Digite o elemento da lista que gostaria de realizar a busca:'))
found = False
for indice in range(0, len(tupla)):
    if tupla[indice] == elemento_busca:
        print(f'Elemento encontrado na posição: {indice}')
        found = True
if not found:
    print('Elemento não encontrado!')