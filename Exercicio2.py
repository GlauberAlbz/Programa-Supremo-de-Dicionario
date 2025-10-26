'''
    Autores: 
    - Glauber Almeida de Brito
    Turma: 2ºA DS               Data: 22/10/2025

    Exercício 2: Glauber
    - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    - Guarde esses resultados em um dicionário em Python.
    - No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

import random as rd
from os import system as sys
from time import sleep

black= "\033[0;30m" 
red= "\033[0;31m"
green= "\033[0;32m"
yellow= "\033[0;33m" 
blue= "\033[0;34m"
purple= "\033[0;35m"
cyan= "\033[0;36m"
orange = "\033[38;5;208m" 
pink= "\033[38;5;198m"
brown= "\033[38;5;130m"
white = "\033[0;37m"
gray = white + black
reset= "\033[0m"

jogadores = dict()
lista_jogadores = list()

sys('cls')
for c in range(0,4):

    sys('cls')

    print(cyan + '╔' + '═' * 73 + '╗')
    print(f'║' + yellow + f'Jogador {c+1}'.center(73) + cyan + '║')
    print('╚' + '═' * 73 + '╝' + reset)
    jogadores['nick'] = str(input('Por favor digite o seu nickname antes de iniciar: '))
    jogadores['dado'] = rd.randint(1, 6)
    lista_jogadores.append(jogadores.copy())
    
    sys('cls')

    print(cyan + '╔' + '═' * 73 + '╗')
    print('║' + yellow + f'Jogador {c+1}'.center(73) + cyan + '║')
    print('╠' + '═' * 73 + '╣')
    print('║' + reset + f'Seja bem vindo(a) {lista_jogadores[c]['nick']}!'.center(73) + cyan + '║')
    print('║' + reset + 'Aqui você irá disputar com outros jogadores em uma competição de dados.'.center(73) + cyan + '║')
    print('║' + reset + 'O jogador que tirar o maior valor vence o jogo!'.center(73) + cyan + '║')
    print('╚' + '═' * 73 + '╝' + reset)
    input('Se estiver pronto para começar pressione ENTER...\n')

    sys('cls')

    for letra in '🎲 Vamos rolar os dados! 🎲':
        print(letra, end='', flush=True)
        sleep(0.05)
    sleep(0.25)

    sys('cls')

    for pontinhos in range(0,6):
        for ponto in range(0,3):
            print('.', end='', flush=True)
            sleep(0.1)
        sys('cls')

    if lista_jogadores[c]['dado'] <= 2:
        print(cyan + '╔' + '═' * 73 + '╗')
        print('║' + reset + f'Que pena {lista_jogadores[c]['nick']}, você tirou {lista_jogadores[c]['dado']}...'.center(73) + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        input('Pressione ENTER para prosseguir...')
    elif lista_jogadores[c]['dado'] > 2 and lista_jogadores[c]['dado'] <= 4:
        print(cyan + '╔' + '═' * 73 + '╗')
        print('║' + reset + f'{lista_jogadores[c]['nick']}, você tirou {lista_jogadores[c]['dado']}.'.center(73) + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        input('Pressione ENTER para prosseguir...')
    elif lista_jogadores[c]['dado'] > 4 and lista_jogadores[c]['dado'] < 6:
        print(cyan + '╔' + '═' * 73 + '╗')
        print('║' + reset + f'Parabéns {lista_jogadores[c]['nick']}! Você tirou {lista_jogadores[c]['dado']}!'.center(73) + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        input('Pressione ENTER para prosseguir...')
    else:
        print(cyan + '╔' + '═' * 73 + '╗')
        print('║' + reset + f'Que incrível {lista_jogadores[c]['nick']}!!! Você tirou {lista_jogadores[c]['dado']}!!!'.center(73) + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        input('Pressione ENTER para prosseguir...')

sys('cls')

for letra in 'O resultado dos jogadores são:':
    print(letra, end='', flush=True)
    sleep(0.05)
print()

# Jogador 1:
for letra in f'{lista_jogadores[0]['nick']} tirou ':
    print(letra, end='', flush=True)
    sleep(0.1)
sleep(1)
for letra in f'{lista_jogadores[0]['dado']} no dado.':
    print(letra, end='', flush=True)
    sleep(0.05)
print()

# Jogador 2:
for letra in f'{lista_jogadores[1]['nick']} tirou ':
    print(letra, end='', flush=True)
    sleep(0.1)
sleep(1)
for letra in f'{lista_jogadores[1]['dado']} no dado.':
    print(letra, end='', flush=True)
    sleep(0.05)
print()

# Jogador 3:
for letra in f'{lista_jogadores[2]['nick']} tirou ':
    print(letra, end='', flush=True)
    sleep(0.1)
sleep(1)
for letra in f'{lista_jogadores[2]['dado']} no dado.':
    print(letra, end='', flush=True)
    sleep(0.05)
print()

# Jogador 4:
for letra in f'{lista_jogadores[3]['nick']} tirou ':
    print(letra, end='', flush=True)
    sleep(0.1)
sleep(1)
for letra in f'{lista_jogadores[3]['dado']} no dado.':
    print(letra, end='', flush=True)
    sleep(0.05)
print()

sys('cls')

# Cálculo do ranking dos jogadores
for i in range(len(lista_jogadores)):
    for j in range(i + 1, len(lista_jogadores)):
        if lista_jogadores[i]['dado'] < lista_jogadores[j]['dado']:
            lista_jogadores[i], lista_jogadores[j] = lista_jogadores[j], lista_jogadores[i]

# Ranking dos Jogadores
print(cyan + '╔' + '═' * 73 + '╗')
print('╠' + reset + '🏆 O ranking dos jogadores:'.center(72) + cyan + '╣')
print('║' + yellow + f'1º lugar: {lista_jogadores[0]['nick']} com {lista_jogadores[0]['dado']}'.center(73) + cyan + '║')
print('║' + gray + f'2º lugar: {lista_jogadores[1]['nick']} com {lista_jogadores[1]['dado']}'.center(73) + cyan + '║')
print('║' + brown + f'3º lugar: {lista_jogadores[2]['nick']} com {lista_jogadores[2]['dado']}'.center(73) + cyan + '║')
print('║' + reset + f'4º lugar: {lista_jogadores[3]['nick']} com {lista_jogadores[3]['dado']}'.center(73) + cyan + '║')
print('╚' + '═' * 73 + '╝' + reset)
