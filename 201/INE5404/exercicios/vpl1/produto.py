class Produto:

    def __init__(self, codigo, descricao, categoria):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__quantidade = 0
        self.__preco_unitario = 0
        self.__cliente = None
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        self.__quantidade = valor
    
    @property
    def preco_unitario(self):
        return self.____preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, valor):
        self.____preco_unitario = valor
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor
    
    def preco_total(self):
        return self.preco_unitario * self.quantidade
        