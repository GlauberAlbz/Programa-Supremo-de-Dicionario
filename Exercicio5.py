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
reset= "\033[0m" 

from os import system as sys
from time import sleep

sys("cls")

pessoadic = dict()
pessoaslist = list()
loop = True



while loop == True:
    user_respo = str()

    loop_nome = False
    while loop_nome == False:

        print((cyan) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
        print('╚' + '═' * 73 + '╝\n' + reset)
        entradanome = str(input("Digite o nome do individuo: ")).capitalize()

        if entradanome.replace(" ", "").isalpha():
            pessoadic['nome'] = entradanome
            loop_nome = True
            sys("cls")
        else:
            print("Números e Caracteres desse tipo não são permitidos....")
            sleep(1)
            sys("cls")

    print((cyan) + '╔' + '═' * 73 + '╗')
    print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
    print('╚' + '═' * 73 + '╝\n' + reset)
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

quantidadePessoas = len(pessoaslist)


premedia = int(0)
contmedia = int(0)
for idades in pessoaslist:
    premedia += idades["idade"]
    contmedia += 1
media = int(premedia / contmedia)



mulhereslist = list()
for mulheres in pessoaslist:
    if mulheres["sexo"] == "F":
        mulhereslist.append(mulheres.copy())

acimaMedia = list()
for m in pessoaslist:
    if m["idade"] > media:
        acimaMedia.append(m.copy())


print(f"{quantidadePessoas} pessoas foram cadastradas\n")

print(f"A média de idade entre essas pessoas é: {media}")

tem_mulher = False
for pessoa in pessoaslist:
    if pessoa["sexo"] == "F":
        tem_mulher = True
        break
    else:
        print("essa lista não possuí mulheres")

if tem_mulher == True:
    for m in mulhereslist:
        print(m["nome"])



if contmedia > 1:
    for pessoa in acimaMedia:
        print(f"{pessoa['nome']} com {pessoa['idade']} anos")
else:
    print("Essa lista possuí apenas 1 candidato, logo ninguém está acima da média.")





