import os

#========================
# Códigos ANSI para cores
#========================
ROXO = '\033[95m'
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'  # Para voltar à cor normal

#==========================
# Função para limpar a tela
#==========================
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#=========================================
# Pausa para o usuário ler antes de voltar
# ========================================
def pausar():
    input(f"\n{AMARELO}Pressione Enter para continuar...{RESET}")

#================================
# Entrada numérica segura (float)
# ===============================
def obter_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(f"{VERMELHO}Erro! Digite um número válido.{RESET}")

#===============================
# Entrada numérica segura (int)
#===============================
def obter_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f"{VERMELHO}Erro! Digite um número inteiro válido.{RESET}")

#===============================================
# Cotação global (pode ser alterada no submenu)
#===============================================

cotacao_euro = 6.0 # 1€ = 6,00 R$ (Valor inicial)

#==========================
# Exercícios
#==========================

def submenu_conversor():
    global cotacao_euro # vamos alterar/ler a variável global aqui
    while True:
        limpar_tela()
        print(f"{ROXO}=== CONVERSOR DE MOEDA ==={RESET}")
        print(f"Cotação atual: {VERDE}1 € = R$ {cotacao_euro:.2f}{RESET}\n")
        print(f"{AZUL}1.{RESET} Reais (R$) → Euros (€)")
        print(f"{AZUL}2.{RESET} Euros (€) → Reais (R$)")
        print(f"{AZUL}3.{RESET} Alterar cotação")
        print(f"{AZUL}0.{RESET} Voltar ao menu principal")

        opc = input(f"\n{AMARELO}Escolha uma opção: {RESET}")

        if opc == "1":
            # R$ -> €
            valor_reais = obter_float("Digite o valor em reais (R$): ")
            euros = valor_reais / cotacao_euro
            print(f"\n{VERDE}Resultado: €{euros:.2f}{RESET}")
            pausar()

        elif opc == "2":
            # € -> R$
            valor_euros = obter_float("Digite o Valor em euros (€): ")
            reais = valor_euros * cotacao_euro
            print(f"\n{VERDE}Resultado: R${reais:.2f}{RESET}")
            pausar()

        elif opc == "3":
            # Alterar cotação
            nova = obter_float("Nova cotação (quanto vale 1 € em R$): ")
            if nova <= 0:
                print(f"{VERMELHO}Cotação inválida. Use um valor maior que zero.{RESET}")
            else:
                cotacao_euro = nova
                print(f"{VERDE}Cotação atualizada: 1 € = R$ {cotacao_euro:.2f}{RESET}")
            pausar()

        elif opc == "0":
            # Voltar ao menu principal
            break

        else:
            print(f"{VERMELHO}Opção inválida, tente novamente.{RESET}")
            pausar()

def submenu_desconto():
    while True:
        limpar_tela()
        print(f"{ROXO}=== CALCULADORA DE DESCONTO ==={RESET}")
        print(f"{AZUL}1.{RESET} Desconto percentual (%)")
        print(f"{AZUL}2.{RESET} Desconto em valor fixo (R$)")
        print(f"{AZUL}0.{RESET} Voltar ao menu principal")

        opc = input(f"\n{AMARELO}Escolha uma opção: {RESET}")
        
        if opc == "1":
            preco = obter_float("Digite o preço do produto (R$): ")
            perc = obter_float("Digite o percentual de desconto (%): ")
            final = preco * (1 - perc/100)
            print(f"\n{VERDE}Preço com {perc:.1f}% de desconto: R${final:.2f}{RESET}")
            pausar()

        elif opc == "2":
            preco = obter_float("Digite o preço do produto (R$): ")
            valor = obter_float("Digite o valor do desconto (R$): ")
            final = preco - valor
            if final < 0:
                final = 0
            print(f"\n{VERDE}Preço com desconto de R${valor:.2f}: R${final:.2f}{RESET}")
            pausar()

        elif opc == "0":
            break

        else:
            print(f"{VERMELHO}Opção inválida, tente novamente.{RESET}")
            pausar()


def idade_em_dias():
    while True:
        try:
            idade = obter_int("Digite sua idade em anos: ")
            break
        except ValueError:
            print("Erro! Digite apenas números inteiros.")
    dias = idade * 365
    meses = idade * 12
    print(f"\n{VERDE}Você já viveu aproximadamente:{RESET}")
    print(f"- {dias} dias")
    print(f"- {meses} meses")
    print(f"- {idade} anos")
    pausar()

#=========================
# Menu interativo
#=========================
def menu():
    while True:
        limpar_tela() 
        print(f"{ROXO}=== MENU PRINCIPAL ==={RESET}")
        print(f"{AZUL}1.{RESET} Calculadora de Desconto")
        print(f"{AZUL}2.{RESET} Conversor de Moeda")
        print(f"{AZUL}3.{RESET} Idade em Dias")
        print(f"{AZUL}0.{RESET} Sair")
    
        opcao = input(f"{AMARELO}Escolha uma opção: {RESET}")

        if opcao == "1":
            submenu_desconto()
        elif opcao == "2":
            submenu_conversor()
        elif opcao == "3":
            idade_em_dias()
        elif opcao == "0":
            print(f"{VERDE}Saindo... até mais!{RESET}")
            break
        else:
            print(f"{VERMELHO}Opção inválida, tente de novo.{RESET}")

        input(f"\n{AMARELO}Pressione Enter para voltar ao menu...{RESET}")

#==========================
# Executar o menu
#==========================
       
menu()