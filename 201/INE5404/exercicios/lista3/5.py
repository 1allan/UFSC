telefones = dict()

def incluir_novo_nome(nome):
    if nome not in telefones.keys():
        telefones[nome] = []
    else:
        print('Nome já cadastrado!')

def incluir_telefone(nome, telefone):
    telefones[nome].append(telefone)

def excluir_telefone(nome, telefone):
    if len(telefones[nome]) == 1:
        del telefones[nome]
    else:
        telefones[nome].remove(telefone)

def excluir_nome(nome):
    del telefones[nome]

def consultar_telefone(nome):
    return telefones[nome]

opcoes = (incluir_novo_nome, incluir_telefone, excluir_telefone, excluir_nome, consultar_telefone)

while True:
    print('Agenda\n1. Incluir novo nome\n2. Incluir telefone\n3. Excluir telefone\n4. Excluir nome\n5. Consultar telefone\n6. Sair')
    escolha = int(input('> '))
    if escolha == 6:
        break
    else:
        opcoes[escolha - 1]()
