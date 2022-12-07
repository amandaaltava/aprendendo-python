'''Programa que usa a tabela com os 20 times do brasileirão em sua ordem de classificação.
mostre:
apenas os 5 primeiros colocados
os 4 últimos colocados
A lista em ordem alfabética
em qual posição da lista está o Fortaleza
'''

times = ('Palmeiras', 'Inter', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athletico- PR', 'Atletico-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Os primeiros colocados são: {times[:5]}')
print(f'Os quatro últimos colocados são: {times[-4:]}')
print(f'Os colocados em ordem alfabética são: {sorted(times)}')
pos = times.index('Corinthians')
print(f'O Corinthians está na posição {pos+1}')