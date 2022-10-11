'''Faça um programa que leia uma frase qualquer e diga se
ela é um palíndromo desconsiderando os espaços

exemp palíndromos:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''

frase = str(input('Digite uma frase: ')).strip() .upper() #tira o espaços da frente e do final da palavra e joga tudo em maisucula  para poder comprar
palavras = frase.split() #separa em palavras individuais
junto = ''.join(palavras) #junta tudo sem espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1):# -1(para começar a contar da última letra p 1°), -1(começa a contar do 0 ) -1(vai voltando letra por letra) VAI FAZER A PALAVRA DE TRAS PARA FRENTE
       inverso += junto[letra]# monta e mostra a palavra ao contrario
if inverso == junto:
    print('Temos um palídromo')
else:
    print('Não é palíndromo')

'''
frase = str(input('frase')) .strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # joga a palavra do inicio para o final e de tras para frente
if inverso == junto:
    print('Palíndromo')
else:
    print('Não palíndromo')
'''