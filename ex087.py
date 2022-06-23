#MINHAresolução
'''coluna1 = list()
coluna2 =list()
coluna3 = list()
listaPAR = list()
for v in range(0,9):
    valor = int(input(f'Digite um valor: '))
    if valor % 2 == 0:
        listaPAR.append(valor)
    if v <= 2:
        coluna1.append(valor)
    elif v == 3 or v == 4 or v == 5:
        coluna2.append(valor)
    elif v == 6 or v == 7 or v ==8:
        coluna3.append(valor)'''
#print(f''' [  {coluna1[0]}  ][  {coluna1[1]}  ][  {coluna1[2]}  ] ''')
#print(f''' [  {coluna2[0]}  ][  {coluna2[1]}  ][  {coluna2[2]}  ] ''')
#print(f''' [  {coluna3[0]}  ][  {coluna3[1]}  ][  {coluna3[2]}  ] ''')
#print(f'OS VALORES PARES DIGITADOS FORAM: {listaPAR}')
#print(f'A SOMA DOS VALORES PARES É: {sum(listaPAR)}')
#soma = coluna1[2] + coluna2[2] + coluna3[2]
#print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA {coluna1[2], coluna2[2], coluna3[2] } É: {soma}')
#print(f'O MAIOR VALOR DA SEGUNDA LINHA {coluna2} É: {max(coluna2)}')

#GUANABARAresolução/MINHA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
listaPARES = []
linha2 = list()
coluna3 = list()
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            listaPARES.append(matriz[linha][coluna])
        elif matriz[1][coluna]:
            linha2.append(matriz[1][coluna])
        elif matriz[linha][2]:
            coluna3.append(matriz[linha][2])
print('=*' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'Os valores PARES digitados foram: {listaPARES}')
print(f'A soma dos valores pares é: {sum(listaPARES)}')
print(f'A soma dos valores da terceira coluna é: {max(coluna3)}')
print(f'O maior valor da segunda linha é: {max(linha2)}')
