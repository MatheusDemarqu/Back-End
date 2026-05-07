from random import shuffle
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [alunol, aluno2, aluno3, aluno4]
shuffle(lista) #embaralha uma lista
print('a ordem de apresentação será {}'.format(lista))
