# Função principal
def main():
    # Leitura da distância desejada em km
    distancia_km = float(input("Digite a distância que deseja percorrer em km: "))

    # Cálculo do preço da passagem
    if distancia_km <= 200:
        preco_passagem = distancia_km * 0.50
    else:
        preco_passagem = distancia_km * 0.45

    # Impressão do preço da passagem
    print(f"Preço da passagem: R$ {preco_passagem:.2f}")

# Chamada da função principal
main()
 