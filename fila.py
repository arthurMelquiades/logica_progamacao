fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

sistema = input("qual o comando ? ") 
if sistema == 'f':
    
     fila.append(len(fila) + 1) 
    
     print(fila)

elif sistema == 'a': 
    
    del fila[0] 
    
    print(fila)

elif sistema == 's': 
    
     print(fila)