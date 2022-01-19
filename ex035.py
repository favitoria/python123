r1 = int(input('Digite o comprimento desta reta: '))
r2 = int(input('Digite o comprimento desta reta: '))
r3 = int(input('Digite o comprimento desta reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Essas retas PODEM formar um triângulo!')
else:
    print('Essas retas NÃO PODEM formar um triângulo')
