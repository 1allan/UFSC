from random import randint
from getpass import getpass

def extrato(function):
    def wrapper(self_, valor):
        self_.historico.append({'operacao': function.__name__, 'valor': valor})
        function(self_, valor)
    return wrapper

class Cliente:

    def __init__(self, nome: str, telefone: int):
        self.nome = nome
        self.telefone = telefone
        self.contas = []


class ContaCorrente:
    
    def __init__(self, senha: str):
        self.numero = randint(0, 9999)
        self.dv = randint(0, 9)
        self.senha = senha
        self.saldo = 0.0
        self.historico = []

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, valor: int):
        if self.saldo + valor < 0:
            print('Saldo insuficiente')
        else:
            self.saldo += valor

    @saldo.getter
    def saldo(self):
        return self.saldo
    

class ContaEspecial(ContaCorrente):
    
    def __init__(self, senha, limite: int = 200):
        super().__init__(senha)
        self.limite = limite
    
    @ContaCorrente.saldo.setter
    def saldo(self, valor: int):
        if self.saldo + valor < -self.limite:
            print('Saldo insuficiente')
        else:
            self.saldo += valor

class Tatu:

    def __init__(self):
        self.clientes = []
        self.contas = []
        self.logados = []

    def menu(self):
        print('Bem vindo ao banco Tatu')
        cliente = None
        while True:
            if input('Já possui cadastro? (y/n)\n> ').lower() == 'y':
                nome = input('Nome: ')
                telefone = int(input('Telefone: '))
                
                for c in self.clientes:
                    if c.nome == nome or c.telefone == telefone:
                        cliente = c
                        break
                
                if cliente is None:
                    print('Conta não encotrada')
            else:
                self.clientes.append(Cliente(
                    input('Nome: '), 
                    int(input('Telefone: '))
                ))
                break
       
        while True:
            funcoes = (
                {'text': '1. Sacar', 'exec': self.saque},
                {'text': '2. Depositar', 'exec': self.deposito},
                {'text': '3. Extrato', 'exec': self.extrato},
                {'text': '4. Sair', 'exec': exit}
            )

            for f in funcoes:
                print(f.text)
            
            opt = int(input('> '))
            
            if opt == 4:
                exit()
            else:
                conta_num = input('Número da conta: ')
                conta_sen = getpass('Senha da conta: ')
                conta = None
                for c in self.contas:
                    if c.numero == conta_num and c.senha == conta_sen:
                        conta = c
                
                if conta is None:
                    print('Conta não encontrada')
                else:
                    funcoes[opt + 1](conta)
    @extrato
    def saque(self, conta):
        valor = int(input('Valor do saque R$ '))
        conta.saldo -= valor

    @extrato
    def deposito(self, conta):
        valor = int(input('Valor do deposito R$ '))
        conta.saldo += valor

    def retirar_extrato(self, conta):
        pass          

    def nova_conta(self):
        if input('Tipo de conta (corrente/especial)').lower() == 'corrente':
            senha = input('Senha da conta: ')
            c = ContaCorrente(senha)
            self.contas(c)
            print('Nova conta criada!')
            print('Número:', c.numero)
        
        else:
            senha = input('Senha da conta: ')
            limite = int(input('Limite: '))
            c = ContaEspecial(senha, limite)
            self.contas(c)
            print('Nova conta criada!')
            print('Número:', c.numero)