'''
    Autores: 
    - Luis Henrique N. C. Pozenato
    Turma: 2ºA DS               Data: 22/10/2025

    Exercício 5: Luis
    - Crie um programa que leia nome, sexo e idade de várias pessoas.
    - Guarde os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
    - No final, Mostre:
        A) Quantas pessoas foram cadastradas
        B) A média de idade
        C) Uma lista com as mulheres
        D) Uma lista de pessoas com idade acima da média
'''

from os import system as sys
from time import sleep

sys("cls")

pessoa = dict()
pessoas = list()
loop = True

while loop == True:
    user_respo = str
    

    pessoa['nome'] = str(input("Digite o nome do individuo: "))
    while pessoa['sexo'] != "M" and pessoa['sexo'] != "F":

        pessoa['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()
        if pessoa['sexo'] == "M":
            print(f"{{pessoas['nome']}} é do sexo masculino. ")
        elif pessoa['sexo'] == "F":
            print(f"{{pessoas['nome']}} é do sexo feminino. ")
        else:
            print("Resposta inválida, tente novamente")
            print(pessoa['sexo'])
        
    pessoa['idade'] = int(input("Digite a idade do Individuo: "))
    pessoas.append(pessoa.copy())

    while user_respo != "S" and user_respo != "N":
        user_respo = str(input('Deseja registrar outra pessoa? (S/N): ')).upper().strip()
        if user_respo == 'N':
            loop = False
        elif user_respo == 'S':
            loop = True
        else:
            print("\nResposta inválida, tente novamente\n")
print("calculo doidão hahaahahhahahaa\n")  
print(pessoas) 
