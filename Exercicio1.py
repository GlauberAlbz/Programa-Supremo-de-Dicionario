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
alunos = [alunos_EFI, alunos_EFII, alunos_EM]
aluno = dict()

print('Bem vindo!')
print('Programa de notas.')

loopprincipal = True

while loopprincipal == True:

    cadastrar = str(input('Você deseja cadastrar um aluno? S/N'))

    if cadastrar == 'S':
        cadastrar = True
    else:
        cadastrar = False

    while cadastrar == True:
        
        aluno['Nome'] = str(input('Digite o nome do(da) aluno(a): '))
        aluno['Grade'] = int(input('Digite a grade do(da) aluno(a): '))

        if aluno['Grade'] > 0 and aluno['Grade'] < 6: # Adiciona a escolaridade do aluno
            aluno['Escolaridade'] = 'Ensino Fundamental I'
        elif aluno['Grade'] > 6 and aluno['Grade'] < 10:
            aluno['Escolaridade'] = 'Ensino Fundamental II'
        else:
            aluno['Escolaridade'] = 'Ensino Médio'
        
        if aluno['Escolaridade'] == 'Ensino Fundamental I': # Adiciona o aluno em uma lista com outros da mesma escolaridade
            alunos_EFI.append(aluno.copy())
        elif aluno['Escolaridade'] == 'Ensino Fundamental II':
            alunos_EFII.append(aluno.copy())
        else:
            alunos_EM.append(aluno.copy())
        
        cadastrar = str(input('Você deseja cadastrar outro aluno? S/N'))
        if cadastrar == 'S':
            cadastrar = True
        else:
            cadastrar = False