'''
    Autores: 
    - Anna Caroline Nascimento Silva
    Turma: 2ºA DS               Data: 22/10/2025

    Exercício 3: Anna
    - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
    - Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    - Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

'''

import random as rd
from time import sleep
from os import system as sys
import datetime as dt

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

nome= []
genero= []
nasc= []
ctps= []
idade= []
contrato= []
salario= []
aposenta= []

hj=dt.date.today()
contribuicao= hj.year - contrato
ctpsmodelo= "1"
loop= "S"


while loop == "S":

    nome= input("Digite seu nome: ")
    nasc= input("Digite sua data de nascimento [DD/MM/AAA]: ")
    genero= (input("Digite seu gênero cadastrado no cartório [M/F]: ").upper())

    datanasc = dt.datetime.strptime(nasc, "%d/%m/%Y").date()
    idade = hj.year - datanasc.year - ((hj.month, hj.day) < (datanasc.month, datanasc.day))

    while ctpsmodelo not in ("0", ""):
        ctpsmodelo= (input("O modelo da sua CTPS é antigo ou novo? [Digite '?' para mais informações][A -> Antigo/ N -> Novo]: ").upper())
        if ctpsmodelo == 'N':
            while True:
                ctps = input("Digite seu CPF [Sem pontos, traços ou espaços - 11 dígitos]: ")
                if len(ctps) == 11 and ctps.isdigit():
                    break  
                else:
                    print("ERRO: O CPF deve ter exatamente 11 dígitos numéricos. Tente novamente.")
            break  
        elif ctpsmodelo == 'A':
            while True:
                ct = input("Digite o número da sua carteira de trabalho [7 dígitos]: ")
                if len(ct) == 7 and ct.isdigit():
                    break
                else:
                    print("ERRO: O número da CTPS deve ter exatamente 7 dígitos numéricos. Tente novamente.")
            while True:
                ps = input("Digite a série da sua carteira de trabalho [4 dígitos]: ")
                if len(ps) == 4 and ps.isdigit():
                    break 
                else:
                    print("ERRO: A série da CTPS deve ter exatamente 4 dígitos numéricos. Tente novamente.")
            ctps= ct+ps
            break
        elif ctpsmodelo == '?':
            print("Número da CTPS Digital (novo) -> Use o CPF para registro e consulta.\nNúmero da CTPS Antiga (antigo) -> Use o Número e Série que constam na página de identificação do documento físico.")
        elif ctpsmodelo == "":
            ctpsmodelo = "0"

    if ctpsmodelo not in ("0", ""):
        contrato = input("Digite o ano de contratação do seu contrato atual: [AAAA]")
        salario = input("Digite seu último sálario: ")
        
        if genero == "M":
            idademin= 65
            contribmin= 20
            
        elif genero == "F":
            idademin= 62
            contribmin= 15

        
       

    loop= (input("Deseja cadastrar outra pessoa? [S/N] ").upper())

    while loop not in ("S", "N"):
        print("Digite uma opção válida")
        loop= (input("Deseja cadastrar outra pessoa? [S/N] ").upper())

    if loop == "N":
        break

        


    
    
