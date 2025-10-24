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


# Ranking dos Jogadores
print('O ranking dos jogadores:')

# Cálculo do ranking dos jogadores
lista_valores_dados = list()
for values in range(0,4):
    lista_valores_dados.append(lista_jogadores[values])
lista_valores_dados.sort(reverse=True)
print(lista_valores_dados)
