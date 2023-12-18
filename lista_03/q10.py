def area_quadrado(lado, exibir=False):
    area = lado ** 2
    if exibir:
        print(f"A área do quadrado com lado {lado} é {area}")
    return area

def area_triangulo(base, altura, exibir=False):
    area = (base * altura) / 2
    if exibir:
        print(f"A área do triângulo com base {base} e altura {altura} é {area}")
    return area

resultado_quadrado = area_quadrado(4, exibir=True)
resultado_triangulo = area_triangulo(6, 9, exibir=True)