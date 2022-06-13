resposta = 'Ss'
numeros = 0
listaTODOS = []
listaPAR = []
listaIMPAR = []
while resposta != 'N':
    numeros = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar [S/N]? '))
    if numeros % 2 == 0:
        listaPAR.append(numeros)
    elif numeros % 2 == 1:
        listaIMPAR.append(numeros)
    listaTODOS.append(numeros)
print(f'Os valores PARES digitados foram: {listaPAR}')
print(f'Os valores IMPARES digitados foram: {listaIMPAR}')
listaTODOS.sort()
print(f'No TOTAL foram: {listaTODOS}')