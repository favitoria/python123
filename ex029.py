v = float(input('Qual a velocidade do seu carro neste momento? '))
if v>80:
    print('VOCÊ ESTÁ A {}KM/H EM UMA PISTA DE 80KM/H. VOCÊ FOI MULTADO!'.format(v))
    taxa = (v - 80) * 7
    print('A MULTA CUSTARÁ: {:.0f}R$'.format(taxa))

