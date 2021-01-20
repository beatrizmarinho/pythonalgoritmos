#15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)

nome_solicitante = input('Olá, seja bem-vindo(a) a nossa feira livre! Por gentileza, informe o seu nome:')
lista_frutas = ['uva','abacaxi','banana','morango','melancia','goiaba','melão']
print(f'Olá, {nome_solicitante}! As frutas disponíveis no dia de hoje são:')
for frutas in lista_frutas:
    print(frutas)
escolha_fruta = input('Por favor, escolha a fruta desejada:')
if escolha_fruta in lista_frutas:
    print(f'Você escolheu {escolha_fruta}! Dirija-se ao balcão para a retirada e pagamento. Boas compras!')
else:
    print('A fruta que você escolheu está fora de estoque no dia de hoje. Tente novamente ou volte outro dia!')