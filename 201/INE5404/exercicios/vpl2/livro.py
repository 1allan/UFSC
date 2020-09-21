from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:

    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.editora = editora
        self.autores = [autor]
        self.capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano


    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.autores:
            self.autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if isinstance(autor, Autor) and autor in self.autores:
            self.autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        if tituloCapitulo not in [c.titulo for c in self.capitulos]:
            self.capitulos.append(Capitulo(numeroCapitulo, tituloCapitulo))

    def excluirCapitulo(self, tituloCapitulo: str):
        for c in self.capitulos:
            if c.titulo == tituloCapitulo:
                self.capitulos.remove(c)
                
    def findCapituloByTitulo(self, tituloCapitulo: str):
        self.tituloCapitulo = None