class Livro:

    def __init__(self, titulo, editora, ano, volume, autores = None):
        self.titulo = titulo
        self.editora = editora
        self.ano = ano
        self.volume = volume
        self.autores = [] if autores is None else autores


class Biblioteca:

    def __init__(self, livros = None):
        self.livros = [] if livros is None else livros

    def consultar(self):
        pass