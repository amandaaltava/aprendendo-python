'''Escreva um programa que leia a velocidade de um carro.. Se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7.00 por cada km acima do limite'''


'''from time import sleep

print('*-*' * 13)              #imprime a graça na tela
km = float(input('Qual a velocidade do seu carro? '))      #recebe a kilometragemm pelo usuário
print('*-*' * 13)
sleep(1)           #espera alguns instantes para apareer o restante do programa
if km <= 80:
    print('Velocidade segura! BOA VIAGEM!')
else:
    print('Multado!!! Velocidade acima do limite. MULTA de R${:.2f}.' .format((km - 80) * 7)) '''

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Velocidade acima do permitido!!')
    print('Você deve pagar uma multa de R${:.2f}!' .format((velocidade - 80) * 7))
print('Tenha um bom dia!')