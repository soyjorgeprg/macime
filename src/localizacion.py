class Localizacion:

    def __init__(self, direccion, cp, localidad, provincia, latitud, longitud):
        self.direccion = direccion
        self.cp = cp
        self.localidad = localidad
        self.provincia = provincia
        self.latitud = latitud
        self.longitud = longitud

    def getProvincia(self):
        return self.provincia

    def getLocalizacion(self):
        return (self.direccion + self.cp + self.localidad + self.provincia)

    def getLocalizacionPrecisa(self):
        return (self.latitud, self.longitud)

    def __str__(self):
        #return (self.latitud + "," + self.longitud)
        return (self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia)
