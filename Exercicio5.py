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

pessoadic = dict()
pessoaslist = list()
loop = True

while loop == True:
    user_respo = str
    
    pessoadic['nome'] = str(input("Digite o nome do individuo: "))
    pessoadic['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()
    while pessoadic['sexo'] != "M" and pessoadic['sexo'] != "F": #Possívelmente irei melhorar isso depois, o "Loop_idade" abaixo parece muito mais simples e fácil de se coomprender.

        print("Resposta inválida, tente novamente")
        pessoadic['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()
        
    if pessoadic['sexo'] == "M":
            print(f"{pessoadic['nome']} é do sexo masculino! ")

    elif pessoadic['sexo'] == "F":
        print(f"{pessoadic['nome']} é do sexo feminino. ")

    #bloco a corrigir
    loop_idade = False
    while loop_idade == False:
        
        entradaIdade = (input("Digite a idade do Individuo: "))
    
        if entradaIdade.isdigit():

            pessoadic['idade'] = int(entradaIdade)
            print(f"A pessoa registrada possuí: {pessoadic['idade']} Anos!")
            loop_idade = True

        elif pessoadic['idade'] != entradaIdade:
            entradaIdade = int()

            if entradaIdade < 0:
                print("Ué, essa pessoas está no útero da mãe ainda?")

        else:
            print("Digite uma idade Válida por favor.") #Possivelmente fazer um if dentro do Else KKKKKKKKKKKKKKK
            
    pessoaslist.append(pessoadic.copy())

    while user_respo != "S" and user_respo != "N":
        user_respo = str(
            input('Deseja registrar outra pessoa? (S/N): ')).upper().strip()
        if user_respo == 'N':
            loop = False
        elif user_respo == 'S':
            loop = True
        else:
            print("\nResposta inválida, tente novamente\n")
print("calculo doidão hahaahahhahahaa\n")
print(pessoaslist)
