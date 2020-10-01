from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str):
        s = False

        for i in self.__clientes:
            if i.codigo == codigo:
                s = True
                break

        if not s:
            cliente = Cliente(nome, codigo)
            self.__clientes.append(cliente)
            return cliente
        else:
            return

    def incluiTecnico(self, codigo: int, nome: str):
        s = False

        for i in self.__tecnicos:
            if i.codigo == codigo:
                s = True
                break

        if not s:
            tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(tecnico)
            return tecnico
        else:
            return
