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

jogadores = dict()
lista_jogadores = list()

sys('cls')
for c in range(0,4):

    sys('cls')

    print(f'Jogador {c+1}')
    jogadores['nick'] = str(input('Por favor digite o seu nickname antes de iniciar: '))
    jogadores['dado'] = rd.randint(1, 6)
    lista_jogadores.append(jogadores.copy())
    
    sys('cls')

    print(f'Jogador {c+1}')
    print(f'Seja bem vindo(a) {lista_jogadores[c]['nick']}!')
    print('Aqui você irá disputar com outros jogadores em uma competição de dados.')
    print('O jogador que tirar o maior valor vence o jogo!')
    input('Se estiver pronto para começar pressione ENTER...\n')

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
        print(f'Que pena {lista_jogadores[c]['nick']}, você tirou {lista_jogadores[c]['dado']}...')
        input('Pressione ENTER para prosseguir...')
    elif lista_jogadores[c]['dado'] > 2 and lista_jogadores[c]['dado'] <= 4:
        print(f'{lista_jogadores[c]['nick']}, você tirou {lista_jogadores[c]['dado']}.')
        input('Pressione ENTER para prosseguir...')
    elif lista_jogadores[c]['dado'] > 4 and lista_jogadores[c]['dado'] < 6:
        print(f'Parabéns {lista_jogadores[c]['nick']}! Você tirou {lista_jogadores[c]['dado']}!')
        input('Pressione ENTER para prosseguir...')
    else:
        print(f'Que incrível {lista_jogadores[c]['nick']}!!! Você tirou {lista_jogadores[c]['dado']}!!!')
        input('Pressione ENTER para prosseguir...')


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

for letra in 'O ranking dos jogadores:':
    print(letra, end='', flush=True)
    sleep(0.05)

            
