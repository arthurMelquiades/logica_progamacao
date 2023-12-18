
def calcular_notas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    resultado = {}

    for nota in notas:
        qtd_notas = valor // nota
        valor %= nota
        resultado[nota] = qtd_notas

    return resultado


valor = int(input("Digite um valor inteiro: "))


notas_resultado = calcular_notas(valor)

print(f"\nValor: {valor}")
print("Notas necessárias:")
for nota, qtd in notas_resultado.items():
    print(f"{qtd} nota(s) de {nota}")