'''
    Autores: 
    - Glauber Almeida de
    Turma: 2ºA DS               Data: 22/10/2025

    Exercício 1: Maycon
    - Faça um programa que Cadastre os nomes dos alunos, suas notas e suas médias. No final mostre:
    - O nome do aluno, sua média e sua situação, caso o usuário queria ver mais informações exiba as notas dos bimestres.
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

alunos_EFI = list() # Ensino Fundamental I
alunos_EFII = list() # Ensino Fundamental II
alunos_EM = list() # Ensino Médio
aluno = dict()

bimestre_1_EF = dict()
bimestre_2_EF = dict()
bimestre_3_EF = dict()
bimestre_4_EF = dict()
boletim_EF = [bimestre_1_EF, bimestre_2_EF, bimestre_3_EF, bimestre_4_EF]
materias_EF = ['Lingua Portuguesa', 'Matemática', 'Ciências', 'História', 'Geografia', 'Inglês', 'Artes', 'Educação Física']

bimestre_1_EM = dict()
bimestre_2_EM = dict()
bimestre_3_EM = dict()
bimestre_4_EM = dict()
boletim_EM = [bimestre_1_EM, bimestre_2_EM, bimestre_3_EM, bimestre_4_EM]
materias_EM = ['Lingua Portuguesa', 'Matemática', 'História', 'Geografia', 'Física', 'Química', 'Biologia', 'Sociologia', 'Filosofia', 'Inglês', 'Artes', 'Educação Física']

def limpar():
    sys('cls')

resposta = str()
indice = int()
nota = int()

skip = False # Serve para pular o inicio do programa para evitar casos de redundância

# 4 variáveis booleanas principais, servem para sustentar os loops principais do programa
loop_ex1 = True
cadastrar = False 
analisar = False
avaliar = False

while loop_ex1 == True:
    if skip == False:
        limpar()
        print('O que deseja fazer?')
        print('1 - Cadastrar alunos')
        print('2 - Analisar alunos')
        print('3 - Avaliar alunos')
        resposta = str(input('Digite sua resposta - (1/2/3): ')).strip()

        while resposta not in ['1', '2', '3']:
            limpar()
            print('O que deseja fazer?')
            print('1 - Cadastrar alunos')
            print('2 - Analisar alunos')
            print('3 - Avaliar alunos')
            print('Digito inválido! Tente novamente.')
            cadastrar = str(input('Digite sua resposta - (1/2/3): ')).strip()

        match resposta:
            case '1':
                cadastrar = True
                analisar = False
                avaliar = False
            case '2':
                cadastrar = False
                analisar = True
                avaliar = False
            case '3':
                cadastrar = False
                analisar = False
                avaliar = True

    while cadastrar == True:
        limpar()
        
        aluno['nome'] = str(input('Digite o nome do(da) aluno(a): '))
        print('╔' + '═' * 73 + '╗')
        print('║' + 'Grades:'.center(73) + '║')
        print('╠' + '═' * 73 + '╣')
        for grades in range(1, 10):
            print('║' + f'{grades} - {grades}º ano do Ensino Fundamental'.center(73) + '║')
        print('╠' + '═' * 73 + '╣')
        for grades in range(1, 4):
            print('║' + f'{9 + grades} - {grades}ª série do Ensino Médio'.center(73) + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        
        aluno['grade'] = int(input('Digite a grade do(da) aluno(a): ')) ################################################ TEM QUE ARRUMAR, NAO PODE POR LETRA

        while aluno['grade'] not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            print('Digito errado')
        
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
        
        print('Você deseja cadastrar outro aluno?')
        resposta = str(input('Digite sua resposta - (S/N) ')).strip().upper()

        while resposta not in ['S', 'N']:
            limpar()

            print('Você deseja cadastrar outro aluno?')
            print('Digito inválido! Tente novamente.')
            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

        if resposta == 'S':
            cadastrar = True
            analisar = False
            avaliar = False
        else:
            cadastrar = False
            analisar = False
            avaliar = False
            skip = False
    
    while analisar == True:
        limpar()

        print('O aluno que você deseja analisar é de qual escolaridade?')
        print('1 - Ensino Fundamental I')
        print('2 - Ensino Fundamental II')
        print('3 - Ensino Médio')

        resposta = str(input('Digite sua resposta - (1/2/3): ')).strip()

        while resposta not in ['1', '2', '3']:
            limpar()

            print('O aluno que você deseja analisar é de qual escolaridade?')
            print('Digito inválido! Tente novamente.')
            resposta = str(input('Digite sua resposta - (1/2/3): ')).strip()

        if resposta == '1':
            if len(alunos_EFI) > 0:
                limpar()

                print('Alunos do Ensino Fundamental I:\n')

                for cont, al in enumerate(alunos_EFI):
                    print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                print('Você deseja analisar algum aluno?')
                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                while resposta not in ['S', 'N']:
                    limpar()

                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EFI):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                    print('Você deseja analisar algum aluno?')
                    print('Digito inválido! Tente novamente.')
                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    limpar()
                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EFI):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')
                    
                    print(f'\nQual aluno você deseja analizar?')
                    resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                    opcoes_validas = [str(i + 1) for i in range(len(alunos_EFI))]

                    while resposta not in opcoes_validas:
                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EFI):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                        print(f'\nQual aluno você deseja analizar?')
                        print('Digito Inválido! Tente novamente.')
                        resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                    indice = int(resposta) - 1
                    
                    limpar()
                    if len(alunos_EFI[indice]) <= 3:
                        print(f'Aluno: {alunos_EFI[indice]['nome']}')
                        print(f'Grade: {alunos_EFI[indice]['grade']}')
                        print(f'Escolaridade: {alunos_EFI[indice]['escolaridade']}')
                        print('O aluno não possui boletim registrado.')
                        print('Deseja registrar o boletim do aluno?')
                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                        while resposta not in ['S', 'N']:
                            print(f'Aluno: {alunos_EFI[indice]['nome']}')
                            print(f'Grade: {alunos_EFI[indice]['grade']}')
                            print(f'Escolaridade: {alunos_EFI[indice]['escolaridade']}')
                            print('O aluno não possui boletim registrado.')
                            print('Deseja registrar o boletim do aluno?')
                            print('Dígito Inválido! Tente novamente.')
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                        if resposta == 'S':
                            cadastrar = False
                            analisar = False
                            avaliar = True
                            skip = True
                            break
                            
                    ########################################################################## Aqui vai a parte que mostra os boletins
                else:
                    break
            else:
                limpar()

                print('Não tem nenhum aluno cadastrado no Ensino Fundamental I!')
                print('Deseja cadastrar algum aluno?')

                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    cadastrar = True
                    analisar = False
                    avaliar = False
                    skip = True
                else:
                    cadastrar = False

        elif resposta == '2':
            if len(alunos_EFII) > 0:
                limpar()

                print('Alunos do Ensino Fundamental I:\n')

                for cont, al in enumerate(alunos_EFII):
                    print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                print('Você deseja analisar algum aluno?')
                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                while resposta not in ['S', 'N']:
                    limpar()

                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EFII):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                    print('Você deseja analisar algum aluno?')
                    print('Digito inválido! Tente novamente.')
                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    limpar()
                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EFII):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')
                    
                    print(f'\nQual aluno você deseja analizar?')
                    resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                    opcoes_validas = [str(i + 1) for i in range(len(alunos_EFII))]

                    while resposta not in opcoes_validas:
                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EFII):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                        print(f'\nQual aluno você deseja analizar?')
                        print('Digito Inválido! Tente novamente.')
                        resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                    indice = int(resposta) - 1
                    
                    limpar()
                    if len(alunos_EFII[indice]) <= 3:
                        print(f'Aluno: {alunos_EFII[indice]['nome']}')
                        print(f'Grade: {alunos_EFII[indice]['grade']}')
                        print(f'Escolaridade: {alunos_EFII[indice]['escolaridade']}')
                        print('O aluno não possui boletim registrado.')
                        print('Deseja registrar o boletim do aluno?')
                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                        while resposta not in ['S', 'N']:
                            print(f'Aluno: {alunos_EFII[indice]['nome']}')
                            print(f'Grade: {alunos_EFII[indice]['grade']}')
                            print(f'Escolaridade: {alunos_EFII[indice]['escolaridade']}')
                            print('O aluno não possui boletim registrado.')
                            print('Deseja registrar o boletim do aluno?')
                            print('Dígito Inválido! Tente novamente.')
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                        if resposta == 'S':
                            cadastrar = False
                            analisar = False
                            avaliar = True
                            skip = True
                            break
                            
                    ########################################################################## Aqui vai a parte que mostra os boletins
                else:
                    break
            
        else: # resposta == '3':
            if len(alunos_EM) > 0:
                limpar()

                print('Alunos do Ensino Fundamental I:\n')

                for cont, al in enumerate(alunos_EM):
                    print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                print('Você deseja analisar algum aluno?')
                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                while resposta not in ['S', 'N']:
                    limpar()

                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EM):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                    print('Você deseja analisar algum aluno?')
                    print('Digito inválido! Tente novamente.')
                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    limpar()
                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EM):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')
                    
                    print(f'\nQual aluno você deseja analizar?')
                    resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                    opcoes_validas = [str(i + 1) for i in range(len(alunos_EM))]

                    while resposta not in opcoes_validas:
                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EM):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                        print(f'\nQual aluno você deseja analizar?')
                        print('Digito Inválido! Tente novamente.')
                        resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                    indice = int(resposta) - 1
                    
                    limpar()
                    if len(alunos_EM[indice]) <= 3:
                        print(f'Aluno: {alunos_EM[indice]['nome']}')
                        print(f'Grade: {alunos_EM[indice]['grade']}')
                        print(f'Escolaridade: {alunos_EM[indice]['escolaridade']}')
                        print('O aluno não possui boletim registrado.')
                        print('Deseja registrar o boletim do aluno?')
                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                        while resposta not in ['S', 'N']:
                            print(f'Aluno: {alunos_EM[indice]['nome']}')
                            print(f'Grade: {alunos_EM[indice]['grade']}')
                            print(f'Escolaridade: {alunos_EM[indice]['escolaridade']}')
                            print('O aluno não possui boletim registrado.')
                            print('Deseja registrar o boletim do aluno?')
                            print('Dígito Inválido! Tente novamente.')
                            resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                        if resposta == 'S':
                            cadastrar = False
                            analisar = False
                            avaliar = True
                            skip = True
                            break
                            
                    ########################################################################## Aqui vai a parte que mostra os boletins
                else:
                    break
    
    while avaliar == True:
        if skip == False:
            limpar()

            print('O aluno que você deseja avaliar é de qual escolaridade?')
            print('1 - Ensino Fundamental I')
            print('2 - Ensino Fundamental II')
            print('3 - Ensino Médio')

            resposta = str(input('Digite sua resposta - (1/2/3): ')).strip()

            while resposta not in ['1', '2', '3']:
                limpar()

                print('O aluno que você deseja avaliar é de qual escolaridade?')
                print('Digito inválido! Tente novamente.')
                resposta = str(input('Digite sua resposta - (1/2/3): ')).strip()

        if resposta == '1':
            if len(alunos_EFI) > 0:
                if skip == False:
                    limpar()

                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EFI):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                    print('Você deseja avaliar algum aluno?')
                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                    while resposta not in ['S', 'N']:
                        limpar()

                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EFI):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                        print('Você deseja avaliar algum aluno?')
                        print('Digito inválido! Tente novamente.')
                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    if skip == False:
                        limpar()
                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EFI):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')
                        
                        print(f'\nQual aluno você deseja avaliar?')
                        resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                        opcoes_validas = [str(i + 1) for i in range(len(alunos_EFI))]

                        while resposta not in opcoes_validas:
                            print('Alunos do Ensino Fundamental I:\n')

                            for cont, al in enumerate(alunos_EFI):
                                print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                            print(f'\nQual aluno você deseja avaliar?')
                            print('Digito Inválido! Tente novamente.')
                            resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                        indice = int(resposta) - 1
                        
                        limpar()
                    if len(alunos_EFI[indice]) <= 3:
                        limpar()
                        
                        print(f'Aluno: {alunos_EFI[indice]['nome']}')
                        print(f'Grade: {alunos_EFI[indice]['grade']}')
                        print(f'Escolaridade: {alunos_EFI[indice]['escolaridade']}')

                        print('Você deseja registrar o boletim de qual bimestre?')
                        resposta = str(input('Digite sua resposta? (1-4): '))

                        while resposta not in ['1', '2', '3', '4']:
                            limpar()
                        
                            print(f'Aluno: {alunos_EFI[indice]['nome']}')
                            print(f'Grade: {alunos_EFI[indice]['grade']}')
                            print(f'Escolaridade: {alunos_EFI[indice]['escolaridade']}')

                            print('Você deseja registrar o boletim de qual bimestre?')
                            print('Digito Inválido! Tente novamente.')
                            resposta = str(input('Digite sua resposta? (1-4): '))
                            
                        match resposta:
                            case '1':
                                print('Boletim 1° Bimestre (Registro): ')

                                if 'boletim_EF' not in alunos_EFI[indice]:
                                    alunos_EFI[indice]['boletim_EF'] = boletim_EF
                                    
                                for materia in materias_EF:
                                    alunos_EFI[indice][f'{boletim_EF[0]}'][f'{materia}'] = int(input(f'Nota de {materia}: '))
                                print(alunos_EFI[indice])
                                
                    else:
                        print()
                else:
                    break

            else:
                limpar()

                print('Não tem nenhum aluno cadastrado no Ensino Fundamental I!')
                print('Deseja cadastrar algum aluno?')

                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    cadastrar = True
                    analisar = False
                    avaliar = False
                    skip = True
                else:
                    cadastrar = False

        elif resposta == '2':
            if len(alunos_EFII) > 0:
                if skip == False:
                    limpar()

                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EFII):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                    print('Você deseja avaliar algum aluno?')
                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                    while resposta not in ['S', 'N']:
                        limpar()

                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EFII):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                        print('Você deseja avaliar algum aluno?')
                        print('Digito inválido! Tente novamente.')
                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    if skip == False:
                        limpar()
                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EFII):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')
                        
                        print(f'\nQual aluno você deseja avaliar?')
                        resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                        opcoes_validas = [str(i + 1) for i in range(len(alunos_EFII))]

                        while resposta not in opcoes_validas:
                            print('Alunos do Ensino Fundamental I:\n')

                            for cont, al in enumerate(alunos_EFII):
                                print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                            print(f'\nQual aluno você deseja avaliar?')
                            print('Digito Inválido! Tente novamente.')
                            resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                        indice = int(resposta) - 1
                        
                        limpar()
                    if len(alunos_EFII[indice]) <= 3:
                        limpar()
                        
                        print(f'Aluno: {alunos_EFII[indice]['nome']}')
                        print(f'Grade: {alunos_EFII[indice]['grade']}')
                        print(f'Escolaridade: {alunos_EFII[indice]['escolaridade']}')
                else:
                    break
                
            else:
                limpar()

                print('Não tem nenhum aluno cadastrado no Ensino Fundamental I!')
                print('Deseja cadastrar algum aluno?')

                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    cadastrar = True
                    analisar = False
                    avaliar = False
                    skip = True
                else:
                    cadastrar = False
            
        else: # resposta == '3':
            if len(alunos_EM) > 0:
                if skip == False:
                    limpar()

                    print('Alunos do Ensino Fundamental I:\n')

                    for cont, al in enumerate(alunos_EM):
                        print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                    print('Você deseja avaliar algum aluno?')
                    resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                    while resposta not in ['S', 'N']:
                        limpar()

                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EM):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                        print('Você deseja avaliar algum aluno?')
                        print('Digito inválido! Tente novamente.')
                        resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    if skip == False:
                        limpar()
                        print('Alunos do Ensino Fundamental I:\n')

                        for cont, al in enumerate(alunos_EM):
                            print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')
                        
                        print(f'\nQual aluno você deseja avaliar?')
                        resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                        opcoes_validas = [str(i + 1) for i in range(len(alunos_EM))]

                        while resposta not in opcoes_validas:
                            print('Alunos do Ensino Fundamental I:\n')

                            for cont, al in enumerate(alunos_EM):
                                print(f'{cont + 1} -> {al['nome']} - {al['grade']}º Ano - {al['escolaridade']}')

                            print(f'\nQual aluno você deseja avaliar?')
                            print('Digito Inválido! Tente novamente.')
                            resposta = str(input(f'Digite sua resposta - (1-{cont + 1}): ')).strip()

                        indice = int(resposta) - 1
                        
                        limpar()
                    if len(alunos_EM[indice]) <= 3:
                        limpar()
                        
                        print(f'Aluno: {alunos_EM[indice]['nome']}')
                        print(f'Grade: {alunos_EM[indice]['grade']}')
                        print(f'Escolaridade: {alunos_EM[indice]['escolaridade']}')
                else:
                    break
                
            else:
                limpar()

                print('Não tem nenhum aluno cadastrado no Ensino Fundamental I!')
                print('Deseja cadastrar algum aluno?')

                resposta = str(input('Digite sua resposta - (S/N): ')).strip().upper()

                if resposta == 'S':
                    cadastrar = True
                    analisar = False
                    avaliar = False
                    skip = True
                else:
                    cadastrar = False

