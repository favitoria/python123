s = int(input('Qual é o teu salário? '))
if s>1250:
    aumento = s + (s*10/100)
else:
    aumento = s + (s*15/100)
print('Estarei aumentando seu salário em 15%, agora você recebe {:.2f}R$'.format(aumento))
