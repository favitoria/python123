DN = int(input('Qual o seu ano de nascimento?'))
idade = 2022 - DN
if DN >= 2013:
    print('A categoria para quem tem {} anos na Confederação Nacional de Natação é: MIRIM'.format(idade))
elif DN >= 2008:
    print('A categoria para quem tem {} anos na Confederação Nacional de Natação é: INFANTIL'.format(idade))
elif DN >= 2003:
    print('A categoria para quem tem {} anos na Confederação Nacional de Natação é: JUNIOR'.format(idade))
elif DN >= 2002:
    print('A categoria para quem tem {} anos na Confederação Nacional de Natação é: SÊNIOR'.format(idade))
else:
    print('A categoria para quem tem {} anos na Confederação Nacional de Natação é: MASTER'.format(idade))
