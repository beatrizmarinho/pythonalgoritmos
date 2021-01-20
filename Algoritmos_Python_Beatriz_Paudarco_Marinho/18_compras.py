#18.Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário selecione 
# um objeto e imprimir a compra na tela)

nome_usuario = input('Olá, bem-vindo(a) a nossa lojinha. Por favor, informe seu nome:')
print(f'Olá, {nome_usuario}! Os materiais disponíves para compra são:')
caderno = {
            'nome': 'caderno',
            'preço': 9.99,
            'cor': 'roxo'
            }
caneta = {
            'nome': 'caneta',
            'preço': 2.99,
            'cor': 'azul'
            } 
borracha = {
            'nome': 'borracha',
            'preço': 3.99,
            'cor': 'branca'
            }
lapis = {
            'nome': 'lapis',
            'preço': 1.99,
            'cor': 'branca'
            }

estante = [caderno, caneta, borracha, lapis]
print(estante)

compras = []
objeto_compra = input('Informe o material que deseja comprar ou digite "encerrar" para finalizar a compra:')
while objeto_compra != 'encerrar':
    found = False
    for objeto in estante:
        if objeto["nome"] == objeto_compra:
            compras.append(objeto)
            found = True
    if not found:
        print('Objeto não encontrado!')
    print(f'Sua lista de compras é: {compras}')
    objeto_compra = input('Informe o material que deseja comprar ou digite "encerrar" para finalizar a compra:')
    
print(f"Sua lista de compras final é: {compras}")