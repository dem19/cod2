
class Programa:
    """Representa um programa generico"""

    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1


class Filme(Programa):
    """Representa um filme"""
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao


class Serie(Programa):
    """Representa uma series"""

    def __init__(self,nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada

    @property
    def temporada(self):
        return self._temporada


#Filmes
#filme1 = Filme('Herry Potter', 2012, 120)
#filme1.dar_likes()
#filme1.dar_likes()
#filme1.dar_likes()
#filme1.likes

#Series
#serie1 = Serie('Vikings', 2014, 300)
#serie1.dar_likes()
#serie1.dar_likes()
#serie1.dar_likes()
#serie1.dar_likes()
#serie1.dar_likes()
#serie1.likes
