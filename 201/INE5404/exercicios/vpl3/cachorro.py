from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self, volumeSom: int = 3, tamanhoPasso: int = 3):
        super().__init__(volumeSom, tamanhoPasso)

    def latir(self):
        return 'MAMIFERO: PRODUZ SOM: {} SOM: AU' .format(super().volumeSom)

    def mover(self):
        return super().mover()

    def produzirSom(self):
        return super().produzirSom()
