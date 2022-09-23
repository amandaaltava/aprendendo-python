import math
ang = float(input('Qual é o angulo a ser analisado?: '))
se = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O Angulo {:.2f} possui o seno {:.2f} o cosseno {:.2f} e a tangente {:.2f}.'.format(ang, se, co, tang))
