from time import sleep
n1 = int(input("Qual é o primeiro número?"))
n2= int(input("Qual é o segundo número?"))
opcao = 0
while opcao != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
opcao = int(input('Qual é a sua opcão?'))
if opcao == 1:
     soma = n1 + n2
     print(f'A soma de {n1} + {n2} é igual a soma')
elif opcao == 2:
     multiplicacao = n1 + n2
     print(f'A multiplicação de {n1} e (n2) é igual a (multiplicacao)')
elif opcao == 3:
  if n1 > n2:
    print(f"0 (nl) é maior que {n2}")
  elif n2 > n1:
    print(f"o {n2} é maior que (n1)")
  else:
    print("Ambos os números são iguais")
elif opcao == 4:
   print('informe os números novamente')
   n1= int(input("Qual é o primeiro número?"))
   n2= int(input("Qual é o segundo número?"))
elif opcao == 5:
    print('Finalizando...')
else:
    print('opção inválida. Tente novamente')
sleep(2)
print('Acabou')
