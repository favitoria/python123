n1 = float(input('Digite aqui sua primeira nota: '))
n2 = float(input('Digite aqui sua segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print('Com a média de {:.1f}, você foi REPROVADO!'.format(m))
elif 6.9 > m >= 5.0:
    print('Com a média de {:.1f}, você está de RECUPERAÇÃO!'.format(m))
elif m >= 7.0:
    print('Com a média de {:.1f}, você foi APROVADO!'.format(m))
