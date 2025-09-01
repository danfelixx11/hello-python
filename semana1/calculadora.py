def calculadora_desconto():
    while true:
        try:
            preco = float(input("Digite o preço do pruduto (R$): "))
            break
        except ValueError:
            print("Erro! Digite apenas números.")
    desconto_5 = preco * 0.95
    desconto_10 = preco * 0.90
    print(f"Preço original: R${preco:.2f}")
    print(f"com 5% de desconto: R${desconto_5:.2f}")
    print(f"Com 10% de desconto: R${desconto_10:.2f}")