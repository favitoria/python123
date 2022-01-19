frase = str(input('Digite uma frase: ').strip().upper())
print('Nesta frase aparece {} vezes a letra A'.format(frase.count('A')))
print('Ela aparece na posição: {}'.format(frase.find('A')+1))
print('E para de aparecer na posição: {}'.format(frase.rfind('A')+1))