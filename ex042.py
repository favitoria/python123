r1 = int(input('Digite o comprimento desta reta: '))
r2 = int(input('Digite o comprimento desta reta: '))
r3 = int(input('Digite o comprimento desta reta: '))
if not r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Essas retas NÃO PODEM formar um triângulo')
elif r1 == r2 == r3:
    print('Essas retas PODEM formar um triângulo!')
    print('Este triângulo é: EQUILÁTERO!')
elif r1 != r2 != r3 != r1:
    print('Essas retas PODEM formar um triângulo!')
    print('Este triângulo é: ESCALENO!')
else:
    print('Essas retas PODEM formar um triângulo!')
    print('Este triângulo é: ISÓSCELES!')