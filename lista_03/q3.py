
soma = 0
quantidade_numeros = 0


while True:
   
    numero = int(input("Digite um número (digite 0 para encerrar): "))
    
    
    if numero == 0:
        break
    

    soma += numero
    quantidade_numeros += 1


if quantidade_numeros > 0:
    media = soma / quantidade_numeros
    print(f"\nQuantidade de números digitados: {quantidade_numeros}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media}")
else:
    print("\nNenhum número foi digitado.")