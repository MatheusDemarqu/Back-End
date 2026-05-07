#Exercício Python 025: Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.

nome = str(input(" Digite qual é o seu nome?")).strip()
print('seu nome tem silva? {}'.format('silva' in nome.lower()))
