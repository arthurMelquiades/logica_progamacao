import random

def obter_opcao_computador():
    opcao = random.randint(0, 2)
    if opcao == 0:
        return 'pedra'
    elif opcao == 1:
        return 'papel'
    else:
        return 'tesoura'

def main():
    while True:
        opcao_computador = obter_opcao_computador()

        opcao_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if opcao_computador == opcao_jogador:
            print("Empate!")
        elif (opcao_computador == 'pedra' and opcao_jogador == 'tesoura') or \
             (opcao_computador == 'tesoura' and opcao_jogador == 'papel') or \
             (opcao_computador == 'papel' and opcao_jogador == 'pedra'):
            print("Jogador venceu!")
        else:
            print("Computador venceu!")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

if __name__ == "__main__":
    main()