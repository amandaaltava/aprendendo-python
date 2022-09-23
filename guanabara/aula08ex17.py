'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}' .format(hipotenusa))'''

import math
co = float(input('O comprimento do cateto oposto é: '))
ca = float(input('O comprimento do cateto adjacente é: '))
hi = math.hypot(co, ca)
print('O comprimento da hypotenusa é {:.2f}' .format(hi))


