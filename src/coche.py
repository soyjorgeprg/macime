class Coche:

    def __init__(self, consumo, deposito, actual):
        self.consumo = consumo
        self.deposito = deposito
        self.actual = actual

    def getConsumo(self):
        return self.consumo

    def getDeposito(self):
        return self.deposito

