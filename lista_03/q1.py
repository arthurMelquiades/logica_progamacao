def imprimir_numeros():
    
    print("Números de 1 a 100:")
    for i in range(1, 101):
        print(i, end=' ')
    print("\n")

def imprimir_pares_50_100():
 
    print("Números pares de 50 a 100:")
    for i in range(50, 101, 2):
        print(i, end=' ')
    print("\n")

def contagem_regressiva():
  
    print("Contagem regressiva:")
    for i in range(10, -1, -1):
        print(i, end=' ')
    print("Fogo!\n")

def numeros_pares_ou_impares(valor, escolha):
    
    print(f"Números {escolha}s até {valor}:")
    for i in range(1, valor + 1):
        if (escolha == 'par' and i % 2 == 0) or (escolha == 'ímpar' and i % 2 != 0):
            print(i, end=' ')
    print("\n")


imprimir_numeros()
imprimir_pares_50_100()
contagem_regressiva()


valor_usuario = int(input("Digite um valor: "))
escolha_usuario = input("Deseja números pares ou ímpares? (par/ímpar): ")


numeros_pares_ou_impares(valor_usuario, escolha_usuario)