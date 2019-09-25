valor_produto = float(input('Valor do produto:'))
pagamento = input('Forma de pagamento: ')

if pagamento == '1':	
	print('À vista(-10%):', valor_produto * .9)
elif pagamento == '2':
	print('1x no cartão(-5%):', valor_produto * .95)
elif pagamento == '3':
	print('2x no cartão(preço normal):', valor_produto)
else:
	print('3x ou mais no cartão(-20%):', valor_produto * .8)