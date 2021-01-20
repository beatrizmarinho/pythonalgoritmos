#14. Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e 
# imprimir o livro selecionado)

nome_solicitante = input('Olá, seja bem-vindo(a) a nossa biblioteca! Por gentileza, informe seu nome:')
lista_livros = ['Moby Dick', 'A Divina Comédia', 'Guerra e Paz','Dom Quixote','As Mil e uma Noites','Orgulho e Preconceito','Romeu e Julieta', 'Os Lusíadas','Viagem ao centro da Terra', 'Os Três Mosqueteiros']
print(f'Olá, {nome_solicitante}! Os livros disponíveis no momento são:')
for livros in lista_livros:
    print(livros)
escolha_livro = input('Por gentileza, informe o livro que gostaria de alugar:')
if escolha_livro in lista_livros:
    print(f'Você escolheu o livro {escolha_livro}! Por favor, faça a retirada no balcão e boa leitura!')
else:
    print('O livro que você escolheu não está disponível. Tente novamente!')