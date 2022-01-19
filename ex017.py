import math
cop = float(input('Qual o cacteto oposto deste triângulo?'))
cadj = float(input('E qual é o caceto adjacente?'))
hq = pow(cop,2) + pow(cadj,2)
h = math.sqrt(hq)
print('O comprimento da hipotenusa é: {:.2f}'.format(h))

copteste = float(input('Qual o cacteto oposto deste triângulo?'))
cadjteste = float(input('E qual é o caceto adjacente?'))
hteste = math.hypot(copteste, cadjteste)
print('O comprimento da hipotenusa é: {:.2f}'.format(hteste))

