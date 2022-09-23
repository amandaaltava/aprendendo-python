'''Verificar se existe a palavra silva no nome de uma pessoa.
fiz como se fosse o nome silva, e não apenas a palavra silva'''

nome = str(input('Qual seu nome completo?: ')).strip().upper().split()
print('SILVA' in nome)


