"""
Crie um programa onde o usuário tente adivinha
o número que o computador está "pensando" e mostre
na tela uma mensagem de validação.
"""

import emoji
from random import randint
from time import sleep
def linha():
    print('_' * 60)


computador = randint(0, 10)
palpites = 0

while True:
    print()
    print('\033[33mEstou pensando em um número de 0 a 10\033[m')
    jogador = int(input('Em que número estou pensando?:'))
    print(f'hmmm... Será que estou pensando no número {jogador}')
    sleep(3)
    linha()
    # Sistema de condições ---------------------------------------------------------------------------------------------
    if jogador != computador and jogador > computador:
        print(f'Não pensei no número \033[31m',jogador,'\033[m')
        print('Menos...')
        palpites += 1
        linha()
    elif jogador != computador and jogador < computador:
        print(f'Não pensei no número \033[31m', jogador, '\033[m')
        print('Mais...')
        palpites += 1
        linha()
    else:
        print(' ')
        print(f'\033[1;35m👏 PARABÉNS 👏\033[m, eu havia pensando no numero\033[34m',jogador,'\033[m.')
        palpites += 1
        break

# mensagem final -------------------------------------------------------------------------------------------------------
if palpites > 1:
    print(f'Você teve {palpites} palpites até acertar')
    linha()
elif palpites == 1:
    print('Sensacional, acertou com apenas 1 palpite!')
    linha()


