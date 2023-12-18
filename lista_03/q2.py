def multiplicacao(a, b):
    resultado = 0
    
    for _ in range(b):
        resultado += a
    return resultado

def divisao_inteira_e_resto(dividendo, divisor):
    quociente = 0
    
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    
    resto = dividendo
    return quociente, resto


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


resultado_multiplicacao = multiplicacao(numero1, numero2)
print(f"A multiplicação de {numero1} por {numero2} é: {resultado_multiplicacao}")


quociente, resto = divisao_inteira_e_resto(numero1, numero2)
print(f"A divisão inteira de {numero1} por {numero2} é: {quociente}")
print(f"O resto da divisão de {numero1} por {numero2} é: {resto}")