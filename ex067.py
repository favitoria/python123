c = 0
print('----TABUADA----')
num = int(input('Digite um valor: '))
while c <= 9:
    c += 1
    soma = num * c
    if num < 0:
        break
    print(f'{num:2} x {c:2} = {num*c:2}')

