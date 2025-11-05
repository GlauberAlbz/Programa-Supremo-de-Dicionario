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
bold = "\033[1m"

from os import system as sys
from time import sleep

sys("cls")

pessoadic = dict()
pessoaslist = list()
loop5 = True

print(cyan + bold + '╔' + '═' * 73 + '╗')
print('║' + (yellow) + f'O programa irá ler: nome, sexo e idade de várias pessoas.'.center(73) + (cyan) + '║')
print('║' + ' ' * 73 + cyan + '║')
print('║' + (orange) + f'no final ele mostrará:'.center(73) + (cyan) + '║')
print('║' + (blue) + f'Quantas pessoas foram cadastradas.'.center(73) + (cyan) + '║')
print('║' + (blue) + f'A média de idade.'.center(73) + (cyan) + '║')
print('║' + (blue) + f'Uma lista com as mulheres.'.center(73) + (cyan) + '║')
print('║' + (blue) + f'Uma lista de pessoas com idade acima da média.'.center(73) + (cyan) + '║')
print('║' + ' ' * 73 + cyan + '║')
print('║' + (purple) + f'Pressione ENTER para continuar...'.center(73) + (cyan) + '║')
print('╚' + '═' * 73 + '╝' + reset)
input("")

while loop5 == True:
    sys('cls')
    
    user_respo = str()

    loop_nome = False
    while loop_nome == False:
        

        sys('cls')

        print((cyan) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        entradanome = str(input("Digite o nome do individuo: ")).capitalize()

        if entradanome.replace(" ", "").isalpha():
            pessoadic['nome'] = entradanome
            loop_nome = True
            sys("cls")
        else:
            print((red) + '╔' + '═' * 73 + '╗')
            print('║' + (yellow) + f'Números e Caracteres desse tipo não são permitidos....'.center(73) + (red) + '║')
            print('╚' + '═' * 73 + '╝' + reset)
            input("Pressione ENTER para continuar...")
            sys("cls")

    print((cyan) + '╔' + '═' * 73 + '╗')
    print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
    print('╚' + '═' * 73 + '╝' + reset)
    pessoadic['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()
    
    while pessoadic['sexo'] != "M" and pessoadic['sexo'] != "F":
        print((red) + '╔' + '═' * 73 + '╗')
        print('║' + (yellow) + f'Resposta inválida, tente novamente'.center(73) + (red) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        input("Pressione ENTER para continuar...")
        sys("cls")
        print((cyan) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        pessoadic['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()

    if pessoadic['sexo'] == "M":
        sys("cls")
        print((blue) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'{pessoadic['nome']} é do sexo masculino!..'.center(73) + (blue) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        input("Pressione ENTER para continuar...")

    elif pessoadic['sexo'] == "F":
        sys("cls")
        print((pink) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'{pessoadic['nome']} é do sexo feminino!..'.center(73) + (pink) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        input("Pressione ENTER para continuar...")
        
    loop_idade = False
    while loop_idade == False:
        sys("cls")
        print((cyan) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        
        entradaIdade = (input("Digite a idade do Individuo: "))
        sys("cls")

        if entradaIdade.isdigit():
            entradaIdade = int(entradaIdade)

            if entradaIdade > 116:
                
                print((red) + '╔' + '═' * 105 + '╗')
                print('║' + (yellow) + f'A pessoa mais velha do mundo possuí 116 anos atualmente, digite uma idade onde a pessoa possa estar viva.'.center(73) + (red) + '║')
                print('╚' + '═' * 105 + '╝' + reset)
                input("Pressione ENTER para continuar...")

            elif entradaIdade == 0 and pessoadic['sexo'] == "F":
                pessoadic['idade'] = int(entradaIdade)
                print((pink) + '╔' + '═' * 73 + '╗')
                print('║' + (reset) + f'vou considerar que a {pessoadic['nome']} tem alguns meses de idade'.center(73) + (pink) + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                input("Pressione ENTER para continuar...")
                loop_idade = True
            elif entradaIdade == 0 and pessoadic['sexo'] == "M":
                pessoadic['idade'] = int(entradaIdade) 
                print((blue) + '╔' + '═' * 73 + '╗')
                print('║' + (reset) + f'vou considerar que o {pessoadic['nome']} tem alguns meses de idade.'.center(73) + (blue) + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                input("Pressione ENTER para continuar...")
                loop_idade = True

            elif entradaIdade == 1:
                pessoadic['idade'] = int(entradaIdade)
                print((cyan) + '╔' + '═' * 73 + '╗')
                print('║' + (reset) + f'{pessoadic['nome']} possuí {pessoadic['idade']} Ano de idade!'.center(73) + (cyan) + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                input("Pressione ENTER para continuar...")
                loop_idade = True
            elif entradaIdade > 0:
                pessoadic['idade'] = int(entradaIdade)
                print((cyan) + '╔' + '═' * 73 + '╗')
                print('║' + (reset) + f'{pessoadic['nome']} possuí {pessoadic['idade']} Anos!'.center(73) + (cyan) + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                input("Pressione ENTER para continuar...")
                loop_idade = True

        else:
            print((red) + '╔' + '═' * 73 + '╗')
            print('║' + (yellow) + f'Digite uma idade Válida por favor.'.center(73) + (red) + '║')
            print('╚' + '═' * 73 + '╝' + reset)
            input("Pressione ENTER para continuar...")
        
    pessoaslist.append(pessoadic.copy())

    while user_respo != "S" and user_respo != "N":

        sys("cls")
        print((cyan) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'Deseja registrar outra pessoa? (S/N)'.center(73) + (cyan) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        user_respo = str(input('Sua Resposta: ')).upper().strip()
        if user_respo == 'N':
            loop5 = False
        elif user_respo == 'S':
            loop5 = True
        else:
            print((red) + '╔' + '═' * 73 + '╗')
            print('║' + (yellow) + f'Resposta inválida, tente novamente'.center(73) + (red) + '║')
            print('╚' + '═' * 73 + '╝' + reset)

sys("cls")


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

print((cyan) + '╔' + '═' * 73 + '╗')
print('║' + (reset) + f'Quantidade de pessoas Cadastradas'.center(73) + (cyan) + '║')
print('╚' + '═' * 73 + '╝\n' + reset)
print(f"• {quantidadePessoas}\n")

print((green) + "=" * 75 + (reset))

print((yellow) + '\n╔' + '═' * 73 + '╗')
print('║' + (reset) + f'A média de idade entre essas pessoas é:'.center(73) + (yellow) + '║')
print('╚' + '═' * 73 + '╝\n' + reset)
print(f"• {media} Anos\n")



tem_mulher = False
for pessoa in pessoaslist:
    if pessoa["sexo"] == "F":
        tem_mulher = True
        break

if tem_mulher == False:
    print((green) + "=" * 75 + (reset))
    print((pink) + '\n╔' + '═' * 73 + '╗')
    print('║' + (reset) + f'Nenhuma mulher foi registrada.'.center(73) + (pink) + '║')
    print('╚' + '═' * 73 + '╝\n' + reset)
   
    
if tem_mulher == True:
    print((pink) + '\n╔' + '═' * 73 + '╗')
    print('║' + (reset) + f'Lista de mulheres registradas'.center(73) + (pink) + '║')
    print('╚' + '═' * 73 + '╝\n' + reset)
    for m in mulhereslist:
        print(f'• {m["nome"]}')
    print("")


print((green) + "=" * 75 + (reset))

verificar = False

if contmedia > 1:
    print((purple) + '\n╔' + '═' * 73 + '╗')
    print('║' + (reset) + f'As pessoas com idade acima da média são:'.center(73) + (purple) + '║')
    print('╚' + '═' * 73 + '╝\n' + reset)
    for pessoa in acimaMedia:
        print(f"• {pessoa['nome']} com {pessoa['idade']} anos")

elif media == 0 and verificar == False:
    print((purple) + '\n╔' + '═' * 81 + '╗')
    print('║' + (reset) + f'Todo mundo tem alguns meses de idade, então não posso definir uma média.'.center(73) + (purple) + '║')
    print('╚' + '═' * 81 + '╝\n' + reset)

else:
    print((purple) + '\n╔' + '═' * 73 + '╗')
    print('║' + (reset) + f'Essa lista possuí apenas 1 candidato, logo ninguém está acima da média.'.center(73) + (purple) + '║')
    print('╚' + '═' * 73 + '╝\n' + reset)
    verificar = True
print("")







