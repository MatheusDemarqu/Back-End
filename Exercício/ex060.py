n = int(input('Quantos termos você quer mostrar?'))
t1 = 0 #primeiro termo da sequência fibonacci
t2 = 1 #segundo termo da sequência fibonacci
print(f'{t1}->{t2}', end='')
cont = 3#ja mostrei os 2 primeiros
while cont <= n:
   t3 = t1 + t2
   print(f'-> {t3}', end='')
   t1 = t2# para fazer a sequência andar
   t2 = t3
   cont += 1
print(' -> FIM')
