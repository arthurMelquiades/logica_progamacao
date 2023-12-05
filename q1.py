# Função para encontrar o maior e o menor entre três números
def encontrar_maior_menor(num1, num2, num3):
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    return maior, menor

# Função principal
def main():
    # Leitura dos três números
    num1, num2, num3 = map(int, input().split())

    # Chamada da função para encontrar o maior e o menor
    maior, menor = encontrar_maior_menor(num1, num2, num3)

    # Impressão dos resultados
    print(f"MAIOR={maior}")
    print(f"MENOR={menor}")

# Chamada da função principal
main()
 