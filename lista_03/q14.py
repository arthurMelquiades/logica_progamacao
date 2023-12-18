def passagem_por_valor(x):
    print("Dentro da função (antes da modificação):", x)
    x = 10
    print("Dentro da função (após a modificação):", x)

def passagem_por_referencia(lista):
    print("Dentro da função (antes da modificação):", lista)
    lista.append(4)
    print("Dentro da função (após a modificação):", lista)

valor = 5
print("Antes da chamada da função (passagem por valor):", valor)
passagem_por_valor(valor)
print("Após a chamada da função (passagem por valor):", valor)
print()

lista_valores = [1, 2, 3]
print("Antes da chamada da função (passagem por referência):", lista_valores)
passagem_por_referencia(lista_valores)
print("Após a chamada da função (passagem por referência):", lista_valores)