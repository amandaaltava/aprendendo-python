km = float(input('Quantos kilometros o carro percorreu? '))
dias = int(input('Por quantos dias esse carro foi alugado? '))
pagarme = km * 0.15 + (dias * 60)
print(f'O valor total a ser pago por esse aluguel é de R$ {pagarme}.')
