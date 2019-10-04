
class Veiculo:
    def __init__(self, marca, ano, peso, autonomia, custo_mant_km, valor_hora_locacao, placa,hodometro):
        self._marca = marca
        self._ano = ano
        self._peso = peso
        self._autonomia = autonomia
        self._custo_mant_km = custo_mant_km
        self._hodometro = hodometro
        self._valor_hora_locacao = valor_hora_locacao
        self._placa = placa

    @property
    def Marca(self):
        return self._marca
    def Ano(self):
        return self._ano
    def Peso(self):
        return self._peso
    def Autonomia(self):
        return self._autonomia
    def Custo_manutencao(self):
        return self._custo_mant_km
    def Hodometro(self):
        return self._hodometro
    def Valor_locacao(self):
        return self._valor_hora_locacao
    def Placa(self):
        return self._placa

    def Valor_locacao(self):
        print("Valor da Locação")
    def Custo_locacao(self):
        print("Custo da Locação")
    def Atualiozar_hodometro(self):
        print("Atualizar o Hodometro")

class Motos(Veiculo):
    def __init__(self,  marca, ano, peso, autonomia, custo_mant_km, hodometro, valor_hora_locacao, placa):
        super().__init__( marca, ano, peso, autonomia, custo_mant_km, hodometro, valor_hora_locacao, placa)




    def Valor_locacao(self):
        return self._valor_hora_locacao

    def Custo_locacao(self):
        return self._hodometro * self._custo_mant_km

    def Atualiozar_hodometro(self):
        if self._hodometro > 0:
            return self._hodometro == 0



class Carro(Veiculo):
    def __init__(self, marca, ano, peso, autonomia, custo_mant_km, hodometro, valor_hora_locacao, placa):
        super().__init__(marca, ano, peso, autonomia, custo_mant_km, hodometro, valor_hora_locacao, placa)

    def Valor_locacao(self):
        pass

    def Custo_locacao(self):
        pass

    def Atualiozar_hodometro(self):
        pass

class Caminhoes(Veiculo):
    def __init__(self, marca, ano, peso, autonomia, custo_mant_km, hodometro, valor_hora_locacao, placa):
        super().__init__(marca, ano, peso, autonomia, custo_mant_km, hodometro, valor_hora_locacao, placa)

    def Valor_locacao(self):
        pass

    def Custo_locacao(self):
        pass

    def Atualiozar_hodometro(self):
        pass




# fam=Motos('honda',2018,500,0,200,20,5,2737)




