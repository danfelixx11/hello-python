# 1 - Calculadora de Desconto
preco = float(input("Digite o preço do produto: "))
print(f"Preço com 5% de desconto: {preco * 0.95:.2f}")
print(f"Preço com 10% de desconto: {preco * 0.90:.2f}")

# 2 - Conversor de Moeda
reais = float(input("Digite o valor em reais (R$): "))
cotacao = 6  # 1 euro = 6 reais (fictício)
print(f"Valor em euros: €{reais / cotacao:.2f}")

# 3 - Idade em Dias
idade = int(input("Digite sua idade em anos: "))
print(f"Você já viveu aproximadamente {idade * 365} dias.")
