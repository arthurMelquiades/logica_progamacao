def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def buscar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    if nome in agenda:
        print(f"O número de telefone de {nome} é: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado.")