P = float(input('Digite seu peso: '))
A = float(input('Digite sua altura: '))
IMC = P / pow(A, 2)
if IMC <= 18.5:
    print('Seu IMC é {}! Você está ABAIXO DO PESO!'.format(IMC))
    print('Se cuide!!')
elif IMC > 18.5 and IMC <= 25:
    print('Seu IMC é {:.1f}! Você está com o PESO IDEAL!'.format(IMC))
    print('PARABÉNS')
elif IMC > 25 and IMC <= 30:
    print('Seu IMC é {:.1f}! Você está com SOBREPESO!'.format(IMC))
    print('Se cuide!!')
elif IMC > 30 and IMC <= 40:
    print('Seu IMC é {:.1f}! Você está com OBESIDADE!'.format(IMC))
    print('Se cuide!!')
elif IMC > 40:
    print('Seu IMC é {:.1f}! Você está com OBESIDADE MÓRBIDA!'.format(IMC))
    print('POR FAVOR, se cuide!!')

