valores = []
mai = 0
mini = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = mini = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < mini:
            mini = valores[c]
print(f'O maior valor foi {max(valores)} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == mai:
        print(f'{c}...', end='')
print(f'\nO menor valor foi {min(valores)} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == mini:
        print(f'{c}...', end='')