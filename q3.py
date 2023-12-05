# Função principal
def main():
    # Leitura da quantidade de kWh consumida e tipo de instalação
    consumo_kwh = float(input("Digite a quantidade de kWh consumida: "))
    tipo_instalacao = input("Digite o tipo de instalação (R para residências, I para indústrias, C para comércios): ")

    # Cálculo do preço a pagar de acordo com a tabela
    if tipo_instalacao == 'R' or tipo_instalacao == 'r':
        if consumo_kwh <= 500:
            preco_pagar = consumo_kwh * 0.40
        else:
            preco_pagar = consumo_kwh * 0.65
    elif tipo_instalacao == 'I' or tipo_instalacao == 'i':
        if consumo_kwh <= 1000:
            preco_pagar = consumo_kwh * 0.55
        else:
            preco_pagar = consumo_kwh * 0.60
    elif tipo_instalacao == 'C' or tipo_instalacao == 'c':
        if consumo_kwh <= 5000:
            preco_pagar = consumo_kwh * 0.55
        else:
            preco_pagar = consumo_kwh * 0.60
    else:
        print("Tipo de instalação inválido. Utilize R para residências, I para indústrias ou C para comércios.")
        return

    # Impressão do preço a pagar
    print(f"Preço a pagar: R$ {preco_pagar:.2f}")

# Chamada da função principal
main()
 