MESES = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')

temperaturas = [float(input()) for _ in range(12)]
media = sum(temperaturas) / len(temperaturas)

for i, t in enmuerate(temperaturas):
    if t > media:
        print(f'{t}ºC - {MESES[i]}')