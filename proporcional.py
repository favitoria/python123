VAN = float(input('VALOR ANTIGO: '))
VNV = float(input('VALOR NOVO: '))
DIASVELHO = int(input('DIAS PLANO NOVO: '))
DIASNOVO = int(input('DIAS PLANO VELHO: '))
PORDIAVELHO = (VAN / 30) * DIASVELHO
PORDIANOVO = (VNV / 30) * DIASNOVO
TOTAL = PORDIANOVO + PORDIAVELHO
print(f'O proporcional é: R${TOTAL:.2f}\nSendo R${PORDIAVELHO:.2f} do plano velho '
      f'e R${PORDIANOVO:.2f} do plano novo')
