"""
Crie um programa onde o usuário tente adivinha
o número que o computador está "pensando" e mostre
na tela uma mensagem de validação.
"""

import emoji
from random import randint
from time import sleep
from colorama import Fore, Style, init

init()
def linha():
    print('_' * 60)


def recomeço():
    print()
    print(f'{"ADIVINHAÇÃO":^30}')
    linha()
    print(Fore.YELLOW + 'Estou pensando em um número de 0 a 10' + Style.RESET_ALL)
recomeço()


while True:
    computador = randint(0, 10)
    palpites = 0

    while True:
        jogador = int(input('Em que número estou pensando?:'))
        print(f'hmmm... Será que estou pensando no número {jogador}')
        sleep(2)
        linha()
        # Sistema de condições -----------------------------------------------------------------------------------------
        if jogador != computador and jogador > computador:
            print(f'Não pensei no número {Fore.RED}{jogador}{Style.RESET_ALL}')
            print('Menos...')
            sleep(1)
            palpites += 1
            linha()
        elif jogador != computador and jogador < computador:
            print(f'Não pensei no número {Fore.RED}{jogador}{Style.RESET_ALL}')
            print('Mais...')
            sleep(1)
            linha()
            palpites += 1
        else:
            print()
            print()
            print(f'{Fore.GREEN}👏 PARABÉNS 👏{Style.RESET_ALL}, eu havia pensado no número'
                  f' {Fore.LIGHTGREEN_EX}{jogador}{Style.RESET_ALL}.')
            palpites += 1
            print()
            linha()

            # mensagem final -------------------------------------------------------------------------------------------
            if palpites > 1:
                print(f'Você teve {palpites} palpites até acertar')
                linha()

            elif palpites == 1:
                print('Sensacional!!!, acertou com apenas 1 palpite!')
                linha()
                break

            # Validação ------------------------------------------------------------------------------------------------
            tentar_de_novo = str(input('Quer tentar de novo [S/N]:')).strip().upper()[0]
            if tentar_de_novo == 'S':
                gerando = 'Gerando um novo game...'
                for letra in gerando:
                    print(letra, end='', flush=True)
                    sleep(0.25)
                print()
                linha()
                recomeço()
                palpites = 0
                continue

            elif tentar_de_novo == 'N':
                validacao = str(input(Fore.RED + 'Tem certeza que deseja finalizar o programa? (y/n)' + Style.RESET_ALL))
                if validacao.lower() != 'y':
                    linha()
                    recomeço()
                    palpites = 0
                    continue
                else:
                    sleep(2)
                    mensagem = 'Finalizando programa...'
                    for letra in mensagem:
                        print(letra, end='', flush=True)
                        sleep(0.30)
                    print()
                    linha()
                    break
    print('<< VOLTE SEMPRE >>')
    break












