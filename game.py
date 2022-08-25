from models.calcular import Calcular

def main():
    pontos: int = 0
    jogar(pontos)

def jogar(pontos):
    dificuldade = int(input('Informa o nível de dificuldade desejado [1, 2, 3]: '))

    calc = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc._mostrar_operacao

    resultado = int(input())

    if calc._checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

        continuar= int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não]: '))

        if continuar == 1:
            jogar(pontos)
        elif continuar == 0:
            print(f'Você finalizou com {pontos} ponto(s).')
            print('Até a próxima!')

if __name__ == '__main__':
    main()
