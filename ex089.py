alunos = list()
nota1 = nota2 = 0
cont = 0
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    média = (nota1 + nota2) /2
    alunos.append([nome, [nota1, nota2], média])
    resposta = str(input('Quer continuar [s/n]? '))
    cont += 1
    if resposta == 'n':
        break
print('-=' * 17)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for c in range(0, cont):
    print(f'{c:<4}{alunos[c][0]:<10}{alunos[c][2]:>8.1f}')
while True:
    pergunta = int(input('As notas de qual aluno você deseja saber? [999 interrompe]: '))
    if pergunta <= len(alunos) - 1:
        print(f'Notas de {alunos[pergunta][0]} são: {alunos[pergunta][1]}')
    elif pergunta == alunos[pergunta]:
        print(f'O aluno: {alunos[pergunta][0]}, tirou as notas: {alunos[pergunta][1]}')
    elif pergunta == 999:
        break