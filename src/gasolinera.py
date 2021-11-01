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

    def __str__(self):
        return "La gasolinera " + self.empresa + " con precio " + str(self.precio) + " localizada en " + str(self.localizacion)

