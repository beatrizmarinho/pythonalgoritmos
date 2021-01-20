#17. Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. 
# Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela)

class Agenda:
    """Classe que gerencia uma agenda de revisões de veículos"""

    def __init__(self):
        self.revisoes_agendadas = []

    def agendar(self, proprietario_nome, data, hora, carro_marca, carro_modelo, carro_ano):
        agendamento = {
            "proprietario_nome": proprietario_nome,
            "data": data,
            "hora": hora,
            "carro_marca": carro_marca,
            "carro_modelo": carro_modelo,
            "carro_ano": carro_ano
        }
        self.revisoes_agendadas.append(agendamento)

    def mostrar(self):
        print(self.revisoes_agendadas)

nome_usuario = input("Olá, por favor, informe o seu nome do usuário:")

texto_com_opcoes = """
Selecione uma opção:
1 -) Mostrar Agendamentos 
2 -) Inserir um agendamento
3 -) Sair
"""

agendamentos = Agenda()

opcao_selecionada = int(input(texto_com_opcoes))
while opcao_selecionada != 3:
    if opcao_selecionada == 1:
        agendamentos.mostrar()
    elif opcao_selecionada == 2:
        proprietario_nome = input('Para agendar a revisão do carro, por gentileza, informe o nome do proprietário:')
        data = input('Informe o dia que gostaria de agendar a revisão:')
        hora = input('Informe o horário da revisão:')
        carro_marca = input('Informe a marca do carro:')
        carro_modelo = input('Informe o modelo do carro:')
        carro_ano = input('Informe o ano do carro:')
        agendamentos.agendar(proprietario_nome, data, hora, carro_marca, carro_modelo, carro_ano)
    else:
        print("Opção inválida!")
    opcao_selecionada = int(input(texto_com_opcoes))

print(f"Sessão encerrada. Até mais {nome_usuario}!")