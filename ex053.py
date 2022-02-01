frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junção = ''.join(palavras)
inverso = ''
for letra in range(len(junção) -1, -1, -1):
    inverso += junção[letra]
print(junção, inverso)
if inverso == junção:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
