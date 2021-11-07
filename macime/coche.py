class Coche:

    def __init__(self, consumo, deposito, actual):
        self.consumo = consumo
        self.deposito = deposito
        self.actual = actual

    def getConsumo(self):
        return self.consumo

    def getDeposito(self):
        return self.deposito

    def __str__(self):
        return "El coche tiene un consumo de " + self.consumo + " con un deposito de " + self.deposito 
