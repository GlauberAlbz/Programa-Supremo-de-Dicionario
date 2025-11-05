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


print((cyan) + '╔' + '═' * 73 + '╗')
print('║' + (reset) + f'Oi, seja bem-vindo ao gerenciamento de aproveitamento de jogadores!'.center(73) + (cyan) + '║')
print('╚' + '═' * 73 + '╝' + reset)
sleep(2)

print((yellow) + "=" * 75)

while True:
    system("cls")
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
    system("cls") 
    jogador = {}   # cria um novo dicionário a cada cadastro
   
    # Validação do código
    while True:
        system("cls")
        print((cyan) + '╔' + '═' * 73 + '╗')
        print('║' + (reset) + f'Digite um código novo de 1 a 999 para o novo jogador'.center(73) + (cyan) + '║')
        print('╚' + '═' * 73 + '╝\n' + reset)

        codigo = input("Sua reposta: ")
        
        if codigo == "0":
            print("não pode")
            sleep(2)
        
        elif codigo.isdigit():
            codigo = int(codigo)
            
            if 1 <= codigo <= 999:
                jogador["codigo"] = codigo
                break
            else:
                print((red) + '╔' + '═' * 73 + '╗')
                print('║' + (yellow) + f'❌ O código deve estar entre 0 e 999!'.center(73) + (red) + '║')
                print('╚' + '═' * 73 + '╝\n' + reset)
                sleep(2)
                
        else:
            print((red) + '╔' + '═' * 73 + '╗')
            print('║' + (yellow) + f'❌ Digite apenas números inteiros!'.center(73) + (red) + '║')
            print('╚' + '═' * 73 + '╝\n' + reset)
            sleep(2)

            
    
    # Validação de nome
    while True:
        nome = input(f"{yellow}Nome do jogador: {reset}").strip().capitalize()
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
            if partidas > 1391:
                print(f"é bem improvável que {jogador['nome']} tenha jogado essa quantidade de partidas, o recorde é 1,391.")
            else:
                partidas = int(partidas)
                break
        else:
            print(f"{red}❌ Digite um número válido de partidas.{reset}")
    
    gols = []
    for i in range(partidas):
        while True:
            g = input(f"{green}Gols na partida {i+1}: {reset}")
            if g.isdigit():
                g = int(g)
                if g > 16:
                    print("muito gol fi")
                else:
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
        cadas = input(f"\n{yellow}Deseja cadastrar outro jogador? {reset}(S/N) ").upper().strip()
        if cadas in ["S", "N"]:
            break
        else:
            print(f"{red}❌ Digite apenas 'S' ou 'N'!{reset}")

# mostra os códigos disponíveis

respo_jogas = True

if len(jogadores) > 0:
    while respo_jogas == True:
        system("cls")
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
                        pergunta = str(input("quer ver outro soccer????")).strip().upper()

                        if pergunta == "N":
                            respo_jogas = False
                        elif pergunta == "S":
                            respo_jogas == True
                            sleep(0.5)
                        else:
                            print("Resposta Inválida, tente novamente")
                            sleep(2)
                            system("cls")
                            
            if not encontrado:
                print(f"{red}❌ Nenhum jogador encontrado com esse código.{reset}")
                sleep(1.5)
        else:
            print(f"{red}❌ Código inválido! Digite apenas números.{reset}")
            sleep(1.5)

else:
    print(f"{red}⚠ Nenhum jogador foi cadastrado!{reset}")
