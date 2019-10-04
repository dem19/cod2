#um cliente poderá criar um carrinho de compras com vários itens de compra. Pense de forma simplificada. Neste sentido,
#o fluxo principal do sistema é o cliente inserir vários produtos em seu carrinho e poder ver o valor final da compra. Para persistência dos dados utilize o SQlite.


class Produtos:
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = preco

    def descricao(self):
        return self._descricao

    def preco(self):
        return self._preco

class Carrinho:
    def __init__(self, itens):
        self._itens = itens
        self._quant = 0

    def itens(self):
        return self._itens

    def quantidade(self):
        return self._quant

    def __getitem__(self, item):
        return self._itens[item]

    def __len__(self):
        return len(self._itens)


    def total(self):
        for item in self._itens:
            self._quant += item.preco
        return self._quant


leite = Produtos('leite', 5.3)
cafe = Produtos('Cafe', 11.4)

car = Carrinho([leite,cafe])
#car = [leite, cafe]


for item in car:
    print(str(item))

print(Carrinho.total)





