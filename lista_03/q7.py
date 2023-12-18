def verifica_parenteses(expressao):
    pilha = []

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False  
            pilha.pop()

    return not pilha 
expressao = input("Digite uma expressão com parênteses: ")

resultado = verifica_parenteses(expressao)

if resultado:
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses não estão balanceados.")