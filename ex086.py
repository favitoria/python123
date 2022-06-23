#MINHAresolução
'''coluna1 = list()
coluna2 =list()
coluna3 = list()
for v in range(0,9):
    valor = int(input(f'Digite um valor: '))
    if v <= 2:
        coluna1.append(valor)
    elif v == 3 or v == 4 or v == 5:
        coluna2.append(valor)
    else:
        coluna3.append(valor)'''
#print(f''' [  {coluna1[0]}  ][  {coluna1[1]}  ][  {coluna1[2]}  ] ''')
#print(f''' [  {coluna2[0]}  ][  {coluna2[1]}  ][  {coluna2[2]}  ] ''')
#print(f''' [  {coluna3[0]}  ][  {coluna3[1]}  ][  {coluna3[2]}  ] ''')
#print(f'oi')

#GUANABARAresolução
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=*' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
