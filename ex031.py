d = int(input('Qual a distância em KM desta viagem?'))
if d<=200:
    taxa = d * 0.50
else:
    taxa = d * 0.45
print('O preço da passagem na distância de {}KM é {:.2f}R$'.format(d, taxa))
