class Localizacion:

    def __init__(self, direccion, cp, localidad, provincia):
        self.direccion = direccion
        self.cp = cp
        self.localidad = localidad
        self.provincia = provincia

    def getProvincia(self):
        return self.provincia

    def getLocalizacion(self):
        return (self.direccion + self.cp + self.localidad + self.provincia)


