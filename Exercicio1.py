'''
    Autores: 
    - Glauber Almeida de
    Turma: 2ºA DS               Data: 22/10/2025

    Exercício 1: Maycon
    - Faça um programa que Cadastre os nomes dos alunos, suas notas e suas médias. No final mostre:
    - O nome do aluno, sua média e sua situação, caso o usuário queria ver mais informações exiba as notas dos bimestres.
'''
from os import system as sys
from os import name as os_name
import copy
from time import sleep

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
orange = "\033[38;5;208m"
pink = "\033[38;5;198m"
brown = "\033[38;5;130m"
white = "\033[0;37m"
gray = white + black
reset = "\033[0m"

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


def limpar():
    sys('cls' if os_name == 'nt' else 'clear')


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
                    print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)

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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print('║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
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
                            print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                                print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                print()
                print(cyan + '╔' + '═' * 73 + '╗')
                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                while resposta not in ['S', 'N']:
                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(73) + cyan + '║')
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
                    print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)

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
                        for cont, al in enumerate(alunos_EFII):print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print('║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
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
                            print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                                print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                print()
                print(cyan + '╔' + '═' * 73 + '╗')
                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                while resposta not in ['S', 'N']:
                    limpar()

                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(73) + cyan + '║')
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
                    print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}ª Série - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}ª Série - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}ª Série - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)

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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print('║' + reset + 'Deseja registrar o boletim do aluno? (S/N)'.center(73) + cyan + '║')
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
                            print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                                print('║' + reset + 'Você deseja visualizar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                print('║' + yellow + 'O aluno que você deseja avaliar é de qual escolaridade?'.center(73) + cyan + '║')
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                                print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                            print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                print()
                print(cyan + '╔' + '═' * 73 + '╗')
                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)

                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                while resposta not in ['S', 'N']:
                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental I!'.center(73) + cyan + '║')
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                                print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                            print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
                print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                print()
                print(cyan + '╔' + '═' * 73 + '╗')
                print('║' + reset + 'Deseja cadastrar algum aluno? (S/N)'.center(73) + cyan + '║')
                print('╚' + '═' * 73 + '╝' + reset)
                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                while resposta not in ['S', 'N']:
                    limpar()

                    print(cyan + '╔' + '═' * 73 + '╗')
                    print('║' + red + 'Não tem nenhum aluno cadastrado no Ensino Fundamental II!'.center(73) + cyan + '║')
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
                        print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                            print(cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                                print( cyan + '║ ' + reset + f"{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}".ljust(69) + cyan + '║' + reset)
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
                        print('║' + reset + 'Você deseja registrar o boletim de qual bimestre?'.center(73) + cyan + '║')
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
