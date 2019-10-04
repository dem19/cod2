
class Produto:
    def __init__(self, codproduto, descricao, preco):
        self._codproduto = codproduto
        self._descricao = descricao
        self._preco = preco

    @property
    def codproduto(self):
        return self._codproduto
    @property
    def descricao(self):
            return self._descricao
    @property
    def preco(self):
        return self._preco


class Carrinho():
    '''Representa um carrinho de compras'''
    def __init__(self,itens,quantidade):
        self._itens = itens
        self._total = 0
        self._quantidade = quantidade

    def __getitem__(self, item):
        return self._itens[item]

    def __len__(self):
        return len(self._itens)

    def __str__(self):
        return ('Nome: {} - Temporadas {} - Likes {}').format\
        (self.nome,self.temporadas,self.likes)

    @property
    def valor(self):
        for item in self._itens:
            self._total += item.preco * item.quantidade
        return self._total




produto1 = Produto(2, 'arroz', 3)
p1 = Carrinho(produto1,2)
#produto2 = Produto(1, 'feijão', 4)
#produto3 = Produto(3, 'macarrão', 4.5)

carrinho = [p1]
for item in carrinho:
    print(item)
#    print("{} - {}".format(item.itens,item.quantidade))
#    print("Codproduto:{}  - Descrição:{}  -  Preço:{} - quantidade: {}  ".format(item.codproduto, item.descricao, item.preco, item.quantidade))
#print("Valor Total: {}".format(carrinho.valor))




