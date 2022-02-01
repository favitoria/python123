maior = 0
menor = 0
for p in range(1,6):
     peso = float(input('Digite um peso: '))
     if p == 1:
          maior = peso
          menor = peso
     else:
          if peso > maior:
               maior = peso
          if peso < menor:
               menor = peso
print('O maior peso é de {}Kg e o menor é de {}kg'.format(maior, menor))


'''peso = []
for c in range(5):
     peso.append(float(input('Digite um peso: ')))
print('O maior peso informado é {}, o menor peso informado é {}'.format(max(peso), min(peso)))'''
