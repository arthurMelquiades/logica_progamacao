def traduzir_plus2_para_portugues(plus2_texto):
    mapeamento_plus2_portugues = {
        "Jqlg": "Hoje",
        "xqw": "vou",
        "rtqitcoct": "programar"
    }

    palavras_plus2 = plus2_texto.split()

    palavras_portugues = [mapeamento_plus2_portugues[palavra] for palavra in palavras_plus2]

    frase_portugues = ' '.join(palavras_portugues)

    return frase_portugues

def decodificar_url_especial(url_plus2):
    url_decodificada = ''.join([chr(int(codigo, 16)) for codigo in url_plus2.split('/')])
    return url_decodificada

comando_plus2 = 'rtkpv("jvvru://ujqtvwtn.cv/eDIPX")'

parte_url_plus2 = comando_plus2.split('"')[1]

url_decodificada = decodificar_url_especial(parte_url_plus2)

comando_traduzido = traduzir_plus2_para_portugues(url_decodificada)

print(comando_traduzido)