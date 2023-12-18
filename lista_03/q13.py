# q13.py

lista_de_tarefas = []

def adicionar_tarefa(tarefa):
    lista_de_tarefas.append(tarefa)

def exibir_tarefas():
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{i}. {tarefa}")

adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer compras")
adicionar_tarefa("Preparar apresentação")

exibir_tarefas()