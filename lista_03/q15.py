def grito_de_natal(felicidade):
    if felicidade <= 1:
        return "A felicidade deve ser maior que 1 para um grito de Natal animado!"
    
    mensagem = "Feliz Natal" + "!!" * felicidade
    return mensagem

valor_de_felicidade = 5
grito = grito_de_natal(valor_de_felicidade)
print(grito)

valor_invalido = 0
grito_invalido = grito_de_natal(valor_invalido)
print(grito_invalido)