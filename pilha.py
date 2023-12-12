pilha = [1, 2, 3, 4, 5]

sistema = input("qual o comando ? ") 
 
if sistema == 'e':

    pilha.append(len(pilha) + 1) 

    print(pilha)

elif sistema == 'd':
    indice_para_deletar = len(pilha)
    del pilha[indice_para_deletar] 

    print(pilha)

elif sistema == 's': 

    print(pilha)
    