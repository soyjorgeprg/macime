import requests
import json

from math import radians, cos, sin, asin, sqrt


class Localizacion:

    def __init__(self, direccion, cp, localidad, provincia, latitud, longitud):
        self.direccion = direccion
        self.cp = cp
        self.localidad = localidad
        self.provincia = provincia
        self._coordenadas = (str(latitud).replace(',', '.'), str(longitud).replace(',', '.'))

    @property
    def coordenadas(self):
        return self._coordenadas

    def domicilio(self):
        return self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia

    def __str__(self):
        return self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia

    def haversine(self, dest):
        dlon = radians(float(dest[1]) - float(self.coordenadas[1]))
        dlat = radians(float(dest[0]) - float(self.coordenadas[0]))

        a = sin(dlat/2)**2 + cos(float(dest[0])) * cos(float(self.coordenadas[0])) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371

        return c * r


    def distanciaMinima(self, gasolineras):
        distancias = []
        for es in gasolineras:
            destino = es.localizacion.coordenadas
            distancia = self.haversine(destino)
            distancias.append(distancia)

        min_value = min(distancias)
        min_index = distancias.index(min_value)
        return min_index
