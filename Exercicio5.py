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
    loop_nome = False
    while loop_nome == False:

        entradanome = str(input("Digite o nome do individuo: ")).capitalize()

        if entradanome.replace(" ", "").isalpha():
            pessoadic['nome'] = entradanome
            loop_nome = True
        else:
            print("Números e Caracteres desse tipo não são permitidos....")

    pessoadic['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()
    
    while pessoadic['sexo'] != "M" and pessoadic['sexo'] != "F":

        print("Resposta inválida, tente novamente")
        pessoadic['sexo'] = str(
            input("Digite o sexo do Individuo: (M/F) ")).upper().strip()

    if pessoadic['sexo'] == "M":
        print(f"{pessoadic['nome']} é do sexo masculino! ")

    elif pessoadic['sexo'] == "F":
        print(f"{pessoadic['nome']} é do sexo feminino. ")

    loop_idade = False
    while loop_idade == False:

        entradaIdade = (input("Digite a idade do Individuo: "))
    
        if entradaIdade.isdigit():
            entradaIdade = int(entradaIdade)

            if entradaIdade > 116:
                print('A pessoa mais velha do mundo possuí 116 anos atualmente, digite uma idade onde a pessoa possa estar viva.')

            elif entradaIdade == 0 and pessoadic['sexo'] == "F":
                pessoadic['idade'] = int(entradaIdade) 
                print(f" vou considerar que a {pessoadic['nome']} tem alguns meses de idade...")
                loop_idade = True
            elif entradaIdade == 0 and pessoadic['sexo'] == "M":
                pessoadic['idade'] = int(entradaIdade) 
                print(f"vou considerar que o {pessoadic['nome']} tem alguns meses de idade...")
                loop_idade = True

            elif entradaIdade == 1:
                pessoadic['idade'] = int(entradaIdade)
                print(f"{pessoadic['nome']} possuí {pessoadic['idade']} Ano de idade!")
                loop_idade = True
            elif entradaIdade > 0:
                pessoadic['idade'] = int(entradaIdade)
                print(f"{pessoadic['nome']} possuí {pessoadic['idade']} Anos!")
                loop_idade = True

        else:
            print("Digite uma idade Válida por favor.")
        
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

print(pessoaslist)


