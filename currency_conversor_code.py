conversao_moeda = float(input("Digite o valor em reais que deseja converter: "))
moeda_destino = input("Digite a moeda para a qual deseja converter (USD, EUR, GBP): ").upper()

if moeda_destino == "USD":
    moeda_dolar = conversao_moeda / 5.16 #realiza a conversão para dólar
    print(f"O valor convertido para dólares é: ${moeda_dolar:.2f}")

elif moeda_destino == "EUR":
    moeda_euro = conversao_moeda / 5.90 #realiza a conversão para euro
    print(f"O valor convertido para euros é: €{moeda_euro:.2f}")

elif moeda_destino == "GBP":
    moeda_libra = conversao_moeda / 6.90 #realiza a conversão para libra esterlina
    print(f"O valor convertido para libras esterlinas é: £{moeda_libra:.2f}")

else:
    print("Moeda inválida. Por favor, escolha entre USD, EUR ou GBP.")
