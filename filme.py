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

class Filme(Programa):
    """Representa um Filme"""
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def __str__(self):
        return ('Nome: {} - Temporadas {} - Likes {}').format \
        (self.nome, self.duracao, self.likes)

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
# Filmes
mib2 = Filme('Mib 2', 2012, 120)
#mib2.dar_liar_likes()
#mib2.lkes()
#mib2.dikes
titanic = Filme('Titanic', 2000, 180)
#titanic.dar_likes()
#titanic.dar_likes()
#titanic.dar_likes()
#titanic.dar_likes()
## Séries
vikings = Serie('Vikings', 2014, 5)
#vikings.dar_likes()
#vikings.likes
got = Serie('Game of Thrones', 2011, 7)
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()

play_list = [mib2, vikings, titanic, got]
for programa in play_list:
    print(str(programa))
