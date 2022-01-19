d = float(input('Quantos dias alugados?'))
km = float(input('E quantos km rodados?'))
t = d * 60 + km * 0.15
print('O total a se pagar é de R${:.2f}'.format(t))