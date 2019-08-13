preco_produto = float(input('Preço do produto:'))
valor_pago = float(input('Valor pago: '))

if preco_produto == valor_pago:
	print('Tudo certo')
elif preco_produto < valor_pago:
	print('Troco: R$', valor_pago - preco_produto)
else:
	print('Faltam R$', preco_produto - valor_pago)