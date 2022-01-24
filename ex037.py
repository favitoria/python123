from time import sleep
num = int(input('Digite um valor qualquer: '))
bc = int(input('Escolha uma base de conversão, sendo: \n- 1 para binário \n- 2 para octal \n- 3 para hexadecimal\n RESPOSTA: '))
if bc == 1:
    c = bin(num)
    print('O NÚMERO {} CONVERTIDO PARA BINÁRIO FICA: {}!'.format(num, c[2::]))
elif bc == 2:
    c = oct(num)
    print('O NÚMERO {} CONVERTIDO PARA OCTAL FICA: {}!'.format(num, c[2::]))
elif bc == 3:
    c = hex(num)
    print('O NÚMERO {} CONVERTIDO PARA HEXADECIMAL FICA: {}!'.format(num, c[2::]))
else:
    print('OPÇÃO INVÁLIDA!')