#16.Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, 
# Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)

class Agenda:
    """Classe que gerencia uma agenda de contatos"""

    def __init__(self):
        self.contatos = []

    def cadastrar(self, contato_nome, telefone, endereco):
        cadastro = {
            "contato_nome": contato_nome,
            "telefone": telefone,
            "endereco": endereco,
        }
        self.contatos.append(cadastro)

    def mostrar(self):
        print(self.contatos)

    def excluir_cadastro(self, contato_nome):
        for cadastro_index in range(0,len(self.contatos)):
            cadastro = self.contatos[cadastro_index]
            if contato_nome == cadastro['contato_nome']:
                del self.contatos[cadastro_index]
                break

nome_usuario = input("Olá, por favor, informe o seu nome do usuário:")

texto_com_opcoes = """
Selecione uma opção:
1 -) Mostrar Cadastros 
2 -) Inserir um cadastro
3 -) Excluir um cadastro
4 -) Sair
"""

cadastros = Agenda()

opcao_selecionada = int(input(texto_com_opcoes))
while opcao_selecionada != 4:
    if opcao_selecionada == 1:
        cadastros.mostrar()
    elif opcao_selecionada == 2:
        contato_nome = input('Para inserir um novo cadastro, por gentileza, informe o nome do contato:')
        telefone = input('Informe o telefone:')
        endereco = input('Informe o endereço:')
        cadastros.cadastrar(contato_nome, telefone, endereco)
    elif opcao_selecionada == 3:
        contato_nome = input('Para excluir um cadastro, por gentileza, informe o nome do contato:')
        cadastros.excluir_cadastro(contato_nome)
    else:
        print("Opção inválida!")
    opcao_selecionada = int(input(texto_com_opcoes))

print(f"Sessão encerrada. Até mais {nome_usuario}!")