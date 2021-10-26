class Gasolinera:

    def __init__(self, empresa, precio, localizacion, horario):
        self.empresa = empresa
        self.precio = precio
        self.localizacion = localizacion
        self.horario = horario

    def getPrecio(self):
        return self.precio

    def getLocalizacion(self):
        return self.localizacion

