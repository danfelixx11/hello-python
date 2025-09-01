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