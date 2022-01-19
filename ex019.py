import random
aluno1 = (input("Qual o seu nome?"))
aluno2 = (input('E o nome daquele seu colega?'))
aluno3 = (input('Qual o nome da menina de franjinha?'))
aluno4 = (input('E o outro que fica no cantinho?'))
nomes = (aluno1, aluno2, aluno3, aluno4)
r = random.choice(nomes)
print('Certo, muito obrigado! Querido(a) aluno(a)..{}! Você foi o sorteado para\n... tan tan tan...\n limpar o quadro negro haha'.format(r))
