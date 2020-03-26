"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

from random import randint

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        ...
        self.arr = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        ...
        
        i = 0
        sorted_ = []
        lowest = self.arr[0]
        while len(self.arr) > 0:
            if self.arr[i] < lowest:
                lowest = self.arr[i]
            i += 1
            
            if i == len(self.arr):
                sorted_.append(lowest)
                self.arr.remove(lowest)
            
                if self.arr:
                    lowest = self.arr[0]
                    i = 0

        self.arr = sorted_

        return sorted_

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """
        ...
        
        return ','.join([str(x) for x in self.arr])
        
if __name__ == '__main__':
    a = Ordenacao([randint(-50, 100) for _ in range(randint(5, 10))])
    print(a.arr)
    print(a.toString())
    print(a.ordena())
    print(a.toString())