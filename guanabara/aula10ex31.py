'''Faça um progama que pergunte a distância em km e calcule o preço da passagem cobrando
R$ 0,50 por km para viagens até 200km e R$ 0,45 para viagens mais longas.'''

from time import sleep

km = float(input('Quantos km terá a merda da sua viagem?: '))
print('EM PROCESSAMENTO...')
sleep(1)
if km <= 200:
    print('A sua viagem será de {}km, então a sua pasagem custará R$ {:.2f}.' .format(km, km * 0.50))
else:
    print('A sua viagem será de {}km, então custará R$ {:.2f}.' .format(km, km * 0.45))
print('Faça uma boa viagem!')

