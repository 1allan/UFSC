 '''
	1) Crie a classe Televisao com os atributos ​ligada ​(inicializado com valor 
	False)​ e ​canal(inicializado com valor  2).
 '''
 class Televisao:
	def __init__(self):
	    self.ligada = False
	    self.canal = 2


 '''
	2) Adicione os atributos tamanho e marca à classe Televisao. Crie dois 
	objetos Televisao e atribua tamanhos e marcas diferentes. Depois, imprima o 
	'valor desses atributos de forma a confirmar independência dos valores de 
	cada instância (objeto).
 '''
 class Televisao:
	def __init__(self, tamanho, marca):
	self.ligada = False
	    self.canal = 2
	    self.tamanho = tamanho
	    self.marca = marca

 a = Televisao(40, 'sei lá')
 b = Televisao(50, 'não sei')

 print(a.tamanho, a.marca)
 print(b.tamanho, b.marca)

 '''
	3) Adicione dois novos métodos muda_canal_para_cima e 
	muda_canal_para_baixo. Atualmente, a classe Televisao inicializa o canal 
	com 2. Modifique a classe televisao deforma a receber o canal inicial em 
	seu construtor.
 '''
 class Televisao:
	def __init__(self, canal, tamanho, marca):
	    self.ligada = False
	    self.canal = canal
	    self.tamanho = tamanho
	    self.marca = marca

	def mudar_canal_para_cima(self):
	    pass

	def mudar_canal_para_baixo(self):
	    pass

 '''
	4) Adicione mais dois atributos canal_minimo (valor padrão 1) e ​
	canal_maximo​ (valor padrão 99) e modifique a classe Televisao de forma que,
	se pedirmos para mudar o canal para baixo, além do mínimo, ela vá para o 
	canal máximo. Se mudarmos para cima, além do canal máximo, que volte ao 
	canal mínimo.
 '''
 class Televisao:
	def __init__(self, canal, tamanho, marca):
	    self.ligada = False
	    self.canal = canal
	    self.tamanho = tamanho
	    self.marca = marca
	    self.canal_minimo = 1
	    self.canal_maximo = 99

	def mudar_canal_para_cima(self):
		self.canal += 1
		if self.canal > self.canal_maximo:
			self.canal = self.canal_minimo
	
	def mudar_canal_para_baixo(self):
		self.canal -= 1
		if self.canal < self.canal_minimo:
			self.canal = self.canal_maximo

 '''
	5) Modifique o construtor da classe Televisao de forma que canal_minimo e 
	canal_maximo seja parametros opcionais valendo respectivamente 2 e 14.
 '''
 class Televisao:
	def __init__(self, canal, tamanho, marca, canal_minimo=2, canal_maximo=14):
	    self.ligada = False
	    self.canal = canal
	    self.tamanho = tamanho
	    self.marca = marca
	    self.canal_minimo = canal_minimo
	    self.canal_maximo = canal_maximo

	def mudar_canal_para_cima(self):
		self.canal += 1
		if self.canal > self.canal_maximo:
			self.canal = self.canal_minimo
	
	def mudar_canal_para_baixo(self):
		self.canal -= 1
		if self.canal < self.canal_minimo:
			self.canal = self.canal_maximo

 '''
	6) Crie duas instancias de Televisao, especificando o valor de canal_minimo e canal_maximo 
	​por nome.
 '''
 class Televisao:
	def __init__(self, canal, tamanho, marca, canal_minimo=2, canal_maximo=14):
	    self.ligada = False
	    self.canal = canal
	    self.tamanho = tamanho
	    self.marca = marca
	    self.canal_minimo = canal_minimo
	    self.canal_maximo = canal_maximo

	def mudar_canal_para_cima(self):
		self.canal += 1
		if self.canal > self.canal_maximo:
			self.canal = self.canal_minimo
	
	def mudar_canal_para_baixo(self):
		self.canal -= 1
		if self.canal < self.canal_minimo:
			self.canal = self.canal_maximo

 tv_1 = Televisao(5, 50, 'A', canal_minimo=2, canal_maximo=98)
 tv_2 = Televisao(10, 55, 'B', canal_minimo=1,  canal_maximo=99)

 '''
	7) Crie classes para representar estados e cidades. Cada estado tem um 
	nome, sigla e cidades. Cada cidade tem nome e população. Escreva um 
	programa de testes que crie três estados com algumas cidades em cada um.
	Exiba a população de cada estado como a soma da população de suas cidades.
 '''
