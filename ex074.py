from random import randint
a = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(a, end=' ')
print(f'\nO maior valor é: {max(a)}')
print(f'O menor valor é: {min(a)}')

