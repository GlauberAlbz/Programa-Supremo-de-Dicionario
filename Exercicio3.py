'''
    Autores: 
    - Anna Caroline Nascimento Silva
    Turma: 2ºA DS               Data: 22/10/2025

    Exercício 3: Anna
    - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
    - Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    - Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

'''

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
    "inicio": "",
    "salario": "",
    "aposenta": "",
    "idadeAposenta": "",
    "contribuicao": ""
    }

while loop == "S":

    sys('cls')

    sleep(2)

    hj=dt.date.today()
    ctpsmodelo= "1"

    pessoa["nome"]= input(f"{purple}Digite seu nome: {reset}")
    
    
    while True:
        sleep(1)
        pessoa["nasc"] = input(f"{purple}Digite sua data de nascimento [DD/MM/AAAA]: {reset}")

        if len(pessoa["nasc"]) != 10 or pessoa["nasc"][2] != '/' or pessoa["nasc"][5] != '/':
            print(f"{red}Use o formato DD/MM/AAAA{reset}")
            continue

        dia, mes, ano = pessoa["nasc"].split('/')

        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
            print(f"{red}Use apenas números na data{reset}")
            continue

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if ano < 1900 or ano > hj.year:
            print(f"{red}Ano inválido{reset}")
            continue
        if mes < 1 or mes > 12:
            print(f"{red}Mês inválido{reset}")
            continue

        diasPorMes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28,
                        31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if dia < 1 or dia >diasPorMes[mes - 1]:
            print(f"{red}Dia inválido para o mês informado{reset}")
            continue

        datanasc = dt.date(ano, mes, dia)

        if datanasc > hj:
            print(f"{red}A data de nascimento não pode ser no futuro{reset}")
            continue
        if hj.year - ano > 120:
            print(f"{red}Idade acima de 120 anos parece incorreta{reset}")
            continue
        break

    sleep(1)

    pessoa["genero"]= (input(f"{purple}Digite seu gênero cadastrado no cartório [M/F]: {reset}").upper())
    
    while pessoa["genero"] not in ("M", "F"):
        print(f"{red}Gênero inválido{reset}")
        sleep(1)
        pessoa["genero"]= (input(f"{purple}Digite seu gênero cadastrado no cartório [M/F]: {reset}").upper())

    pessoa["idade"] = hj.year - datanasc.year - ((hj.month, hj.day) < (datanasc.month, datanasc.day))

    while ctpsmodelo not in ("0", ""):
        sleep(1)
        ctpsmodelo= (input(f"{pink}O modelo da sua CTPS é antigo ou novo? {green}[Digite '?' para mais informações]{reset}[{yellow}A{reset} -> {yellow}Antigo{reset}/ {orange}N{reset} -> {orange}Novo{reset}]: {reset}").upper())

        if ctpsmodelo not in ("0", "", "A", "N", "?", "1"):
            print(f"{red}Carteira de trabalho inválida{reset}")
            continue
        
        if ctpsmodelo == 'N':
            sleep(1)
            sys('cls')
            while True:
                sleep(1)
                pessoa["ctps"] = input(f"{purple}Digite seu CPF [Sem pontos, traços ou espaços - 11 dígitos]: {reset}")
                if len(pessoa["ctps"]) == 11 and pessoa["ctps"].isdigit():
                    break  
                else:
                    print(f"{red}O CPF deve ter exatamente 11 dígitos numéricos. Tente novamente{reset}")
            break  
        
        elif ctpsmodelo == 'A':
            sys('cls')
            while True:
                sleep(1)
                ct = input(f"{purple}Digite o número da sua carteira de trabalho [7 dígitos]: {reset}")
                if len(ct) == 7 and ct.isdigit():
                    break
                else:
                    print(f"{red}O número da CTPS deve ter exatamente 7 dígitos numéricos. Tente novamente{reset}")
            while True:
                sleep(1)
                ps = input(f"{purple}Digite a série da sua carteira de trabalho [4 dígitos]: {reset}")
                if len(ps) == 4 and ps.isdigit():
                    break 
                else:
                    print(f"{red}A série da CTPS deve ter exatamente 4 dígitos numéricos. Tente novamente{reset}")
            pessoa["ctps"]= ct+ps
            break
        
        elif ctpsmodelo == '?':
            sys('cls')
            sleep(1)
            print(f"{orange}Número da CTPS Digital (novo) -> Use o CPF para registro e consulta.\n\n{yellow}Número da CTPS Antiga (antigo) -> Use o Número e Série que constam na página de identificação do documento físico.{reset}")
        
        elif ctpsmodelo == "":
            ctpsmodelo = "0"

    if ctpsmodelo not in ("0", ""):

        while True:
            sleep(1)
            pessoa["contrato"] = (input(f"{purple}Digite o ano de contratação do seu contrato atual [AAAA]: {reset}"))
            if len(pessoa["contrato"]) == 4 and pessoa["contrato"].isdigit():
                pessoa["contrato"] = int(pessoa["contrato"])
                if hj.year - 100 <= pessoa["contrato"] <= hj.year and pessoa["contrato"] >= ano:
                    break
                else:
                    print(f"{red}Ano de contratação inválido{reset}")
                    continue
            else:
                print(f"{red}Formato inválido. Tente novamente{reset}")
                continue

        while True:
            sleep(1)
            pessoa["inicio"] = (input(f"{purple}Digite o ano de inicio de sua contribuição para a previdência [AAAA]: {reset}"))
            if len(pessoa["inicio"]) == 4 and pessoa["inicio"].isdigit():
                pessoa["inicio"] = int(pessoa["inicio"])
                if hj.year - 100 <= pessoa["inicio"] <= hj.year and pessoa["inicio"] >= ano:
                    break
                else:
                    print(f"{red}Ano de contribuição inválido{reset}")
                    continue
            else:
                print(f"{red}Formato inválido. Tente novamente{reset}")
                continue

        sleep(1)

        pessoa["salario"] = (input(f"{purple}Digite seu último sálario: {reset}"))

        while not pessoa["salario"].isdigit():
            print(f"{red}Use apenas números{reset}")
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
   
            sys('cls')
            
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
            sleep(5)

            sys('cls')

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
        sleep(5)

        sys('cls')

    loop= (input(f"{orange}Deseja cadastrar outra pessoa? [S/N] {reset}").upper())

    while loop not in ("S", "N"):
        print(f"{red}Digite uma opção válida{reset}")
        sleep(1)
        loop= (input(f"{orange}Deseja cadastrar outra pessoa? [S/N] {reset}").upper())

    if loop == "N":
        sleep(1)
        break
    
