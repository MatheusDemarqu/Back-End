from random import randint

cont = 0
while True:
    palpite = int(input('Diga um valor'))
    escolha = str(input('Par ou Ímpar?')).lower()
    pc = randint(1,10)
    resultado palpite + pc
    if resultado % 2 == 0 and escolha == 'par' or resultado % 2 != 0 and escolha == 'impar':
        print(f'Você jogou {palpite} e o computador jogou {pc} total deu {resultado} deu (escolha}')
        cont += 1
        print('Você VENCEU!')
    else:
        escolhapc = 'par' if resultado % 2 ==0 else 'impar'
        print(f'Você jogou {palpite} e o computador jogou {pc} total deu (resultado} deu {escolhapc}')
        break
    print('Vamos jogar novamente ...')
print(f'Game Over! Você venceu (cont) vezes')
