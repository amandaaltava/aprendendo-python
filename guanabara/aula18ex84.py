galera = list()
dado = list()
totmai = 0
totme = 0

for p in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totme += 1
print(f'Temos {totmai} maiores de idade e {totme} menores de idade.')