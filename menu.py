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
# Normaliza e converte números
#================================
def _normalize_number_str(s: str) -> str:
    s = s.strip()
    # remove espaços e símbolos de moeda mais comuns
    s = s.replace(' ', '').replace('R$', '').replace('$', '')
    # se vier tanto ',' quanto '.': decidir qual é o decimal pela posição
    if ',' in s and '.' in s:
        if s.rfind(',') > s.rfind('.'):
            # vírgula aparece por último -> formato europeu: 1.234,56
            s = s.replace('.', '')    # remove separador de milhares
            s = s.replace(',', '.')   # vírgula -> ponto decimal
        else:
            # ponto aparece por último -> formato americano: 1,234.56
            s = s.replace(',', '')    # remove separador de milhares
    else:
        # se só houver vírgula, troca por ponto; senão deixa como está
        s= s.replace(',', '.')
    return s


#================================
# Entrada numérica segura (float)
# ===============================
def obter_float(msg):
    while True:
        raw = input(msg)
        norm = _normalize_number_str(raw)
        try:
            return float(norm)
        except ValueError:
            print(f"{VERMELHO}Erro! Digite um número válido (use vírgula ou ponto).{RESET}")

#===============================
# Entrada numérica segura (int)
#===============================
def obter_int(msg):
    while True:
        raw = input(msg)
        norm = _normalize_number_str(raw)
        try:
            val = float(norm)
            if val.is_integer():
                return int(val)
            else:
                print(f"{VERMELHO}Erro! Digite um número inteiro, sem casas decimais.{RESET}")
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


def contador_vogais():
    limpar_tela()
    print(f"{ROXO}=== CONTADOR DE VOGAIS ==={RESET}")

    frase = input("Digite uma frase qualquer: ")

    vogais = "aeiouAEIOU"
    contador = 0

    for letra in frase:
        if letra in vogais:
            contador += 1
    

    print(f"\n{VERDE}A frase digitada foi:{RESET} {frase}")
    print(f"{VERDE}Quantidade de vogais:{RESET} {contador}")
    

    pausar()


def boletim_notas():
    limpar_tela()
    print(f"{ROXO}=== BOLETIM DE NOTAS ==={RESET}")

    # 1) Pergunta quantas notas serão informadas (vamos usar for com range)
    n = obter_int("Quantas notas deseja informar? ")

    
    # 2) Validação simples
    if n <= 0:
        print(f"{VERMELHO}Você precisa informar pelo menos 1 nota.{RESET}")
        pausar()
        return  # sai da função e volta ao menu
    
    
    # 3) Cria uma lista vazia para armazenar as notas
    notas = []

    
    # 4) Laço for para coletar N notas
    for i in range(n):
        nota = obter_float(f"Digite a nota {i+1}: ")
        notas.append(nota)

    
    # 5) Cálculos (mostro com for para você treinar, e também a forma "pythonica")
    soma = 0
    for nota in notas:
        soma += nota

    media = soma / n
    maior = max(notas)
    menor = min(notas)

    
    # 6) Saída formatada
    print(f"\n{VERDE}Resumo do Boletim:{RESET}")
    print(f"- Quantidade de notas: {n}")
    print(f"- Notas informadas: {notas}")
    print(f"- Soma: {soma:.2f}")
    print(f"- Média: {media:.2f}")
    print(f"- Maior nota: {maior:.2f}")
    print(f"- Menor nota: {menor:.2f}")


    # 7) Extra: mostrar as notas com índice (treino de enumerate)
    print("\nNotas por posição (índice → valor):")
    for indice, valor in enumerate(notas, start=1):
        print(f"  {indice} → {valor:.2f}")


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
        print(f"{AZUL}4.{RESET} Boletim de Notas")
        print(f"{AZUL}5.{RESET} Contador de Vogais")
        print(f"{AZUL}0.{RESET} Sair")
    
        opcao = input(f"{AMARELO}Escolha uma opção: {RESET}")

        if opcao == "1":
            submenu_desconto()
        elif opcao == "2":
            submenu_conversor()
        elif opcao == "3":
            idade_em_dias()
        elif opcao == "4":
            boletim_notas()
        elif opcao == "5":
            contador_vogais()
        elif opcao == "0":
            print(f"{VERDE}Saindo... até mais!{RESET}")
            break
        else:
            print(f"{VERMELHO}Opção inválida, tente de novo.{RESET}")

        pausar()

#==========================
# Executar o menu
#==========================
       
menu()