import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #arredonda pra cima 
print('a raiz de {} é igual a {}'.format(num, math.floor(raiz)))
