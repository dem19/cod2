import math


class FiguraGeometrica:
    """Representa uma figura geometrica"""

    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor

    @property
    def nome(self):
        return self._nome

    @property
    def cor(self):
        return self._cor

    def calcula_area(self):
        print('Área da figura')

    def calcula_perimetro(self):
        print('Área da figura')


class Quadrado(FiguraGeometrica):
    """representa um quadrado"""

    def __init__(self, nome, cor, lado):
        super().__init__(nome, cor)
        self._lado = lado

    @property
    def lado(self):
        return self._lado

    def calcula_area(self):
        return self._lado ** 2

    def calcula_perimetro(self):
        return self._lado * 4


class Retangulo(FiguraGeometrica):
    """Representa um retângulo"""

    def __init__(self, nome, cor, base, altura):
        super().__init__(nome, cor)
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    def calcula_area(self):
        return self._base * self._altura

    def calcula_perimetro(self):
        return self._base * 2 + self._altura * 2


class Circulo(FiguraGeometrica):
    """Representa um circulo"""

    def __init__(self, nome, cor, raio):
        super().__init__(nome, cor)
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    def calcula_area(self):
        return math.pi * self._raio ** 2

    def calcula_perimetro(self):
        return 2 * math.pi * self._raio


quadrado = Quadrado('Quadrado', 'azul', 2)
print(quadrado.calcula_area())

retangulo = Retangulo('Retangulo', 'preto', 12, 7)
print(retangulo.calcula_area())

circulo = Circulo('Roda', 'braca', 6)
print(circulo.calcula_area())