from random import randint, sample
abc = 'abcdefghijklmnopqrstuvwxyz'

class Estado:
    def __init__(self, nome, sigla, cidades):
		self.nome = nome
		self.sigla = sigla
		self.cidades = cidades
		self.populacao = sum([c.populacao for c in self.cidades])


class Cidade:
    def __init__(self, nome, populacao):
		self.nome = nome
		self.populacao = populacao


random_name = lambda: ''.join(sample(abc, randint(3, 15))).capitalize() 

cidades = [Cidade(random_name(), randint(0, 10**6)) for _ in range(30)]
estados = [Estado(
	random_name(),
	''.join(sample(abc, 2)).upper(),
	cidades[(i * 15):((i + 1) * 15)]) for i in range(2)
]

for e in estados:
    print('Estado:', e.nome)
    print('População:', e.populacao)

'''
    8) Escreva uma classe Coordenada com atributos x e y, e métodos para 
	mostrar as coordenadas, calcular a distancia para outra coordenada, 
	comparar coordenadas, mostrar no formato coordenada polar.
'''
class Coordenada:
    def __init__(self, x, y):
		self.x = x
		self.y = y
		
    def mostrar_coordenadas(self):
			return self.x, self.y
		
    def distancia(self, c2):
		return ((c2.x - self.x) ** 2 + (c.y - self.y)) ** 0.5
		
'''
    9) Escreva classes para as seguintes formas: quadrado, retângulo e círculo.
'''
class Retangulo:
    def __init__(self, largura, altura):
		self.largura = largura
		self.altura = altura

	def area(self):
		return self.largura * self.altura


class Quadrado(Retangulo):
    def __init__(self, tamanho):
		super().__init__(tamanho, tamanho)


class Circulo:
    def __init__(self, raio):
		self.raio = raio
	
	def area(self):
		return 3.141592653589793 * self.raio ** 2

'''
    10) Escreva uma classe Fracao que armazena dois inteiros, numerador e 
	denominador.
	   a) Implemente metodos para somas, subtração, multiplicação e divisão de 
	   duas frações;
	   b) Implemente o método que imprime uma fração no formato 
	   numerador/denominador;
	   c) Implemente um método que inverte a fração;
	   d) Implemente um método que retorna a fração em valor real;
	   e) Implemente um método que cria uma fração (numerador/denominador) a 
	   partir de um número real.
'''
class Fracao:
    def __init__(self, numerador, denominador):
		self.numerador = numerador
		self.denominador = denominador
		self.valor = numerador/denominador

    def soma(self, b):
		denominador_comum = self.denominador * b.denominador
		return f'{
			denominador_comum / self.denominador * self.numerador +
			denominador_comum / b.denominador * b.numerador
			}/{denominador_comum}'
	
	def subtracao(self, b):
		b.numerador *= -1
		return self.soma(b)
	
	def multiplicacao(self, b):
		return f'{self.numerador * b.numerador}/{
			self.denominador * b.denominador
			}'
	
	def divisao(self, b):
		return f'{self.numerador * b.denominador}/{
			self.denominador * b.numerador
			}'
    
    def imprime(self):
		print(f'{self.numerador}/{self.denominador}')
		
    def inverte(self):
		self.numerador, self.denominador = self.denominador, self.numerador
		
    def get_valor(self):
	   	return self.valor
    