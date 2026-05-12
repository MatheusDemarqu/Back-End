from random import randint
from time import sleep #faz ele esperar

aleatorio = randint(0, 5)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
jogador = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(3) #espera 3 segundos

if aleatorio == jogador:
    print("Parabéns! Você conseguiu")
else:
    print("Ganhei! Eu pensei no número {} e não no {}".format(aleatorio, jogador))
