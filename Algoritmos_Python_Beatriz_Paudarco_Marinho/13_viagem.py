#13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)

nome_viajante = input('Seja bem-vindo(a) a nossa agência de viagens! Por favor, nos informe o seu nome:')
opcoes_destino = ['Maceió-AL','Jericoacoara-CE','Ouro Preto-MG', 'Trindade-RJ', 'Brotas-SP']
print(f'Olá, {nome_viajante}! As opções de destino para esse mês são:')
for destino in opcoes_destino:
    print(destino)
escolha_destino = input('Por gentileza, informe o destino escolhido para sua viagem:')
if escolha_destino in opcoes_destino:
    print(f'Você escolheu {escolha_destino}! Agendamento Realizado com sucesso!')
else:
    print('O destino que você escolheu não está na lista.')