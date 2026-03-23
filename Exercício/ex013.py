preco = float(input('Qual é o preço do produto? R$'))
desconto = preco - (preco * 5/ 100)
print('o produto que custava{:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))
