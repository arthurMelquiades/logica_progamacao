# Função principal
def main():
    # Leitura das informações sobre o jogo
    hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input("Digite a hora inicial, minuto inicial, hora final e minuto final separados por espaço: ").split())

    # Cálculo da duração do jogo
    duracao_horas = hora_final - hora_inicial
    duracao_minutos = minuto_final - minuto_inicial

    # Tratamento para garantir que a duração seja sempre positiva
    if duracao_horas < 0:
        duracao_horas += 24

    if duracao_minutos < 0:
        duracao_minutos += 60
        duracao_horas -= 1

    # Impressão do resultado
    print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")

# Chamada da função principal
main()
