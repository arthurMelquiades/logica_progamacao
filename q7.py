# Função principal
def main():
    # Leitura dos três valores de ponto flutuante
    a, b, c = sorted(map(float, input("Digite três valores de ponto flutuante separados por espaço: ").split()), reverse=True)

    # Verificação do tipo de triângulo
    if a >= b + c:
        print("NAO FORMA TRIANGULO")
    else:
        if a**2 == b**2 + c**2:
            print("TRIANGULO RETANGULO")
        elif a**2 > b**2 + c**2:
            print("TRIANGULO OBTUSANGULO")
        elif a**2 < b**2 + c**2:
            print("TRIANGULO ACUTANGULO")

        if a == b == c:
            print("TRIANGULO EQUILATERO")
        elif a == b or b == c or a == c:
            print("TRIANGULO ISOSCELES")

# Chamada da função principal
main()
