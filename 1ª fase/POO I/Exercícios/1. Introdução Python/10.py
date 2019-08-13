valor_compra = float(input('Valor da compra: '))

if valor_compra >= 5000:
	print('Valor da compra: R$', valor_compra)
	print('Desconto: 20%')
	print('Valor final: R$', valor_compra * .8)
else:
	print('Valor da compra: R$', valor_compra)
	print('Desconto: 15%')
	print('Valor final: R$', valor_compra * .85)
