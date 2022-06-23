listaPAR = list()
listaIMPAR = list()
listona = [[listaPAR], [listaIMPAR]]
valor = 0
for v in range(0,7):
    valor = int(input(f'DIGITE UM VALOR PARA A POSIÇÃO {v+1}º: '))
    if valor % 2 == 0:
        listaPAR.append(valor)
    else:
        listaIMPAR.append(valor)
print(f'Os valores ÍMPARES digitados foram: {sorted(listaIMPAR)}')
print(f'Os valores PARES digitados foram: {sorted(listaPAR)}')