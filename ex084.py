povao = list()
dado = list()
maiorpeso = menorpeso = 0
nomemaior = ''
nomemenor = ''
while True:
    dado.append(str(input('NOME: ')))
    dado.append(float(input('PESO: ')))
    maiorpeso = dado[1]
    povao.append(dado[:])
    dado.clear()
    resposta = input('Quer continuar [s/n]? ')
    for p in povao:
        if p[1] >= maiorpeso:
            maiorpeso = p[1]
            nomemaior = p[0]
        elif p[1] < maiorpeso:
            menorpeso = p[1]
            nomemenor = p[0]
    if resposta != 's':
        break
print(f'Você cadastrou {len(povao)} pessoas')
print(f'O maior peso foi de: {maiorpeso}kg. Peso de: ', end='')
for u in povao:
    if u[1] == maiorpeso:
        print(u[0])
print(f'O menor peso foi de: {menorpeso}kg. Peso de: ', end='')
for u in povao:
    if u[1] == menorpeso:
        print(u[0])
