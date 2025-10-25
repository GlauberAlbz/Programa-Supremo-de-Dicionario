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

loop= "S"

pessoa = {
    "nome": "",
    "genero": "",
    "nasc": "",
    "ctps": "",
    "idade": "",
    "contrato": "",
    "salario": "",
    "aposenta": "",
    "contribuicao": ""
    }
    


while loop == "S":
    hj=dt.date.today()
    ctpsmodelo= "1"

    pessoa["nome"]= input("Digite seu nome: ")
    
    while True:
        pessoa["nasc"] = input("Digite sua data de nascimento [DD/MM/AAAA]: ")

        # Verifica o formato básico
        if len(pessoa["nasc"]) != 10 or pessoa["nasc"][2] != '/' or pessoa["nasc"][5] != '/':
            print("Use o formato DD/MM/AAAA.")
            continue

        dia, mes, ano = pessoa["nasc"].split('/')

        # Verifica se todos são números
        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
            print("Use apenas números na data.")
            continue

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        # Validação básica de faixa de valores
        if ano < 1900 or ano > hj.year:
            print("Ano inválido")
            continue
        if mes < 1 or mes > 12:
            print("Mês inválido")
            continue
        # Dias válidos por mês
        diasPorMes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28,
                        31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if dia < 1 or dia >diasPorMes[mes - 1]:
            print("Dia inválido para o mês informado")
            continue

        datanasc = dt.date(ano, mes, dia)

        # Verifica se é futura ou idade absurda
        if datanasc > hj:
            print("A data de nascimento não pode ser no futuro")
            continue
        if hj.year - ano > 120:
            print("Idade acima de 120 anos parece incorreta")
            continue
        break

    pessoa["genero"]= (input("Digite seu gênero cadastrado no cartório [M/F]: ").upper())
    
    while pessoa["genero"] not in ("M", "F"):
        print("Gênero inválido.")
        pessoa["genero"]= (input("Digite seu gênero cadastrado no cartório [M/F]: ").upper())

    pessoa["idade"] = hj.year - datanasc.year - ((hj.month, hj.day) < (datanasc.month, datanasc.day))

    while ctpsmodelo not in ("0", ""):
        ctpsmodelo= (input("O modelo da sua CTPS é antigo ou novo? [Digite '?' para mais informações][A -> Antigo/ N -> Novo]: ").upper())

        if ctpsmodelo not in ("0", "", "A", "N", "?", "1"):
            print("Carteira de trabalho inválida")
            continue
        
        if ctpsmodelo == 'N':
            while True:
                pessoa["ctps"] = input("Digite seu CPF [Sem pontos, traços ou espaços - 11 dígitos]: ")
                if len(pessoa["ctps"]) == 11 and pessoa["ctps"].isdigit():
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
                    print("O número da CTPS deve ter exatamente 7 dígitos numéricos. Tente novamente.")
            while True:
                ps = input("Digite a série da sua carteira de trabalho [4 dígitos]: ")
                if len(ps) == 4 and ps.isdigit():
                    break 
                else:
                    print("A série da CTPS deve ter exatamente 4 dígitos numéricos. Tente novamente.")
            pessoa["ctps"]= ct+ps
            break
        
        elif ctpsmodelo == '?':
            print("Número da CTPS Digital (novo) -> Use o CPF para registro e consulta.\nNúmero da CTPS Antiga (antigo) -> Use o Número e Série que constam na página de identificação do documento físico.")
        
        elif ctpsmodelo == "":
            ctpsmodelo = "0"

    if ctpsmodelo not in ("0", ""):

        pessoa["contrato"] = int(input("Digite o ano de contratação do seu contrato atual [AAAA]: "))
        while pessoa["contrato"] < hj.year - 100 or pessoa["contrato"] > hj.year or pessoa["contrato"] < ano:
            print("Ano de contratação inválido")
            pessoa["contrato"] = int(input("Digite o ano de contratação do seu contrato atual [AAAA]: "))

        inicio = int(input("Digite o ano de inicio de sua contribuição para a previdência [AAAA]: "))
        while inicio < hj.year - 100 or inicio > hj.year or inicio < ano:
            print("Ano de contratação inválido")
            inicio = int(input("Digite o ano de inicio de sua contribuição para a previdência [AAAA]: "))

        pessoa["salario"] = (input("Digite seu último sálario: "))

        while not pessoa["salario"].isdigit():
            print("Use apenas números")
            pessoa["salario"] = (input("Digite seu último sálario: "))

        pessoa["salario"] = float(pessoa["salario"])
        
        pessoa["contribuicao"]= hj.year - inicio
        
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

            print(pessoa["aposenta"])

    loop= (input("Deseja cadastrar outra pessoa? [S/N] ").upper())

    while loop not in ("S", "N"):
        print("Digite uma opção válida")
        loop= (input("Deseja cadastrar outra pessoa? [S/N] ").upper())

    if loop == "N":
        break

        


    
    
