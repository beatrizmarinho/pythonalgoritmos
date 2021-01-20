#5. Algoritmo para calcular a média do aluno (Deve colocar o nome do aluno, colocar 4 notas e imprimir sua média)

nome_aluno = input('Digite o nome do(a) aluno(a):')
a = float(input('Digite a primeira nota:'))
b = float(input('Digite a segunda nota:'))
c = float(input('Digite a terceira nota:'))
d = float(input('Digite a quarta nota:'))
media = sum([a,b,c,d])/4
print(f'A média do(a) aluno(a) {nome_aluno} é {media}.')