import random
alum = input('Qual o nome do seu projeto?')
aldois = input('Qual o nome do projeto de sua amiga?')
altres = input ('E o do seu colega que senta atrás de você?')
alquatro = input('Certo... e o da sua colega que senta na frente?')
alunos = [alum, aldois, altres, alquatro]
r = random.shuffle(alunos)
print('A ordem de apresentação será:')
print(alunos)
