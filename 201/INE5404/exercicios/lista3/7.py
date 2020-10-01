class MeuDicionario:

    def __init__(self, chaves = None, itens = None):
        self.chaves = chaves if chaves is not None else []
        self.itens = itens if itens is not None else []
    
    def inserir(self, item):
        pass

    def remover(self, item):
        pass

    def __contains__(self, item):
        return self.chaves[self.itens.index(item)] if item in self.itens else False
    
    def __setitem__(self, chave, item):
        self.chaves.append(chave)
        self.itens.append(item)

    def __getitem__(self, chave):
        return self.itens[self.chaves.index(chave)]

    def __delitem__(self, chave):
        idx = self.chaves.index(chave)
        self.chaves.pop(idx)
        self.itens.pop(idx)

    def __str__(self):
        out = '{'
        for i, chave in enumerate(self.chaves):
            out +=  f'{chave}: {self.itens[i]},'
        return out[:-1] += '}'