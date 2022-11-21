'''Faça um programq que leia o primeiro termo e
a razão de uma PROGRESSAO ARITIMÉTICA
 no final mostre os 10 PRIMEIROS TERMOS dessa progressao
 e pergunte ao usuário quantos termos ele ainda quer mostrar

 obs: pulando de tantos em tantos'''

pt = int(input('Pirmeiro termo: '))
r = int(input('Razão da P.A.: '))
termo = pt
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo = termo + r
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos vc ainda quer ver a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
