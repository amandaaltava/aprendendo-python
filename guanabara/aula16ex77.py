'''Programa que tenha uma tupla com varias palavras - sem qualquer acentuação
depois disso mostre quais sao as vogais de cada palavra'''

palavra = ('Lula', 'Suplicy', 'Gleisi', 'Genoino', 'Haddad')


for laco in palavra:      # Verifica a tupla
    print(f'\nNa palavra {laco} temos ', end='')    # Atribui a palavra da vez na impresao e junta  apróxima impressao na mesma linha
    for letra in laco:                   # Looping para a próxima impressao - das vogais
        if letra.lower() in 'aeiou':      # Verifica cada letra na palavra da vez se tem as vogais
            print(letra, end='')         # E então imprime a vogal, que sairá na mesma linha da frase impressa por último