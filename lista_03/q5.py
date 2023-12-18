def exibir_menu():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calcular_tabuada(operacao):
    numero = int(input("Digite um número para ver a tabuada: "))
    for i in range(1, 11):
        if operacao == 1:
            resultado = numero + i
        elif operacao == 2:
            resultado = numero - i
        elif operacao == 3:
            resultado = numero * i
        elif operacao == 4:
            resultado = numero / i
        print(f"{numero} {'+' if operacao == 1 else '-' if operacao == 2 else '*' if operacao == 3 else '/'} {i} = {resultado}")

while True:
    exibir_menu()
    opcao = input("Digite o número da operação desejada (ou '5' para sair): ")

    if opcao == '5':
        print("Programa encerrado. Até logo!")
        break

    try:
        opcao = int(opcao)
        if 1 <= opcao <= 4:
            calcular_tabuada(opcao)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")