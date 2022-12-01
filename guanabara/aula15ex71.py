'''Programa que simula um caixa eletronico
Pergunta quanto será o valor sacado
e vai informar quantas cédulas de cada valor serão entregues
Considerando as notas de
50, 20, 10 e 1'''

print('=' * 20)
print('BANCO DO OVO')
valor = int(input('Qual valor quer sacar? R$'))
print('=' * 20)
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:    #o total recebe o valor pq esse valor seguirá diminuindo
        total = total - ced  #se o valor for igual ao valor da cédula(que começa em 50) o total fica o valor dele menos o da cédula
        totced = totced + 1  #contador de quantas vezes tirou a cédula daquele valor

    else:             #condição
        if totced > 0:        #se o valor já for 0 pode imprimir o resultado
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:          #se o valor da nota atual for 50, ela recebe a cédula de 20
            ced = 20
        elif ced == 20:        #se o valor da nota atual for 20, ela recebe a cédula de 10
            ced = 10
        elif ced == 10:        #se o valor da nota atual for 10, ela recebe a cédula de 01
            ced = 1
        totced = 0           #zera a variável para refazer o looping
        if total == 0:       #quando chegar em 0 acabou o dinheiro e finaliza o looping
            break
print('Volte sempre ao banco do OVO.')