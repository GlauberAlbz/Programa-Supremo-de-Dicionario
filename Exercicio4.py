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

    system("cls")
    
    while True:
        system("cls")
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
        system("cls")
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
            system("cls")
            g = input(f"{green}Gols na partida {i+1}: {reset}")
            if g.isdigit():
                g = int(g)
                if g > 16:
                    print((red) + '╔' + '═' * 73 + '╗')
                    print('║' + (yellow) + f'❌ Quantidade exacerbada de gols, o limite é 16.'.center(73) + (red) + '║')
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
        system("cls")
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
                            system("cls")
                            
            if not encontrado:
                print(f"{red}❌ Nenhum jogador encontrado com esse código.{reset}")
                sleep(1.5)
        else:
            print(f"{red}❌ Código inválido! Digite apenas números.{reset}")
            sleep(1.5)

else:
    print(f"{red}⚠ Nenhum jogador foi cadastrado!{reset}")
