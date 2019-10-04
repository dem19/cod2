
class Programa:
    """Representa um programa genérico"""
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

class Serie(Programa):
    """Representa uma Série"""
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas

    def __str__(self):
        return ('Nome: {} - Temporadas {} - Likes {}').format\
        (self.nome,self.temporadas,self.likes)

got = Serie('Game of Thrones', 2011, 7)
got.dar_likes()
got.dar_likes()


play_list = [got]
for programa in play_list:
    print(str(programa))

