'''Programa que leia um número pelo teclado entre 0 e 20 e
escreva ele por extenso'''

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))   #Pede o número ao usuário
while True:                                         #Enquanto o número inserido não estiver entre 0 e 20 ele solicita o número novamente, se for entre 0 e 20 ele sai do loop
    if n not in range(0, 20):
        n = int(input('Digite novamente. Digite um número entre 0 e 20:'))
    else:
        break
print(f'você digitou {tupla[n]}')   #Imprime o item digitado da tupla associado ao índex

