def contem_item(lista, item):
  
  
    
    return item in lista

def gerar_terceira_lista(lista1, lista2):
   
    terceira_lista = []

    for item in lista1:
        if not contem_item(terceira_lista, item):
            terceira_lista.append(item)

    for item in lista2:
        if not contem_item(terceira_lista, item):
            terceira_lista.append(item)

    return terceira_lista


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

terceira_lista = gerar_terceira_lista(lista1, lista2)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Terceira Lista (sem elementos repetidos):", terceira_lista)