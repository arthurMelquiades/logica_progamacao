# Função principal
def main():
    # Leitura do salário do funcionário
    salario = float(input("Digite o salário do funcionário: R$ "))

    # Cálculo do aumento com base nas condições
    if salario > 1250.00:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.15

    # Cálculo do novo salário
    novo_salario = salario + aumento

    # Impressão dos resultados
    print(f"Salário anterior: R$ {salario:.2f}")
    print(f"Aumento: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")

# Chamada da função principal
main()
 