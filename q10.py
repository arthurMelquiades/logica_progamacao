import random

def main():
    # Sorteio do número secreto entre 1 e 100
    numero_secreto = random.randint(1, 100)

    # Inicialização da variável palpite
    palpite = 0

    # Loop principal
    while True:
        # Leitura do palpite do usuário
        palpite = int(input("Digite seu palpite (entre 1 e 100): "))

        # Verificação do palpite
        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        else:
            # Caso o palpite seja correto, encerra o jogo
            print(f"Parabéns! Você acertou. O número secreto era {numero_secreto}.")
           
