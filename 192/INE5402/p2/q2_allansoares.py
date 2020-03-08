funcionario = []

while True:
    opt = input('''
    1) Cadastrar funcionários
    2) Calcular a idade em que um funcionário irá se aposentar
    3) Alterar dados do cadastro
    4) Consultar dados
    5) Sair do programa
    ''')
    
    if opt == '5':
        break
    
    elif opt == '1':
        while True:
            nome = input('Nome: ')
            nascimento = int(input('Ano de nascimento: '))
            cargo = input('Cargo: ')
            ano_contratacao = int(input('Ano da contratação: '))
            carteira_trabalho = int(input('Número da carteira de trabalho: '))
            
            funcionario.append({
                'nome': nome,
                'nascimento': nascimento,
                'cargo': cargo,
                'ano_contratacao': ano_contratacao,
                'carteira_trabalho': carteira_trabalho
            })
            
            if input('Desejas continuar?(Y/N)').upper() == 'N':
                break
    
    elif opt == '2':
        nome = input('Nome: ')
        for i in range(len(funcionario)):
            if funcionario[i]['nome'] == nome:
                print('Faltam {} anos para o {} se aposentar'.format(30 - (2019 - funcionario[i]['ano_contratacao']), funcionario[i]['nome']))
    
    elif opt == '3':
        nome = input('Nome: ')
        for i in range(len(funcionario)):
            if funcionario[i]['nome'] == nome:
                funcionario[i]['nome'] = input('Alterar nome: ')
                funcionario[i]['cargo'] = input('Alterar cargo: ')
                funcionario[i]['carteira_trabalho'] = input('Alterar carteira de trabalho: ')
    
    elif opt == '4':
        nome = input('Nome: ')
        for i in range(len(funcionario)):
            if funcionario[i]['nome'] == nome:
                print('Nome:', nome)
                print('Ano de nascimento:', funcionario[i]['nascimento'])
                print('Cargo:', funcionario[i]['cargo'])
                print('Ano de contratação:', funcionario[i]['ano_contratacao'])
                print('Número da carteira de trabalho:', funcionario[i]['carteira_trabalho'])
            