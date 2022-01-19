import math
a = float(input('Me diga um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno de {:.0f}º é: {:.2f}, o cosseno é {:.2f} e a tangente é:{:.2f}'.format(a,s,c,t))
