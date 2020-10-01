from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipoChamados = []

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        s = False

        for c in self.__chamados:
            if c.data == data and c.cliente == cliente and c.tecnico == tecnico and c.tipo == tipo:
                s = True
                break

        if not s:
            chamado = Chamado(data, cliente, tecnico, titulo,
                                descricao, prioridade, tipo)
            self.__chamados.append(chamado)
            return chamado
        else:
            return

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str):
        s = False

        for i in self.__tipoChamados:
            if i.codigo == codigo:
                s = True
                break

        if not s:
            tipoChamado = TipoChamado(codigo, descricao, nome)
            self.__tipoChamados.append(tipoChamado)
            return tipoChamado
        else:
            return

    @property
    def tipoChamados(self):
        return self.__tipoChamados

    def totalChamadosPorTipo(self, tipo: TipoChamado):
        total = 0

        for i in self.__chamados:
            if i.tipo == tipo:
                total += 1

        return total
