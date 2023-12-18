def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

minha_lista = [7, 4, 3, 12, 8]
print("Lista original:", minha_lista)

bubble_sort(minha_lista)

print("Lista ordenada:", minha_lista)