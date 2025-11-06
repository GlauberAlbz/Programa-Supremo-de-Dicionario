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
from os import name as os_name
from time import sleep
import datetime as dt
import copy

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

def limpar():
    sys('cls' if os_name == 'nt' else 'clear')

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
            limpar()
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
            limpar()

        elif respostainicio == "2":
            limpar()
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
                limpar()

            else:
                usuarios_cadastrados.append([username, senha])
                print(green + "Usuário cadastrado com sucesso!" + reset)
                sleep(1.5)
                limpar()

        else:
            print(red + "Opção inválida. Tente novamente." + reset)
            sleep(1.5)
            limpar()
    casos = str()
    while casos not in ["0","1","2","3","4","5",]:
        limpar()
        print(cyan + bold + '╔' + '═' * 73 + '╗')
        print('║' + white + 'Lista de Programas'.center(73) + cyan + '║')
        print('╠' + '═' * 73 + '╣')
        print('║' + ' ' * 73 + cyan + '║')

        print('║' + pink + '1 - Sistema de gerenciamento de notas.'.center(73) + cyan + '║')
        print('║' + ' ' * 73 + cyan + '║')

        print('║' + red + '2 - Jogo de rolar dado.'.center(73) + cyan + '║')
        print('║' + ' ' * 73 + cyan + '║')

        print('║' + blue + '3 - Consultor de Carteira de Trabalho.'.center(73) + cyan + '║')
        print('║' + ' ' * 73 + cyan + '║')
    
        print('║' + orange + '4 - Análise de aproveitamendo de jogadores.'.center(73) + cyan + '║')
        print('║' + ' ' * 73 + cyan + '║')

        print('║' + yellow + '5 - Pesquisa em um grupo de pessoas.'.center(73) + cyan + '║')
        print('║' + ' ' * 73 + cyan + '║')
        print('║' + purple + '0 - Encerrar Programa.'.center(73) + cyan + '║')
        print('║' + ' ' * 73 + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)

        casos = str(input("Qual programa deseja rodar?: ")).strip()

        if casos not in ["0","1","2","3","4","5",]:
            limpar()
            print((red) + '╔' + '═' * 73 + '╗')
            print('║' + red + 'Opção inexistente, Tente novamente!'.center(73) + red + '║')
            print('╚' + '═' * 73 + '╝\n' + reset)
            input("")
    
    match casos:
        case "1":
            alunos_EFI = list()  # Ensino Fundamental I
            alunos_EFII = list()  # Ensino Fundamental II
            alunos_EM = list()  # Ensino Médio
            aluno = dict()

            bimestre_1_EF = dict()
            bimestre_2_EF = dict()
            bimestre_3_EF = dict()
            bimestre_4_EF = dict()
            boletim_EF = [bimestre_1_EF, bimestre_2_EF, bimestre_3_EF, bimestre_4_EF]
            materias_EF = ['Lingua Portuguesa', 'Matemática', 'Ciências', 'História', 'Geografia', 'Inglês', 'Artes',
                           'Educação Física']

            bimestre_1_EM = dict()
            bimestre_2_EM = dict()
            bimestre_3_EM = dict()
            bimestre_4_EM = dict()
            boletim_EM = [bimestre_1_EM, bimestre_2_EM, bimestre_3_EM, bimestre_4_EM]
            materias_EM = ['Lingua Portuguesa', 'Matemática', 'História', 'Geografia', 'Física', 'Química', 'Biologia',
                           'Sociologia', 'Filosofia', 'Inglês', 'Artes', 'Educação Física']

            resposta = str()
            resposta_escolaridade = str()
            resposta_aluno = str()
            indice = int()
            nota = int()

            skip = False  # Serve para pular partes do programa para evitar casos de redundância
            registro_boletim = False
            visualizar_boletim = False

            # 4 variáveis booleanas principais, servem para sustentar os loops principais do programa
            loop_ex1 = True
            cadastrar = False
            analisar = False
            avaliar = False

            while loop_ex1:
                if not skip:
                    limpar()
                    # cabeçalho estilizado (menu)
                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + yellow + 'O que deseja fazer?'.center(73) + cyan + '║')
                    print('╠' + '═' * 73 + '╣')
                    print('║' + reset + '1 - Cadastrar alunos'.center(73) + cyan + '║')
                    print('║' + reset + '2 - Analisar alunos'.center(73) + cyan + '║')
                    print('║' + reset + '3 - Avaliar alunos'.center(73) + cyan + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    resposta = str(input('Digite sua resposta - (1/2/3): ')).strip()

                    while resposta not in ['1', '2', '3']:
                        limpar()
                        print(cyan + '╔' + '═' * 73 + '╗')
                        print('║' + yellow + 'O que deseja fazer?'.center(73) + cyan + '║')
                        print('╠' + '═' * 73 + '╣')
                        print('║' + reset + '1 - Cadastrar alunos'.center(73) + cyan + '║')
                        print('║' + reset + '2 - Analisar alunos'.center(73) + cyan + '║')
                        print('║' + reset + '3 - Avaliar alunos'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝' + reset)
                        print(red + 'Digito inválido! Tente novamente.' + reset)
                        resposta = str(input('Digite sua resposta - (1/2/3): ')).strip()

                    match resposta:
                        case '1':
                            cadastrar = True
                            analisar = False
                            avaliar = False
                            resposta = ''
                        case '2':
                            cadastrar = False
                            analisar = True
                            avaliar = False
                            resposta = ''
                        case '3':
                            cadastrar = False
                            analisar = False
                            avaliar = True
                            resposta = ''

                while cadastrar:
                    limpar()

                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + yellow + ' CADASTRO DE ALUNO '.center(73) + cyan + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    print()

                    aluno['nome'] = str(input('Digite o nome do(da) aluno(a): '))
                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + yellow + 'Grades:'.center(73) + cyan + '║')
                    print('╠' + '═' * 73 + '╣')
                    for grades in range(1, 10):
                        print('║' + f'{grades} - {grades}º ano do Ensino Fundamental'.center(73) + '║')
                    print('╠' + '═' * 73 + '╣')
                    for grades in range(1, 4):
                        print('║' + f'{9 + grades} - {grades}ª série do Ensino Médio'.center(73) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)

                    aluno['grade'] = str(input('Digite a grade do(da) aluno(a): ')).strip()

                    while aluno['grade'] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
                        limpar()

                        print(cyan + '╔' + '═' * 73 + '╗')
                        print('║' + yellow + ' CADASTRO DE ALUNO '.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝' + reset)
                        print()
                        print(f'Digite o nome do(da) aluno(a): {aluno['nome']}')
                        print(cyan + '╔' + '═' * 73 + '╗')
                        print('║' + yellow + 'Grades:'.center(73) + cyan + '║')
                        print('╠' + '═' * 73 + '╣')
                        for grades in range(1, 10):
                            print('║' + f'{grades} - {grades}º ano do Ensino Fundamental'.center(73) + '║')
                        print('╠' + '═' * 73 + '╣')
                        for grades in range(1, 4):
                            print('║' + f'{9 + grades} - {grades}ª série do Ensino Médio'.center(73) + '║')
                        print('╚' + '═' * 73 + '╝' + reset)
                        print(red + 'Digito errado' + reset)
                        aluno['grade'] = str(input('Digite a grade do(da) aluno(a): '))

                    aluno['grade'] = int(aluno['grade'])

                    # Adicionando a escolaridade do aluno
                    if aluno['grade'] > 0 and aluno['grade'] < 6:
                        aluno['escolaridade'] = 'Ensino Fundamental I'
                    elif aluno['grade'] > 5 and aluno['grade'] < 10:
                        aluno['escolaridade'] = 'Ensino Fundamental II'
                    else:
                        aluno['escolaridade'] = 'Ensino Médio'
                        aluno['grade'] = aluno['grade'] - 9

                    # Adicionando o aluno em uma lista com outros da mesma escolaridade
                    if aluno['escolaridade'] == 'Ensino Fundamental I':
                        alunos_EFI.append(aluno.copy())
                        aluno = dict()
                    elif aluno['escolaridade'] == 'Ensino Fundamental II':
                        alunos_EFII.append(aluno.copy())
                        aluno = dict()
                    else:
                        alunos_EM.append(aluno.copy())
                        aluno = dict()

                    print(green + 'Você deseja cadastrar outro aluno?' + reset)
                    resposta = str(input('Digite sua resposta - (S/N) ')).strip().upper()

                    while resposta not in ['S', 'N']:
                        limpar()

                        print(green + 'Você deseja cadastrar outro aluno?' + reset)
                        print(red + 'Digito inválido! Tente novamente.' + reset)
                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                    if resposta == 'S':
                        cadastrar = True
                        analisar = False
                        avaliar = False
                        resposta = ''
                    else:
                        cadastrar = False
                        analisar = False
                        avaliar = False
                        skip = False
                        resposta = ''

                while analisar:
                    limpar()

                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + yellow + 'O aluno que você deseja analisar é de qual escolaridade?'.center(73) + cyan + '║')
                    print('╠' + '═' * 73 + '╣')
                    print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                    print('║' + reset + '1 - Ensino Fundamental I'.center(73) + cyan + '║')
                    print('║' + reset + '2 - Ensino Fundamental II'.center(73) + cyan + '║')
                    print('║' + reset + '3 - Ensino Médio'.center(73) + cyan + '║')
                    print('╚' + '═' * 73 + '╝' + reset)

                    resposta_escolaridade = str(input('Digite sua resposta - (0/1/2/3): ')).strip()

                    while resposta_escolaridade not in ['0', '1', '2', '3']:
                        limpar()

                        print(cyan + '╔' + '═' * 73 + '╗')
                        print('║' + yellow + 'O aluno que você deseja analisar é de qual escolaridade?'.center(73) + cyan + '║')
                        print('╠' + '═' * 73 + '╣')
                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                        print('║' + reset + '1 - Ensino Fundamental I'.center(73) + cyan + '║')
                        print('║' + reset + '2 - Ensino Fundamental II'.center(73) + cyan + '║')
                        print('║' + reset + '3 - Ensino Médio'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝' + reset)
                        print(red + 'Digito inválido! Tente novamente.' + reset)
                        resposta_escolaridade = str(input('Digite sua resposta - (0/1/2/3): ')).strip()

                    if resposta_escolaridade == '1':
                        if len(alunos_EFI) > 0:
                            limpar()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()

                            for cont, al in enumerate(alunos_EFI):
                                print(
                                    cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                        69) + cyan + '║' + reset)
                            print()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Você deseja analisar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                for cont, al in enumerate(alunos_EFI):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)
                                print()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Você deseja analisar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                visualizar_boletim = True
                                resposta = ''
                                limpar()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()

                                for cont, al in enumerate(alunos_EFI):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)

                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + f'Qual aluno você deseja analisar?'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                opcoes_validas = [str(i + 1) for i in range(len(alunos_EFI))]

                                while resposta_aluno not in opcoes_validas:
                                    limpar()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EFI):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + f'Qual aluno você deseja analisar?'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(red + 'Digito Inválido! Tente novamente.' + reset)
                                    resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                indice = int(resposta_aluno) - 1

                                if len(alunos_EFI[indice]) <= 3:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(f"{green}Aluno:{reset} {alunos_EFI[indice]['nome']}")
                                    print(f"{green}Grade:{reset} {alunos_EFI[indice]['grade']}° Ano")
                                    print(f"{green}Escolaridade:{reset} {alunos_EFI[indice]['escolaridade']}")
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'O aluno não possui boletim registrado.'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                    while resposta not in ['S', 'N']:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EFI[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EFI[indice]['grade']}° Ano")
                                        print(f"{green}Escolaridade:{reset} {alunos_EFI[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'O aluno não possui boletim registrado.'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print(
                                            '║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Digito Inválido! Tente novamente.' + reset)
                                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                    if resposta == 'S':
                                        cadastrar = False
                                        analisar = False
                                        avaliar = True
                                        skip = True
                                        resposta = ''
                                        break
                                    else:
                                        skip = False
                                        cadastrar = False
                                        analisar = False
                                        avaliar = False
                                        resposta = ''
                                        break
                                else:
                                    while visualizar_boletim:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EFI[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EFI[indice]['grade']}° Ano")
                                        print(f"{green}Escolaridade:{reset} {alunos_EFI[indice]['escolaridade']}")
                                        print()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(
                                            73) + cyan + '║')
                                        print('╠' + '═' * 73 + '╣')
                                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                        print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                        while resposta not in ['0', '1', '2', '3', '4']:
                                            limpar()

                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)
                                            print(f"{green}Aluno:{reset} {alunos_EFI[indice]['nome']}")
                                            print(f"{green}Grade:{reset} {alunos_EFI[indice]['grade']}° Ano")
                                            print(f"{green}Escolaridade:{reset} {alunos_EFI[indice]['escolaridade']}")
                                            print()

                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(
                                                73) + cyan + '║')
                                            print('╠' + '═' * 73 + '╣')
                                            print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                            print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)
                                            print(red + 'Digito Inválido! Tente novamente.' + reset)
                                            resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                        match resposta:
                                            case '0':
                                                visualizar_boletim = False
                                                skip = False
                                            case '1':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 1° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFI[indice]['boletim_EF'][0].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '2':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 2° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFI[indice]['boletim_EF'][1].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '3':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 3° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFI[indice]['boletim_EF'][2].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '4':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 4° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFI[indice]['boletim_EF'][3].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                            else:
                                resposta = ''
                                break
                        else:
                            limpar()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print(
                                '║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(
                                    73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito Inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                cadastrar = True
                                analisar = False
                                avaliar = False
                                skip = True
                                resposta = ''
                            else:
                                resposta = ''
                                cadastrar = False

                    elif resposta_escolaridade == '2':
                        if len(alunos_EFII) > 0:
                            limpar()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()

                            for cont, al in enumerate(alunos_EFII):
                                print(
                                    cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                        69) + cyan + '║' + reset)
                            print()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Você deseja analisar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                for cont, al in enumerate(alunos_EFII):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)
                                print()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Você deseja analisar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                visualizar_boletim = True
                                resposta = ''
                                limpar()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()

                                for cont, al in enumerate(alunos_EFII):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)

                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + f'Qual aluno você deseja analisar?'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                opcoes_validas = [str(i + 1) for i in range(len(alunos_EFII))]

                                while resposta_aluno not in opcoes_validas:
                                    limpar()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EFII): print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)
                                    print()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + f'Qual aluno você deseja analisar?'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(red + 'Digito Inválido! Tente novamente.' + reset)
                                    resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                indice = int(resposta_aluno) - 1

                                if len(alunos_EFII[indice]) <= 3:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(f"{green}Aluno:{reset} {alunos_EFII[indice]['nome']}")
                                    print(f"{green}Grade:{reset} {alunos_EFII[indice]['grade']}° Ano")
                                    print(f"{green}Escolaridade:{reset} {alunos_EFII[indice]['escolaridade']}")
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'O aluno não possui boletim registrado.'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                    while resposta not in ['S', 'N']:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EFII[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EFII[indice]['grade']}° Ano")
                                        print(f"{green}Escolaridade:{reset} {alunos_EFII[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'O aluno não possui boletim registrado.'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print(
                                            '║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Dígito Inválido! Tente novamente.' + reset)
                                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                    if resposta == 'S':
                                        cadastrar = False
                                        analisar = False
                                        avaliar = True
                                        skip = True
                                        resposta = ''
                                        break
                                    else:
                                        skip = False
                                        cadastrar = False
                                        analisar = False
                                        avaliar = False
                                        resposta = ''
                                        break
                                else:
                                    while visualizar_boletim:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EFII[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EFII[indice]['grade']}° Ano")
                                        print(f"{green}Escolaridade:{reset} {alunos_EFII[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(
                                            73) + cyan + '║')
                                        print('╠' + '═' * 73 + '╣')
                                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                        print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                        while resposta not in ['0', '1', '2', '3', '4']:
                                            limpar()

                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)
                                            print(f"{green}Aluno:{reset} {alunos_EFII[indice]['nome']}")
                                            print(f"{green}Grade:{reset} {alunos_EFII[indice]['grade']}° Ano")
                                            print(f"{green}Escolaridade:{reset} {alunos_EFII[indice]['escolaridade']}")
                                            print()
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(
                                                73) + cyan + '║')
                                            print('╠' + '═' * 73 + '╣')
                                            print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                            print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)
                                            print(red + 'Digito Inválido! Tente novamente.' + reset)
                                            resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                        match resposta:
                                            case '0':
                                                visualizar_boletim = False
                                                skip = False
                                            case '1':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 1° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFII[indice]['boletim_EF'][0].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '2':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 2° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFII[indice]['boletim_EF'][1].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '3':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 3° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFII[indice]['boletim_EF'][2].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '4':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 4° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EFII[indice]['boletim_EF'][3].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                            else:
                                resposta = ''
                                break
                        else:
                            limpar()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print(
                                '║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(
                                    73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito Inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                cadastrar = True
                                analisar = False
                                avaliar = False
                                skip = True
                                resposta = ''
                            else:
                                resposta = ''
                                cadastrar = False

                    elif resposta_escolaridade == '3':
                        if len(alunos_EM) > 0:
                            limpar()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()

                            for cont, al in enumerate(alunos_EM):
                                print(
                                    cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}ª Série - {al['escolaridade']}".ljust(
                                        69) + cyan + '║' + reset)
                            print()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Você deseja analisar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()

                                for cont, al in enumerate(alunos_EM):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}ª Série - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)
                                print()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Você deseja analisar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                visualizar_boletim = True
                                resposta = ''
                                limpar()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()

                                for cont, al in enumerate(alunos_EM):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}ª Série - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)

                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + f'Qual aluno você deseja analisar?'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                opcoes_validas = [str(i + 1) for i in range(len(alunos_EM))]

                                while resposta_aluno not in opcoes_validas:
                                    limpar()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EM):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()
                                    print(red + 'Digito Inválido! Tente novamente.' + reset)
                                    resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                indice = int(resposta_aluno) - 1

                                if len(alunos_EM[indice]) <= 3:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(f"{green}Aluno:{reset} {alunos_EM[indice]['nome']}")
                                    print(f"{green}Grade:{reset} {alunos_EM[indice]['grade']}ª Série")
                                    print(f"{green}Escolaridade:{reset} {alunos_EM[indice]['escolaridade']}")
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'O aluno não possui boletim registrado.'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                    while resposta not in ['S', 'N']:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EM[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EM[indice]['grade']}ª Série")
                                        print(f"{green}Escolaridade:{reset} {alunos_EM[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'O aluno não possui boletim registrado.'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print(
                                            '║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Dígito Inválido! Tente novamente.' + reset)
                                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                    if resposta == 'S':
                                        cadastrar = False
                                        analisar = False
                                        avaliar = True
                                        skip = True
                                        resposta = ''
                                        break
                                    else:
                                        skip = False
                                        cadastrar = False
                                        analisar = False
                                        avaliar = False
                                        resposta = ''
                                        break
                                else:
                                    while visualizar_boletim:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EM[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EM[indice]['grade']}ª Série")
                                        print(f"{green}Escolaridade:{reset} {alunos_EM[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(
                                            73) + cyan + '║')
                                        print('╠' + '═' * 73 + '╣')
                                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                        print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                        while resposta not in ['0', '1', '2', '3', '4']:
                                            limpar()

                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)
                                            print(f"{green}Aluno:{reset} {alunos_EM[indice]['nome']}")
                                            print(f"{green}Grade:{reset} {alunos_EM[indice]['grade']}ª Série")
                                            print(f"{green}Escolaridade:{reset} {alunos_EM[indice]['escolaridade']}")
                                            print()
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(
                                                73) + cyan + '║')
                                            print('╠' + '═' * 73 + '╣')
                                            print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                            print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                            print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)
                                            print(red + 'Digito Inválido! Tente novamente.' + reset)
                                            resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                        match resposta:
                                            case '0':
                                                visualizar_boletim = False
                                                skip = False
                                            case '1':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 1° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EM[indice]['boletim_EM'][0].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '2':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 2° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EM[indice]['boletim_EM'][1].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '3':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 3° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EM[indice]['boletim_EM'][2].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                                            case '4':
                                                limpar()
                                                print(cyan + '╔' + '═' * 73 + '╗')
                                                print('║' + yellow + 'Boletim 4° Bimestre'.center(73) + cyan + '║')
                                                print('╚' + '═' * 73 + '╝' + reset)
                                                for materia, nota in alunos_EM[indice]['boletim_EM'][3].items():
                                                    print(yellow + f'{materia}: ' + reset + f'{nota}')
                                                input('Pressione ENTER para voltar...')
                            else:
                                resposta = ''
                                break
                        else:
                            limpar()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Médio!'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Médio!'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito Inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                cadastrar = True
                                analisar = False
                                avaliar = False
                                skip = True
                                resposta = ''
                            else:
                                resposta = ''
                                cadastrar = False

                    else:  # resposta_escolaridade == '0'
                        skip = False
                        cadastrar = False
                        analisar = False
                        avaliar = False

                while avaliar:
                    if not skip:
                        limpar()

                        print(cyan + '╔' + '═' * 73 + '╗')
                        print('║' + yellow + 'O aluno que você deseja avaliar é de qual escolaridade?'.center(73) + cyan + '║')
                        print('╠' + '═' * 73 + '╣')
                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                        print('║' + reset + '1 - Ensino Fundamental I'.center(73) + cyan + '║')
                        print('║' + reset + '2 - Ensino Fundamental II'.center(73) + cyan + '║')
                        print('║' + reset + '3 - Ensino Médio'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝' + reset)

                        resposta_escolaridade = str(input('Digite sua resposta - (0/1/2/3): ')).strip()

                        while resposta_escolaridade not in ['0', '1', '2', '3']:
                            limpar()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + yellow + 'O aluno que você deseja avaliar é de qual escolaridade?'.center(
                                73) + cyan + '║')
                            print('╠' + '═' * 73 + '╣')
                            print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                            print('║' + reset + '1 - Ensino Fundamental I'.center(73) + cyan + '║')
                            print('║' + reset + '2 - Ensino Fundamental II'.center(73) + cyan + '║')
                            print('║' + reset + '3 - Ensino Médio'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print(red + 'Digito inválido! Tente novamente.' + reset)
                            resposta_escolaridade = str(input('Digite sua resposta - (0/1/2/3): ')).strip()

                    if resposta_escolaridade == '1':
                        resposta = ''
                        if len(alunos_EFI) > 0:
                            if skip:
                                resposta = 'S'
                            if not skip:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                for cont, al in enumerate(alunos_EFI):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Você deseja avaliar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                while resposta not in ['S', 'N']:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EFI):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Você deseja avaliar algum aluno? (S/N)'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(red + 'Digito inválido! Tente novamente.' + reset)
                                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                resposta = ''
                                registro_boletim = True
                                if not skip:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EFI):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + f'Qual aluno você deseja avaliar?'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                    opcoes_validas = [str(i + 1) for i in range(len(alunos_EFI))]

                                    while resposta_aluno not in opcoes_validas:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Alunos do Ensino Fundamental I:'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print()
                                        for cont, al in enumerate(alunos_EFI):
                                            print(
                                                cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                    69) + cyan + '║' + reset)
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + f'Qual aluno você deseja avaliar?'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Digito Inválido! Tente novamente.' + reset)
                                        resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                indice = int(resposta_aluno) - 1
                                resposta = ''

                                while registro_boletim:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(f"{green}Aluno:{reset} {alunos_EFI[indice]['nome']}")
                                    print(f"{green}Grade:{reset} {alunos_EFI[indice]['grade']}° Ano")
                                    print(f"{green}Escolaridade:{reset} {alunos_EFI[indice]['escolaridade']}")
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(
                                        73) + cyan + '║')
                                    print('╠' + '═' * 73 + '╣')
                                    print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                    print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                    while resposta not in ['0', '1', '2', '3', '4']:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EFI[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EFI[indice]['grade']}° Ano")
                                        print(f"{green}Escolaridade:{reset} {alunos_EFI[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(
                                            73) + cyan + '║')
                                        print('╠' + '═' * 73 + '╣')
                                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                        print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Digito Inválido! Tente novamente.' + reset)
                                        resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                    match resposta:
                                        case '0':
                                            registro_boletim = False
                                            skip = False
                                        case '1':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 1° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFI[indice]:
                                                alunos_EFI[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFI[indice]['boletim_EF'][0][f'{materia}'] = nota

                                            skip = True
                                        case '2':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 2° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFI[indice]:
                                                alunos_EFI[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFI[indice]['boletim_EF'][1][f'{materia}'] = nota

                                            skip = True
                                        case '3':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 3° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFI[indice]:
                                                alunos_EFI[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFI[indice]['boletim_EF'][2][f'{materia}'] = nota

                                            skip = True
                                        case '4':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 4° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFI[indice]:
                                                alunos_EFI[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFI[indice]['boletim_EF'][3][f'{materia}'] = nota

                                            skip = True
                            else:
                                resposta = ''
                                break

                        else:
                            limpar()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print(
                                '║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)

                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(
                                    73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito Inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                cadastrar = True
                                analisar = False
                                avaliar = False
                                skip = True
                                resposta = ''
                            else:
                                cadastrar = False
                                resposta = ''

                    elif resposta_escolaridade == '2':
                        resposta = ''
                        if len(alunos_EFII) > 0:
                            if skip:
                                resposta = 'S'
                            if not skip:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                for cont, al in enumerate(alunos_EFII):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Você deseja avaliar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                while resposta not in ['S', 'N']:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EFII):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Você deseja avaliar algum aluno? (S/N)'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(red + 'Digito inválido! Tente novamente.' + reset)
                                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                resposta = ''
                                registro_boletim = True
                                if not skip:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EFII):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + f'Qual aluno você deseja avaliar?'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                    opcoes_validas = [str(i + 1) for i in range(len(alunos_EFII))]

                                    while resposta_aluno not in opcoes_validas:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Alunos do Ensino Fundamental II:'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print()
                                        for cont, al in enumerate(alunos_EFII):
                                            print(
                                                cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                    69) + cyan + '║' + reset)
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + f'Qual aluno você deseja avaliar?'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Digito Inválido! Tente novamente.' + reset)
                                        resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                indice = int(resposta_aluno) - 1
                                resposta = ''

                                while registro_boletim:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(f"{green}Aluno:{reset} {alunos_EFII[indice]['nome']}")
                                    print(f"{green}Grade:{reset} {alunos_EFII[indice]['grade']}° Ano")
                                    print(f"{green}Escolaridade:{reset} {alunos_EFII[indice]['escolaridade']}")
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(
                                        73) + cyan + '║')
                                    print('╠' + '═' * 73 + '╣')
                                    print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                    print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                    while resposta not in ['0', '1', '2', '3', '4']:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EFII[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EFII[indice]['grade']}° Ano")
                                        print(f"{green}Escolaridade:{reset} {alunos_EFII[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(
                                            73) + cyan + '║')
                                        print('╠' + '═' * 73 + '╣')
                                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                        print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Digito Inválido! Tente novamente.' + reset)
                                        resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                    match resposta:
                                        case '0':
                                            registro_boletim = False
                                            skip = False
                                        case '1':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 1° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFII[indice]:
                                                alunos_EFII[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFII[indice]['boletim_EF'][0][f'{materia}'] = nota

                                            skip = True
                                        case '2':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 2° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFII[indice]:
                                                alunos_EFII[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFII[indice]['boletim_EF'][1][f'{materia}'] = nota

                                            skip = True
                                        case '3':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 3° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFII[indice]:
                                                alunos_EFII[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFII[indice]['boletim_EF'][2][f'{materia}'] = nota

                                            skip = True
                                        case '4':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 4° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EF' not in alunos_EFII[indice]:
                                                alunos_EFII[indice]['boletim_EF'] = copy.deepcopy(boletim_EF)

                                            for materia in materias_EF:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EFII[indice]['boletim_EF'][3][f'{materia}'] = nota

                                            skip = True
                            else:
                                resposta = ''
                                break

                        else:
                            limpar()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print(
                                '║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(
                                    73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito Inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                cadastrar = True
                                analisar = False
                                avaliar = False
                                skip = True
                                resposta = ''
                            else:
                                cadastrar = False
                                resposta = ''

                    elif resposta_escolaridade == '3':
                        resposta = ''
                        if len(alunos_EM) > 0:
                            if skip:
                                resposta = 'S'
                            if not skip:
                                limpar()

                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                for cont, al in enumerate(alunos_EM):
                                    print(
                                        cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                            69) + cyan + '║' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Você deseja avaliar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                                while resposta not in ['S', 'N']:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EM):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Você deseja avaliar algum aluno? (S/N)'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(red + 'Digito inválido! Tente novamente.' + reset)
                                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                resposta = ''
                                registro_boletim = True
                                if not skip:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print()
                                    for cont, al in enumerate(alunos_EM):
                                        print(
                                            cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                69) + cyan + '║' + reset)
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + f'Qual aluno você deseja avaliar?'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                    opcoes_validas = [str(i + 1) for i in range(len(alunos_EM))]

                                    while resposta_aluno not in opcoes_validas:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Alunos do Ensino Médio:'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print()
                                        for cont, al in enumerate(alunos_EM):
                                            print(
                                                cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(
                                                    69) + cyan + '║' + reset)
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + f'Qual aluno você deseja avaliar?'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Digito Inválido! Tente novamente.' + reset)
                                        resposta_aluno = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                                indice = int(resposta_aluno) - 1
                                resposta = ''

                                while registro_boletim:
                                    limpar()

                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    print(f"{green}Aluno:{reset} {alunos_EM[indice]['nome']}")
                                    print(f"{green}Grade:{reset} {alunos_EM[indice]['grade']}ª Série")
                                    print(f"{green}Escolaridade:{reset} {alunos_EM[indice]['escolaridade']}")
                                    print()
                                    print(cyan + '╔' + '═' * 73 + '╗')
                                    print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(
                                        73) + cyan + '║')
                                    print('╠' + '═' * 73 + '╣')
                                    print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                    print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                    print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                    print('╚' + '═' * 73 + '╝' + reset)
                                    resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                    while resposta not in ['0', '1', '2', '3', '4']:
                                        limpar()

                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + yellow + 'Detalhes do Aluno'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(f"{green}Aluno:{reset} {alunos_EM[indice]['nome']}")
                                        print(f"{green}Grade:{reset} {alunos_EM[indice]['grade']}ª Série")
                                        print(f"{green}Escolaridade:{reset} {alunos_EM[indice]['escolaridade']}")
                                        print()
                                        print(cyan + '╔' + '═' * 73 + '╗')
                                        print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(
                                            73) + cyan + '║')
                                        print('╠' + '═' * 73 + '╣')
                                        print('║' + reset + '0 - Voltar'.center(73) + cyan + '║')
                                        print('║' + reset + '1 - 1° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '2 - 2° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '3 - 3° Bimestre'.center(73) + cyan + '║')
                                        print('║' + reset + '4 - 4° Bimestre'.center(73) + cyan + '║')
                                        print('╚' + '═' * 73 + '╝' + reset)
                                        print(red + 'Digito Inválido! Tente novamente.' + reset)
                                        resposta = str(input('Digite sua resposta? (0/1/2/3/4): '))

                                    match resposta:
                                        case '0':
                                            registro_boletim = False
                                            skip = False
                                        case '1':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 1° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EM' not in alunos_EM[indice]:
                                                alunos_EM[indice]['boletim_EM'] = copy.deepcopy(boletim_EM)

                                            for materia in materias_EM:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EM[indice]['boletim_EM'][0][f'{materia}'] = nota

                                            skip = True
                                        case '2':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 2° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EM' not in alunos_EM[indice]:
                                                alunos_EM[indice]['boletim_EM'] = copy.deepcopy(boletim_EM)

                                            for materia in materias_EM:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EM[indice]['boletim_EM'][1][f'{materia}'] = nota

                                            skip = True
                                        case '3':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 3° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EM' not in alunos_EM[indice]:
                                                alunos_EM[indice]['boletim_EM'] = copy.deepcopy(boletim_EM)

                                            for materia in materias_EM:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EM[indice]['boletim_EM'][2][f'{materia}'] = nota

                                            skip = True
                                        case '4':
                                            resposta = ''
                                            print(cyan + '╔' + '═' * 73 + '╗')
                                            print('║' + yellow + 'Boletim 4° Bimestre (Registro)'.center(73) + cyan + '║')
                                            print('╚' + '═' * 73 + '╝' + reset)

                                            if 'boletim_EM' not in alunos_EM[indice]:
                                                alunos_EM[indice]['boletim_EM'] = copy.deepcopy(boletim_EM)

                                            for materia in materias_EM:
                                                nota = int(input(f'Nota de {materia}: '))
                                                alunos_EM[indice]['boletim_EM'][3][f'{materia}'] = nota

                                            skip = True
                            else:
                                resposta = ''
                                break

                        else:
                            limpar()

                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Médio!'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            print()
                            print(cyan + '╔' + '═' * 73 + '╗')
                            print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝' + reset)
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            while resposta not in ['S', 'N']:
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Médio!'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print()
                                print(cyan + '╔' + '═' * 73 + '╗')
                                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝' + reset)
                                print(red + 'Digito Inválido! Tente novamente.' + reset)
                                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                            if resposta == 'S':
                                cadastrar = True
                                analisar = False
                                avaliar = False
                                skip = True
                                resposta = ''
                            else:
                                cadastrar = False
                                resposta = ''

                    else:  # resposta_escolaridade == '0'
                        skip = False
                        cadastrar = False
                        analisar = False
                        avaliar = False
        case "2":
            jogadores = dict()
            lista_jogadores = list()

            limpar()
            for c in range(0,4):

                limpar()

                print(cyan + '╔' + '═' * 73 + '╗')
                print(f'║' + yellow + f'Jogador {c+1}'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                jogadores['nick'] = str(input('Por favor digite o seu nickname antes de iniciar: ')).capitalize().strip()
                jogadores['dado'] = rd.randint(1, 6)
                lista_jogadores.append(jogadores.copy())
                
                limpar()

                print(cyan + '╔' + '═' * 73 + '╗')
                print('║' + yellow + f'Jogador {c+1}'.center(73) + cyan + '║')
                print('╠' + '═' * 73 + '╣')
                print('║' + reset + f'Seja bem vindo(a) {lista_jogadores[c]['nick']}!'.center(73) + cyan + '║')
                print('║' + reset + 'Aqui você irá disputar com outros jogadores em uma competição de dados.'.center(73) + cyan + '║')
                print('║' + reset + 'O jogador que tirar o maior valor vence o jogo!'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                input('Se estiver pronto para começar pressione ENTER...\n')

                limpar()

                for letra in '🎲 Vamos rolar os dados! 🎲':
                    print(letra, end='', flush=True)
                    sleep(0.05)
                sleep(0.25)

                limpar()

                for pontinhos in range(0,6):
                    for ponto in range(0,3):
                        print('.', end='', flush=True)
                        sleep(0.1)
                    limpar()

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

            limpar()

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

            limpar()

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

        case "3":
            loop= "S"

            pessoa = {
                "nome": "",
                "genero": "",
                "nasc": "",
                "ctps": "",
                "idade": "",
                "contrato": "",
                "inicio": "",
                "salario": "",
                "aposenta": "",
                "idadeAposenta": "",
                "contribuicao": ""
                }

            while loop == "S":

                limpar()

                sleep(2)

                hj=dt.date.today()
                ctpsmodelo= "1"

                print((cyan) + '╔' + '═' * 73 + '╗')
                print('║' + (reset) + f'Digite seu nome: '.center(73) + (cyan) + '║')
                print('╚' + '═' * 73 + '╝\n' + reset)
                pessoa["nome"]= input()
                
                
                while True:
                    limpar()
                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + 'Digite sua data de nascimento [DD/MM/AAAA]: '.center(73) + (cyan) + '║')
                    print('║' + ' ' * 73 + cyan + '║')
                    print('║' + blue + 'Use o formato DD/MM/AAAA'.center(73) + cyan + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)
                    pessoa["nasc"] = input()

                    if len(pessoa["nasc"]) != 10 or pessoa["nasc"][2] != '/' or pessoa["nasc"][5] != '/':
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Use o formato DD/MM/AAAA'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)
                        continue

                    dia, mes, ano = pessoa["nasc"].split('/')

                    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Use apenas números na data'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)
                        continue

                    dia = int(dia)
                    mes = int(mes)
                    ano = int(ano)

                    if ano < 1900 or ano > hj.year:
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Ano inválido'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)
                        continue

                    if mes < 1 or mes > 12:
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Mês inválido'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)
                        continue

                    diasPorMes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28,
                                    31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    if dia < 1 or dia >diasPorMes[mes - 1]:
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Dia inválido para o mês informado'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)
                        continue

                    datanasc = dt.date(ano, mes, dia)

                    if datanasc > hj:
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'A data de nascimento não pode ser no futuro'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)
                        continue

                    if hj.year - ano > 120:
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Idade acima de 120 anos parece incorreta'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)
                        continue
                    break

                
                sleep(1)

                print((cyan) + '╔' + '═' * 73 + '╗')
                print('║' + blue + 'Digite seu gênero cadastrado no cartório [M/F]:'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝\n' + reset)
                pessoa["genero"]= (input().upper().strip())

                limpar()
                
                while pessoa["genero"] not in ("M", "F"):
                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + red + 'Gênero inválido'.center(73) + cyan + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)
                    sleep(1)
                    
                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + blue + 'Digite seu gênero cadastrado no cartório [M/F]:'.center(73) + cyan + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)
                    pessoa["genero"]= (input().upper().strip())

                    limpar()

                pessoa["idade"] = hj.year - datanasc.year - ((hj.month, hj.day) < (datanasc.month, datanasc.day))

                while ctpsmodelo not in ("0", ""):
                    sleep(1)
                    ctpsmodelo= (input(f"{pink}O modelo da sua CTPS é antigo ou novo? {green}[Digite '?' para mais informações]{reset}[{yellow}A{reset} -> {yellow}Antigo{reset}/ {orange}N{reset} -> {orange}Novo{reset}]: {reset}").upper().strip())

                    if ctpsmodelo not in ("0", "", "A", "N", "?", "1"):
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Carteira de trabalho inválida '.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        continue
                    
                    if ctpsmodelo == 'N':
                        sleep(1)
                        limpar()
                        while True:
                            sleep(1)
                            print((cyan) + '╔' + '═' * 73 + '╗')
                            print('║' + blue + 'Digite seu CPF [Sem pontos, traços ou espaços - 11 dígitos]: '.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                            pessoa["ctps"] = input()
                            if len(pessoa["ctps"]) == 11 and pessoa["ctps"].isdigit():
                                break  
                            else:
                                print((cyan) + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'O CPF deve ter exatamente 11 dígitos numéricos. Tente novamente'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝\n' + reset)
                        break  
                    
                    elif ctpsmodelo == 'A':
                        limpar()
                        while True:
                            sleep(1)
                            print((cyan) + '╔' + '═' * 73 + '╗')
                            print('║' + purple + 'Digite o número da sua carteira de trabalho [7 dígitos]: '.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                            ct = input()
                            if len(ct) == 7 and ct.isdigit():
                                break
                            else:
                                print((cyan) + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'O número da CTPS deve ter exatamente 7 dígitos numéricos. Tente novamente'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝\n' + reset)
                        while True:
                            sleep(1)
                            print((cyan) + '╔' + '═' * 73 + '╗')
                            print('║' + purple + 'Digite a série da sua carteira de trabalho [4 dígitos]: '.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                            ps = input()
                            if len(ps) == 4 and ps.isdigit():
                                break 
                            else:
                                print((cyan) + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'A série da CTPS deve ter exatamente 4 dígitos numéricos. Tente novamente'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝\n' + reset)
                        pessoa["ctps"]= ct+ps
                        break
                    
                    elif ctpsmodelo == '?':
                        limpar()
                        sleep(1)
                        print(f"{orange}Número da CTPS Digital (novo) -> Use o CPF para registro e consulta.\n\n{yellow}Número da CTPS Antiga (antigo) -> Use o Número e Série que constam na página de identificação do documento físico.{reset}")
                    
                    elif ctpsmodelo == "":
                        ctpsmodelo = "0"

                if ctpsmodelo not in ("0", ""):

                    while True:
                        sleep(1)
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + purple + 'Digite o ano de contratação do seu contrato atual [AAAA]: '.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        pessoa["contrato"] = (input())
                        if len(pessoa["contrato"]) == 4 and pessoa["contrato"].isdigit():
                            pessoa["contrato"] = int(pessoa["contrato"])
                            if hj.year - 100 <= pessoa["contrato"] <= hj.year and pessoa["contrato"] >= ano:
                                break
                            else:
                                print((cyan) + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Ano de contratação inválido'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝\n' + reset)
                                continue
                        else:
                            print((cyan) + '╔' + '═' * 73 + '╗')
                            print('║' + red + 'Formato inválido. Tente novamente'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                            continue

                    while True:
                        sleep(1)
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + purple + 'Digite o ano de inicio de sua contribuição para a previdência [AAAA]: '.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        pessoa["inicio"] = (input())
                        if len(pessoa["inicio"]) == 4 and pessoa["inicio"].isdigit():
                            pessoa["inicio"] = int(pessoa["inicio"])
                            if hj.year - 100 <= pessoa["inicio"] <= hj.year and pessoa["inicio"] >= ano:
                                break
                            else:
                                print((cyan) + '╔' + '═' * 73 + '╗')
                                print('║' + red + 'Ano de contribuição inválido'.center(73) + cyan + '║')
                                print('╚' + '═' * 73 + '╝\n' + reset)
                                continue
                        else:
                            print((cyan) + '╔' + '═' * 73 + '╗')
                            print('║' + red + 'Formato inválido. Tente novamente'.center(73) + cyan + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                            continue

                    sleep(1)

                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + purple + 'Digite seu último sálario: '.center(73) + cyan + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)
                    pessoa["salario"] = (input())

                    while not pessoa["salario"].isdigit():
                        print((cyan) + '╔' + '═' * 73 + '╗')
                        print('║' + red + 'Use apenas números'.center(73) + cyan + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(1)
                        pessoa["salario"] = (input(f"{purple}Digite seu último sálario: {reset}"))

                    pessoa["salario"] = float(pessoa["salario"])
                    
                    pessoa["contribuicao"]= hj.year - pessoa["inicio"]
                    
                    if pessoa["genero"] == "M":
                        idademin= 65
                        contribmin= 20
                        
                    elif pessoa["genero"] == "F":
                        idademin= 62
                        contribmin= 15

                    if pessoa["idade"] >= idademin and pessoa["contribuicao"] >= contribmin:
                        pessoa["aposenta"]= hj.year

                    else:
                        faltaIdade= max(0, idademin - pessoa["idade"])
                        faltaContrib= max(0, contribmin - pessoa["contribuicao"])
                        falta= max(faltaIdade, faltaContrib)
                        pessoa["aposenta"]= hj.year + falta
                        pessoa["idadeAposenta"] = pessoa["aposenta"] - ano
                        if ctpsmodelo == "N":
                            cpf = pessoa["ctps"]
                            pessoa["ctps"] = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                        elif ctpsmodelo == "A":
                            ctps = pessoa["ctps"]
                            pessoa["ctps"] = f"{ctps[:7]}/{ctps[7:]}"
                        if pessoa["genero"] == "F":
                            pessoa["genero"] = "Feminino"
                        elif pessoa["genero"] == "M":
                            pessoa["genero"] = "Masculino"

                        sleep(1)
            
                        limpar()
                        
                        sleep(1)

                        print((orange) + '╔' + '═' * 73 + '╗')
                        print('║' + (cyan) + f'Dados do usuário'.center(73) + (orange) + '║')
                        print('╚' + '═' * 73 + '╝' + reset)
                        sleep(1)
                        print(f"{blue}Nome: {pessoa["nome"]}".upper())
                        sleep(1)
                        print(f"Gênero cadastrado no cartório: {pessoa["genero"]}".upper())
                        sleep(1)
                        print(f"Data de nascimento: {pessoa["nasc"]}".upper())
                        sleep(1)
                        print(f"Idade: {pessoa["idade"]} ano(s)".upper())
                        sleep(1)

                        print(f"Carteira de trabalho: {pessoa["ctps"]}".upper())
                        sleep(1)
                        print(f"Ano de inicio do contrato atual: {pessoa["contrato"]}".upper())
                        sleep(1)
                        print(f"Ano de inicio de contribuição para a previdência: {pessoa["inicio"]}".upper())
                        sleep(1)
                        print(f"Último salário: R${pessoa["salario"]:.2f}".upper())
                        sleep(1)
                        print(f"Ano de aposentadoria: {pessoa["aposenta"]}".upper())
                        sleep(1)
                        print(f"Idade de aposentadoria: {pessoa["idadeAposenta"]} anos".upper())
                        sleep(1)
                        print(f"Foram contribuídos: {pessoa["contribuicao"]} ano(s){reset}".upper())
                        input("Pressione ENTER para continuar")
                        limpar()

                if ctpsmodelo in ("0", ""):

                    if pessoa["genero"] == "F":
                        pessoa["genero"] = "Feminino"
                    elif pessoa["genero"] == "M":
                        pessoa["genero"] = "Masculino"

                    print((orange) + '╔' + '═' * 73 + '╗')
                    print('║' + (cyan) + f'Dados do usuário'.center(73) + (orange) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    sleep(1)
                    print(f"{blue}Nome: {pessoa["nome"]}".upper())
                    sleep(1)
                    print(f"Gênero cadastrado no cartório: {pessoa["genero"]}".upper())
                    sleep(1)
                    print(f"Data de nascimento: {pessoa["nasc"]}".upper())
                    sleep(1)
                    print(f"Idade: {pessoa["idade"]} ano(s){reset}".upper())
                    input("Pressione ENTER para continuar")
                    limpar()

                loop= (input(f"{orange}Deseja cadastrar outra pessoa? [S/N] {reset}").upper())

                while loop not in ("S", "N"):
                    print(f"{red}Digite uma opção válida{reset}")
                    sleep(1)
                    loop= (input(f"{orange}Deseja cadastrar outra pessoa? [S/N] {reset}").upper())

                if loop == "N":
                    sleep(1)
                    break
    

        case "4":
            
            jogadores = []  # lista para guardar todos os jogadores

            limpar()

            print((cyan) + '╔' + '═' * 73 + '╗')
            print('║' + (reset) + f'Oi, seja bem-vindo ao gerenciamento de aproveitamento de jogadores!'.center(73) + (cyan) + '║')
            print('╚' + '═' * 73 + '╝' + reset)
            sleep(2)

            print((yellow) + "=" * 75)

            while True:
                limpar()
                print((cyan) + '╔' + '═' * 73 + '╗')
                print('║' + (reset) + f'Deseja cadastrar algum jogador?'.center(73) + (cyan) + '║')
                print('╚' + '═' * 73 + '╝\n' + reset)

                cadas = input("(S/N): ").upper()
                if cadas in ["S", "N"]:
                    break
                else:
                    print((red) + '╔' + '═' * 73 + '╗')
                    print('║' + (yellow) + f"❌ Digite apenas 'S' para sim ou 'N' para não!".center(72) + (red) + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)
                    sleep(2)

            sleep(1)

            while cadas == "S":
                limpar()
                jogador = {}   # cria um novo dicionário a cada cadastro
            
                # Validação do código
                while True:
                    limpar()
                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + f'Digite um código novo de 1 a 999 para o novo jogador'.center(73) + (cyan) + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)

                    codigo = input()
                    
                    if codigo == "0":
                        print((red) + '╔' + '═' * 73 + '╗')
                        print('║' + (yellow) + f'❌ Não é permitido o número 0.'.center(72) + (red) + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)

                    elif codigo.isdigit():
                        codigo = int(codigo)
                        
                        if 1 <= codigo <= 999:
                            # Verificar se código já existe
                            codigo_repetido = False
                            for j in jogadores:
                                if j["codigo"] == codigo:
                                    codigo_repetido = True
                                    break
                            
                            if codigo_repetido:
                                print((red) + '╔' + '═' * 73 + '╗')
                                print('║' + (yellow) + f'❌ Código {codigo:03} já está em uso!'.center(72) + (red) + '║')
                                print('╚' + '═' * 73 + '╝\n' + reset)
                                sleep(2)
                            else:
                                jogador["codigo"] = codigo
                                break


                        else:
                            print((red) + '╔' + '═' * 73 + '╗')
                            print('║' + (yellow) + f'❌ O código deve estar entre 0 e 999!'.center(72) + (red) + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                            sleep(2)
                            
                    else:
                        print((red) + '╔' + '═' * 73 + '╗')
                        print('║' + (yellow) + f'❌ Digite apenas números inteiros!'.center(72) + (red) + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(2)

                limpar()
                
                while True:
                    limpar()
                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + f'Digite o nome do Jogador'.center(73) + (cyan) + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)
                    
                    nome_input = input().strip().capitalize()

                    # Verifica se está vazio
                    if nome_input == "":
                        print((red) + '╔' + '═' * 73 + '╗')
                        print('║' + (yellow) + f'❌ O nome não pode estar vazio!'.center(73) + (red) + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(1.5)
                        continue

                    # Verifica se contém apenas letras e espaços
                    if nome_input.replace(" ", "").isalpha():
                        jogador["nome"] = nome_input
                        break
                    else:
                        print((red) + '╔' + '═' * 73 + '╗')
                        print('║' + (yellow) + f'❌ O nome não pode conter números ou caracteres especiais!'.center(72) + (red) + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        sleep(1.5)

                # Validação das partidas jogadas
                while True:
                    limpar()
                    partidas = input(f"{yellow}Digite quantas partidas {jogador['nome']} jogou: {reset}")
                    if partidas.isdigit():
                        partidas = int(partidas)
                        if partidas > 1391:
                            print((red) + '╔' + '═' * 73 + '╗')
                            print('║' + (yellow) + f'❌ é bem improvável que {jogador['nome']} tenha jogado essa quantidade de partidas, o recorde é 1,391.'.center(73) + (red) + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                        else:
                            partidas = int(partidas)
                            break
                    else:
                        print((red) + '╔' + '═' * 73 + '╗')
                        print('║' + (yellow) + f'❌  Digite um número válido de partidas.'.center(73) + (red) + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)

                

                gols = []
                for i in range(partidas):
                    while True:
                        limpar()
                        g = input(f"{green}Gols na partida {i+1}: {reset}")
                        if g.isdigit():
                            g = int(g)
                            if g > 16:
                                print((red) + '╔' + '═' * 73 + '╗')
                                print('║' + (yellow) + f'❌ Quantidade exacerbada de gols, o limite é 16.'.center(72) + (red) + '║')
                                print('╚' + '═' * 73 + '╝\n' + reset)
                                sleep(2)
                            else:
                                gols.append(int(g))
                                break
                        else:
                            print((red) + '╔' + '═' * 73 + '╗')
                            print('║' + (yellow) + f'❌ Digite um número inteiro válido.'.center(73) + (red) + '║')
                            print('╚' + '═' * 73 + '╝\n' + reset)
                            
                
                jogador["partidas_jogadas"] = partidas
                jogador["gols_partida"] = gols
                jogador["total_gols"] = sum(gols)
                
                jogadores.append(jogador)
                
                print((green) + '╔' + '═' * 73 + '╗')
                print('║' + (green) + f'✅ Jogador cadastrado com sucesso!'.center(72) + (green) + '║')
                print('╚' + '═' * 73 + '╝\n' + reset)
                sleep(1)

                
                
                # Validação de resposta S/N novamente
                while True:
                    limpar()
                    print((orange) + '╔' + '═' * 73 + '╗')
                    print('║' + (blue) + f'✅ Deseja cadastrar outro jogador? {reset}(S/N) '.center(76) + (orange) + '║')
                    print('╚' + '═' * 73 + '╝\n' + reset)
                    cadas = input().upper().strip()
                    if cadas in ["S", "N"]:
                        break
                    else:
                        print((red) + '╔' + '═' * 73 + '╗')
                        print('║' + (yellow) + f'❌ Digite apenas "S" ou "N"!'.center(73) + (red) + '║')
                        print('╚' + '═' * 73 + '╝\n' + reset)
                        

            # mostra os códigos disponíveis

            respo_jogas = True

            if len(jogadores) > 0:
                while respo_jogas == True:
                    limpar()
                    print(f"{blue}📋 Jogadores cadastrados:{reset}\n")
                    for j in jogadores:
                        print(f"{cyan}Código {j['codigo']:03} - {j['nome']}{reset}")
                    
                    print()
                    escolha = input(f"{yellow}Digite o código do jogador que deseja visualizar:{reset} ")

                    if escolha.isdigit():
                        escolha = int(escolha)
                        encontrado = False
                        for j in jogadores:
                            if j["codigo"] == escolha:
                                encontrado = True
                                print(f"\n{green}🔍 Detalhes do jogador:{reset}")
                                print(f"{blue}Código: {reset}{j['codigo']:03}")
                                print(f"{blue}Nome: {reset}{j['nome']}")
                                print(f"{blue}Partidas jogadas: {reset}{j['partidas_jogadas']}")
                                print(f"{blue}Gols por partida: {reset}{j['gols_partida']}")
                                print(f"{blue}Total de gols: {reset}{j['total_gols']}")
                                
                                pergunta = str()
                                while pergunta != 'N' and pergunta != "S":
                                    print((orange) + '╔' + '═' * 73 + '╗')
                                    print('║' + (blue) + f'Deseja analisar mais algum jogador?: {reset}(S/N) '.center(77) + (orange) + '║')
                                    print('╚' + '═' * 73 + '╝\n' + reset)
                                    pergunta = str(input()).strip().upper()

                                    if pergunta == "N":
                                        respo_jogas = False
                                    elif pergunta == "S":
                                        respo_jogas == True
                                        sleep(0.5)
                                    else:
                                        print(f"{red}Resposta Inválida, tente novamente" + reset)
                                        sleep(2)
                                        limpar()
                                        
                        if not encontrado:
                            print(f"{red}❌ Nenhum jogador encontrado com esse código.{reset}")
                            sleep(1.5)
                    else:
                        print(f"{red}❌ Código inválido! Digite apenas números.{reset}")
                        sleep(1.5)

            else:
                print(f"{red}⚠ Nenhum jogador foi cadastrado!{reset}")

        case "5":
            limpar()

            pessoadic = dict()
            pessoaslist = list()
            loop5 = True

            print(cyan + bold + '╔' + '═' * 73 + '╗')
            print('║' + (yellow) + f'O programa irá ler: nome, sexo e idade de várias pessoas.'.center(73) + (cyan) + '║')
            print('║' + ' ' * 73 + cyan + '║')
            print('║' + (orange) + f'No final ele mostrará:'.center(73) + (cyan) + '║')
            print('║' + (blue) + f'Quantas pessoas foram cadastradas.'.center(73) + (cyan) + '║')
            print('║' + (blue) + f'A média de idade.'.center(73) + (cyan) + '║')
            print('║' + (blue) + f'Uma lista com as mulheres.'.center(73) + (cyan) + '║')
            print('║' + (blue) + f'Uma lista de pessoas com idade acima da média.'.center(73) + (cyan) + '║')
            print('║' + ' ' * 73 + cyan + '║')
            print('║' + (purple) + f'Pressione ENTER para continuar...'.center(73) + (cyan) + '║')
            print('╚' + '═' * 73 + '╝' + reset)
            input("")

            while loop5 == True:
                limpar()
                
                user_respo = str()

                loop_nome = False
                while loop_nome == False:
                    

                    limpar()

                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    entradanome = str(input("Digite o nome do individuo: ")).strip().capitalize()

                    if entradanome.replace(" ", "").isalpha():
                        pessoadic['nome'] = entradanome
                        loop_nome = True
                        limpar()
                    else:
                        print((red) + '╔' + '═' * 73 + '╗')
                        print('║' + (yellow) + f'Números e Caracteres desse tipo não são permitidos....'.center(73) + (red) + '║')
                        print('╚' + '═' * 73 + '╝' + reset)
                        input("Pressione ENTER para continuar...")
                        limpar()

                print((cyan) + '╔' + '═' * 73 + '╗')
                print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                pessoadic['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()
                
                while pessoadic['sexo'] != "M" and pessoadic['sexo'] != "F":
                    print((red) + '╔' + '═' * 73 + '╗')
                    print('║' + (yellow) + f'Resposta inválida, tente novamente'.center(73) + (red) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    input("Pressione ENTER para continuar...")
                    limpar()
                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    pessoadic['sexo'] = str(input("Digite o sexo do Individuo: (M/F) ")).upper().strip()

                if pessoadic['sexo'] == "M":
                    limpar()
                    print((blue) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + f'{pessoadic['nome']} é do sexo masculino!..'.center(73) + (blue) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    input("Pressione ENTER para continuar...")

                elif pessoadic['sexo'] == "F":
                    limpar()
                    print((pink) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + f'{pessoadic['nome']} é do sexo feminino!..'.center(73) + (pink) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    input("Pressione ENTER para continuar...")
                    
                loop_idade = False
                while loop_idade == False:
                    limpar()
                    print((cyan) + '╔' + '═' * 73 + '╗')
                    print('║' + (reset) + f'Insira o dados do usuário a ser cadastrado'.center(73) + (cyan) + '║')
                    print('╚' + '═' * 73 + '╝' + reset)
                    
                    entradaIdade = input("Digite a idade do Individuo: ").strip()
                    limpar()

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

                    limpar()
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

            limpar()


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
            

        case "0":
            looppai = False
            continue
    print("")
    print()

    escolha = str()

    while escolha != "1" and escolha != "2" and escolha != "3":
        print(cyan + bold + '╔' + '═' * 73 + '╗')
        print('║' + white + f'Votação encerrada'.center(73) + cyan + '║')
        print('╠' + '═' * 73 + '╣')
        print('║' + white + '1 - Voltar para o menu'.center(73) + cyan + '║')
        print('║' + yellow + '2 - Outro Login'.center(73) + cyan + '║')
        print('║' + red + '3 - Encerrar o programa'.center(73) + cyan + '║')
        print('╚' + '═' * 73 + '╝' + reset)

        escolha = str(input("Selecione uma das opções: ")).strip()
        if escolha == "1":
            looplogin = False  # permanece logado, roda programa de novo
        elif escolha == "2":
            looplogin = True   # volta para loop de login
            limpar()
        elif escolha == "3":
            looppai = False  # encerra tudo
        else:
            print(red + "Opção inválida. Tente novamente." + reset)
            sleep(1.5)
            limpar()

limpar()
print(cyan + bold + '╔' + '═' * 73 + '╗')
print('║' + white + 'Tarefa encerrada'.center(73) + cyan + '║')
print('╠' + '═' * 73 + '╣')
print('║' + green + 'Obrigado pela preferência!'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')

print('║' + yellow + 'Sistema de Login:'.center(73) + cyan + '║')
print('║' + blue + 'Luis Pozenato'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')

print('║' + yellow + 'Programa 1'.center(73) + cyan + '║')
print('║' + blue + 'Glauber Almeida de Brito'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')


print('║' + yellow + 'Programa 2'.center(73) + cyan + '║')
print('║' + blue + 'Glauber Almeida de Brito'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')

print('║' + yellow + 'Programa 3'.center(73) + cyan + '║')
print('║' + blue + 'Anna Caroline Nascimento Silva'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')


print('║' + yellow + 'Programa 4'.center(73) + cyan + '║')
print('║' + blue + 'Maycon Kaio Silva'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')


print('║' + yellow + 'Programa 5'.center(73) + cyan + '║')
print('║' + blue + 'Luis Pozenato'.center(73) + cyan + '║')
print('║' + ' ' * 73 + cyan + '║')
print('╚' + '═' * 73 + '╝' + reset)
    



