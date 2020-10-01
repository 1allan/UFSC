from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self, volumeSom: int = 2, tamanhoPasso: int = 2):
        super().__init__(volumeSom, tamanhoPasso)

    def miar(self):
        return 'MAMIFERO: PRODUZ SOM: {} SOM: MIAU' .format(super().volumeSom)

    def mover(self):
        return super().mover()

    def produzirSom(self):
        return super().produzirSom()
