'''
    Autores: 
    - Maycon Kaio Silva
    Turma: 2ºA DS               Data: 22/10/2025

    Exercício 4: Maycon
    - Crie um programa que gerencie o aproveitamento de jogadores de futebol.
    - O programa vai ler o nome dos jogadores e quantas partidas ele jogou.
    - Depois vair ler a quantidade de gols feitos em cada partida.
    - No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

from os import system
from time import sleep

jogadores = []  # lista para guardar todos os jogadores

# cores
black= "\033[0;30m" 
red= "\033[0;31m"
green= "\033[0;32m"
yellow= "\033[0;33m" 
blue= "\033[0;34m"
purple= "\033[0;35m"
cyan= "\033[0;36m"
orange = "\033[38;5;208m" 
reset= "\033[0m" 

system("cls")

print(f"{green}Oi, seja bem-vindo ao gerenciamento de aproveitamento de jogadores!{reset}\n")
sleep(2)

while True:
    cadas = input(f"{yellow}Deseja cadastrar algum jogador? {reset}(S/N) ").upper()
    if cadas in ["S", "N"]:
        break
    else:
        print(f"{red}❌ Digite apenas 'S' para sim ou 'N' para não!{reset}")

sleep(1)

while cadas == "S":
    system("cls") 
    jogador = {}   # cria um novo dicionário a cada cadastro
   
    # Validação do código
    while True:
        codigo = input(f"{yellow}Digite um código novo de 0 a 999 para o novo jogador:{reset} ")
        if codigo.isdigit():
            codigo = int(codigo)
            if 0 <= codigo <= 999:
                jogador["codigo"] = codigo
                break
            else:
                print(f"{red}❌ O código deve estar entre 0 e 999!{reset}")
        else:
            print(f"{red}❌ Digite apenas números inteiros!{reset}")
    
    # Validação de nome
    while True:
        nome = input(f"{yellow}Nome do jogador: {reset}").strip()
        valido = True

        for c in nome:
            if not ((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or c == ' '):
                valido = False
                break
        
        if nome == "":
            print(f"{red}❌ O nome não pode estar vazio!{reset}")
        elif not valido:
            print(f"{red}❌ O nome não pode conter números ou caracteres especiais!{reset}")
        else:
            jogador["nome"] = nome
            break

    # Validação das partidas jogadas
    while True:
        partidas = input(f"{yellow}Digite quantas partidas {jogador['nome']} jogou: {reset}")
        if partidas.isdigit():
            partidas = int(partidas)
            break
        else:
            print(f"{red}❌ Digite um número válido de partidas.{reset}")
    
    gols = []
    for i in range(partidas):
        while True:
            g = input(f"{green}Gols na partida {i+1}: {reset}")
            if g.isdigit():
                gols.append(int(g))
                break
            else:
                print(f"{red}❌ Digite um número inteiro válido.{reset}")
    
    jogador["partidas_jogadas"] = partidas
    jogador["gols_partida"] = gols
    jogador["total_gols"] = sum(gols)
    
    jogadores.append(jogador)
    
    print(f"\n{green}✅ Jogador cadastrado com sucesso!{reset}")
    sleep(1)
    
    # Validação de resposta S/N novamente
    while True:
        cadas = input(f"\n{yellow}Deseja cadastrar outro jogador? {reset}(S/N) ").upper()
        if cadas in ["S", "N"]:
            break
        else:
            print(f"{red}❌ Digite apenas 'S' ou 'N'!{reset}")

system("cls")

# mostra os códigos disponíveis
if len(jogadores) > 0:
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
                break
        
        if not encontrado:
            print(f"{red}❌ Nenhum jogador encontrado com esse código.{reset}")
    else:
        print(f"{red}❌ Código inválido! Digite apenas números.{reset}")

else:
    print(f"{red}⚠ Nenhum jogador foi cadastrado!{reset}")
