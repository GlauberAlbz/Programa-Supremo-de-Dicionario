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

jogadores1 = {'nick': 'Glauber', 'dado': 6}
jogadores2 = {'nick': 'Anna', 'dado': 5}
jogadores3 = {'nick': 'Maycon', 'dado': 3}
jogadores4 = {'nick': 'Luis', 'dado': 4}
lista_jogadores = [jogadores1, jogadores2, jogadores3, jogadores4]

sys('cls')
for c in range(0,4):

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


# Exibição do resultado
print('O resultado dos jogadores são:')

print(f'{lista_jogadores[0]['nick']} tirou {lista_jogadores[0]['dado']} no dado')
print(f'{lista_jogadores[1]['nick']} tirou {lista_jogadores[1]['dado']} no dado')
print(f'{lista_jogadores[2]['nick']} tirou {lista_jogadores[2]['dado']} no dado')
print(f'{lista_jogadores[3]['nick']} tirou {lista_jogadores[3]['dado']} no dado')

# Cálculo do ranking dos jogadores
for i in range(len(lista_jogadores)):
    for j in range(i + 1, len(lista_jogadores)):
        if lista_jogadores[i]['dado'] < lista_jogadores[j]['dado']:
            lista_jogadores[i], lista_jogadores[j] = lista_jogadores[j], lista_jogadores[i]

# Ranking dos Jogadores
print('🏆 O ranking dos jogadores:')
print(f'1º lugar: {lista_jogadores[0]['nick']} com {lista_jogadores[0]['dado']}')
print(f'2º lugar: {lista_jogadores[1]['nick']} com {lista_jogadores[1]['dado']}')
print(f'3º lugar: {lista_jogadores[2]['nick']} com {lista_jogadores[2]['dado']}')
print(f'4º lugar: {lista_jogadores[3]['nick']} com {lista_jogadores[3]['dado']}')
