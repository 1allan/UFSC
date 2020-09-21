class MinhaLista:

    def __init__(self, valores=tuple()):
        self.valores = valores
    
    def append(self, valor):
        self.valores += tuple(valor)
    
    def remove(self, valor):
        lista = list(self.valores)
        lista.remove(valor)
        self.valores = tuple(lista)
    
    def pop(self, index=-1):
        lista = list(self.valores)
        removido = lista.pop(index=index)
        self.valores = tuple(lista)
        return removido
        
    def sort(self):
        lista = list(self.valores)
        lista.sort()
        self.valores = tuple(lista)