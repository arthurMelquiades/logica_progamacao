# RECURSIVO 
def contagem_regressiva_recursiva(n):
    if n <= 0:
        print("Fim da contagem regressiva!")
    else:
        print(n)
        contagem_regressiva_recursiva(n - 1)

numero = int(input("Digite um número inteiro para a contagem regressiva: "))

contagem_regressiva_recursiva(numero)


#ITERATIVO 
def contagem_regressiva_iterativa(n):
    while n > 0:
        print(n)
        n -= 1
    print("Fim da contagem regressiva!")

numero = int(input("Digite um número inteiro para a contagem regressiva: "))

contagem_regressiva_iterativa(numero)