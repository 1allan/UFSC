from q2_caminhao_allansoares import Caminhao
from q2_carro_allansoares import Carro

menu = (
'''
a) Cadastrar novos veículos
b) Consultar informações
c) Calcular preço Carro
d) Calcular preço Caminhão
e) Sair
'''
)

veiculos = []
carros = 0
caminhoes = 0

while True:
    op = input(menu).lower()
    
    if op == 'a':
        while True:
            veiculo = input('Carro ou caminhão? ').lower()
            
            chassi = int(input('Número do chassi: '))
            placa = input('Número da placa: ')
            modelo = input('Modelo: ')
            marca = input('Marca: ')
            preco = float(input('Preço: '))

            if veiculo == 'carro':
                assentos = int(input('Número de assentos: '))
                tipo = input('Tipo: ')
                veiculos.append(Carro(chassi, placa, modelo, marca, preco, assentos, tipo))
                carros += 1
                
            elif veiculo == 'caminhao':
                eixos = int(input('Número de eixos: '))
                capacidade = float(input('Capacidade máxima de carga: '))
                veiculos.append(Caminhao(chassi, placa, modelo, marca, preco, eixos, capacidade))
                caminhoes += 1
                
            else:
                print('Tipo inválido')
            
            if input('Deseja continuar? (y/n) ').lower() == 'n':
                break
            
    if op == 'b':
        while True:
            chassi = int(input('Número do chassi: '))
            for v in veiculos:
                if v.chassi == chassi:
                    v.info()
            
            if input('Deseja continuar? (y/n)').lower() == 'n':
                break

    if op == 'c':
        while True:
            chassi = int(input('Número do chassi: '))
            for v in veiculos:
                if type(v) == Carro and v.chassi == chassi:
                    print(f'Preço final: {v.calcular_preco()}R$')
                    break
            
            if input('Deseja continuar? (y/n)').lower() == 'n':
                break
                    
    if op == 'd':
        while True:            
            chassi = int(input('Número do chassi: '))
            for v in veiculos:
                if type(v) == Caminhao and v.chassi == chassi:
                    print(f'Preço final: {v.calcular_preco()}R$')
                    break
                    
            if input('Deseja continuar? (y/n)').lower() == 'n':
                break
            
    if op == 'e':        
        print(f'Número total de veículos: {len(veiculos)}')
        print(f'Quantidade de carros: {carros}')
        print(f'Quantidade de caminhões: {caminhoes}')
        break