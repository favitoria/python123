'''produtos = ('Quadros Anime', 50.40, 'Broche Anime', 2.50, 'Camiseta Anime', 30.20, 'Caneca Anime', 15.30, 'Colares Anime', 10.00, 'Brincos Anime', 7.60, 'Anéis Anime', 6.80, 'Bonecos Anime', 70.70, 'Moletom Anime', 65.50, 'Chaveiro Anime', 12.20)
print('==--====--== LOJINHA DO RORONOA ZORO ==--====--==')
print('--------------------Valores------------------------')
print(f'{produtos[0]}..........................R$ {produtos[1]:>8.2f}')
print(f'{produtos[2]}...........................R$ {produtos[3]:>8.2f}')
print(f'{produtos[4]}.........................R$ {produtos[5]:>8.2f}')
print(f'{produtos[6]}...........................R$ {produtos[7]:>8.2f}')
print(f'{produtos[8]}..........................R$ {produtos[9]:>8.2f}')
print(f'{produtos[10]}..........................R$ {produtos[11]:>8.2f}')
print(f'{produtos[12]}............................R$ {produtos[13]:>8.2f}')
print(f'{produtos[14]}..........................R$ {produtos[15]:>8.2f}')
print(f'{produtos[16]}..........................R$ {produtos[17]:>8.2f}')
print(f'{produtos[18]}.........................R$ {produtos[19]:>8.2f}')
print('---------------------------------------------------')'''
produtos = ('Quadros Anime', 50.40, 'Broche Anime', 2.50,
            'Camiseta Anime', 30.20, 'Caneca Anime', 15.30,
            'Colares Anime', 10.00, 'Brincos Anime', 7.60, 'Anéis Anime', 6.80,
            'Bonecos Anime', 70.70, 'Moletom Anime', 65.50,
            'Chaveiro Anime', 12.20)
print('==--====--== LOJINHA DO RORONOA ZORO ==--====--==')
print('--------------------Valores------------------------')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('---------------------------------------------------')


