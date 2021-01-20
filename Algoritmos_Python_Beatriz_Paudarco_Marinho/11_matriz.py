#11. Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário fazer uma busca)

#Escrevendo a matriz
matriz = []
for linha in range(1, 11):
    coluna = list(range(1,11))
    matriz.append(coluna)
print(matriz)

#Buscando na matriz
elemento_busca = int(input('Digite o elemento da lista que gostaria de realizar a busca:'))
found = False
for indice_linha in range(0, len(matriz)):
    for indice_coluna in range(0, len(matriz[indice_linha])):
        if matriz[indice_linha][indice_coluna] == elemento_busca:
            found = True
            print(f'Elemento encontrado na linha {indice_linha} e na coluna {indice_coluna}!')
            break
    if found: break
if not found:
    print('Elemento não encontrado!') 