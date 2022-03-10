números = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num > 0 and num > 20:
    num = int(input('Valor errado, tente novamente. Digite um número entre 0 e 20: '))
print(f'O número digitado foi: {números[num - 1]}')
