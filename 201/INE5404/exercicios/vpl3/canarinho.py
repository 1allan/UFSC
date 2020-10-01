from ave import Ave


class Canarinho(Ave):
    def __init__(self, tamanhoPasso: int, alturaVoo: int):
        super().__init__(tamanhoPasso, alturaVoo)

    def cantar(self):
        return 'AVE: PRODUZ SOM: PIU'

    def mover(self):
        return super().mover()

    def produzirSom(self):
        return super().produzirSom()
