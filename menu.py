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

#==========================
# Exercícios
#==========================
def calculadora_desconto():
    while True:
        try:
            preco = float(input("Digite o preço do produto (R$): "))
            break
        except ValueError:
            print("Erro! Digite apenas números.")
    desconto_5 = preco * 0.95
    desconto_10 = preco * 0.90
    print(f"Preço original: R${preco:.2f}")
    print(f"Com 5% de desconto: R${desconto_5:.2f}")
    print(f"Com 10% de desconto: R${desconto_10:.2f}")


def conversor_moeda():
    while True:
        try:
            reais = float(input("Digite o valor em reais (R$): "))
            break
        except ValueError:
            print("Erro! Digite apenas números.")
    cotacao = 6
    euros = reais / cotacao
    print(f"Valor em euros: €{euros:.2f}")


def idade_em_dias():
    while True:
        try:
            idade = int(input("Digite sua idade em anos: "))
            break
        except ValueError:
            print("Erro! Digite apenas números inteiros.")
    dias = idade * 365
    print(f"Você já viveu aproximadamente {dias} dias.")

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
            calculadora_desconto()
        elif opcao == "2":
            conversor_moeda()
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