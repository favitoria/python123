nome = input('Diga o nome de sua cidade: ').strip()
print('Tem a palavra "SANTO" no começo do nome?')
dividido = nome.split()
d2 = dividido [0]
print(('SANTO' in d2.upper()))

cid = str(input('Em que cidade você nasceu? ')).strip().upper()
print(cid[:5] == 'SANTO')
