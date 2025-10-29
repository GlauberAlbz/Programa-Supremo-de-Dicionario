'''
    Autores: 
    - Glauber Almeida de Brito
    - Anna Caroline Nascimento Silva
    - Maycon Kaio Silva
    - Luis Henrique N. C. Pozenato
    Turma: 2ºA DS               Data: 22/10/2025

    Atividade de Dicionário - Glauber X Gustavo dos Santos
    Faça um programa que:
    - Tenha tela de login/cadastro
    - Tenha um menu para escolher o programa desejado:
        - Programas: Exercício 1, Exercício 2, Exercício 3, Exercício 4, Exercício 5
    - Tenha uma tela de encerramento
'''
'''
    Exercício 1: Maycon
    - Faça um programa que Cadastre os nomes dos alunos, suas notas e suas médias. No final mostre:
    - O nome do aluno, sua média e sua situação, caso o usuário queria ver mais informações exiba as notas dos bimestre.
'''
'''
    Exercício 2: Glauber
    - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    - Guarde esses resultados em um dicionário em Python.
    - No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
'''
    Exercício 3: Anna
    - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
    - Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    - Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
'''
    Exercício 4: Maycon
    - Crie um programa que gerencie o aproveitamento de jogadores de futebol.
    - O programa vai ler o nome dos jogadores e quantas partidas ele jogou.
    - Depois vair ler a quantidade de gols feitos em cada partida.
    - No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
'''
    Exercício 5: Luis
    - Crie um programa que leia nome, sexo e idade de várias pessoas.
    - Guarde os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
    - No final, Mostre:
        A) Quantas pessoas foram cadastradas
        B) A média de idade
        C) Uma lista com as mulheres
        D) Uma lista de pessoas com idade acima da média
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
bold = "\033[1m"

usuarios_cadastrados = []  # lista composta com [nome, senha]
looplogin = True
looppai = True

while looppai == True:
    while looplogin == True:

        print(cyan + bold + '╔' + '═' * 73 + '╗')
        print('║' + white + f'Início'.center(73) + cyan + '║')
        print('╠' + '═' * 73 + '╣')
        print('║' + white + '1 - Login'.center(73) + cyan + '║')
        print('║' + yellow + '2 - Não possuí login?'.center(73) + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        respostainicio = input("Selecione uma das opções: ")

        if respostainicio == "1":
            sys("cls")
            print(cyan + bold + '╔' + '═' * 73 + '╗')
            print('║' + white + f'Insira o dados do usuário'.center(73) + cyan + '║')
            print('╚' + '═' * 73 + '╝' + reset)
            usernamelogin = input("Digite o nome do usuário: ")
            senhalogin = input("Digite a senha: ")
            login_valido = False

            for usuario in usuarios_cadastrados:
                if usuario[0] == usernamelogin and usuario[1] == senhalogin:
                    print(green + "Login bem-sucedido!" + reset)
                    login_valido = True
                    looplogin = False

            if login_valido == False:
                print(red + "Usuário ou senha incorretos." + reset)
            sleep(1.5)
            sys("cls")

        elif respostainicio == "2":
            sys("cls")
            print(cyan + bold + '╔' + '═' * 73 + '╗')
            print('║' + white + f'Insira o dados do usuário a ser cadastrado'.center(73) + cyan + '║')
            print('╚' + '═' * 73 + '╝' + reset)
            username = input("Digite o nome do usuário: ")
            senha = input("Digite a senha: ")
            existe = False

            for usuario in usuarios_cadastrados:
                if usuario[0] == username:
                    existe = True

            if existe:
                print(red + "Usuário já cadastrado! Tente outro nome." + reset)
                sleep(1.5)
                sys("cls")

            else:
                usuarios_cadastrados.append([username, senha])
                print(green + "Usuário cadastrado com sucesso!" + reset)
                sleep(1.5)
                sys("cls")

        else:
            print(red + "Opção inválida. Tente novamente." + reset)
            sleep(1.5)
            sys("cls")

    sys("cls")

    casos = str(input("Qual programa deseja rodar?"))
    # Glauber - Programa
    match casos:
        case "1":
            1
        case "2":
            2
        case "3":
            3
        case "4":
            4
        case "5":
            5
        case "6":
            6
            
    
    escolha = str()

    while escolha != "1" and escolha != "2" and escolha != "3":
        print(cyan + bold + '╔' + '═' * 73 + '╗')
        print('║' + white + f'Votação encerrada'.center(73) + cyan + '║')
        print('╠' + '═' * 73 + '╣')
        print('║' + white + '1 - Rodar de novo'.center(73) + cyan + '║')
        print('║' + yellow + '2 - Outro Login'.center(73) + cyan + '║')
        print('║' + red + '3 - Encerrar o programa'.center(73) + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)

        escolha = str(input("Selecione uma das opções: ")).strip()
        if escolha == "1":
            looplogin = False  # permanece logado, roda programa de novo
        elif escolha == "2":
            looplogin = True   # volta para loop de login
            sys("cls")
        elif escolha == "3":
            looppai = False  # encerra tudo
        else:
            print(red + "Opção inválida. Tente novamente." + reset)
            sleep(1.5)
            sys("cls")
sys("cls")
print(cyan + bold + '╔' + '═' * 73 + '╗')
print('║' + white + f'Tarefa encerrada'.center(73) + cyan + '║')
print('╠' + '═' * 73 + '╣')
print('║' + green + 'Obrigado pela preferência!'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')

print('║' + yellow + 'Sistema de Login:'.center(73) + cyan + '║')
print('║' + blue + 'Luis Pozenato'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')

print('║' + yellow + 'Programa 1'.center(73) + cyan + '║')
print('║' + blue + 'Glauber Almeida Brito'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')


print('║' + yellow + 'Programa 2'.center(73) + cyan + '║')
print('║' + blue + 'Glauber Almeida Brito'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')

print('║' + yellow + 'Programa 3'.center(73) + cyan + '║')
print('║' + blue + 'Caroline Nascimento Silva'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')


print('║' + yellow + 'Programa 4'.center(73) + cyan + '║')
print('║' + blue + 'Maycon Kaio Silva'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')


print('║' + yellow + 'Programa 5'.center(73) + cyan + '║')
print('║' + blue + 'Luis Henrique Nunes Calazans Pozenato'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')
print('╚' + '═' * 73 + '╝' + reset)
    



