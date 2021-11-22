import requests
import json
import operator

from math import radians, cos, sin, asin, sqrt


class Localizacion:
    def __init__(self, direccion, cp, localidad, provincia, latitud, longitud):
        self.direccion = direccion
        self.cp = cp
        self.localidad = localidad
        self.provincia = provincia
        self._coordenadas = (
            str(latitud).replace(",", "."),
            str(longitud).replace(",", "."),
        )

    @property
    def coordenadas(self):
        return self._coordenadas

    def domicilio(self):
        return (
            self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia
        )

    def __str__(self):
        return (
            self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia
        )

    def haversine(self, dest):
        dlon = radians(float(dest[1]) - float(self.coordenadas[1]))
        dlat = radians(float(dest[0]) - float(self.coordenadas[0]))

        a = (
            sin(dlat / 2) ** 2
            + cos(float(dest[0])) * cos(float(self.coordenadas[0])) * sin(dlon / 2) ** 2
        )
        c = 2 * asin(sqrt(a))
        r = 6371

        return c * r

    def distanciasOrigen(self, gasolineras):
        distancias = []
        for es in gasolineras:
            destino = es.localizacion.coordenadas
            distancia = self.haversine(destino)
            distancias.append([distancia, es])

        distancias.sort(key=operator.itemgetter(0))
        return distancias

    def mejorEESS(self, distEESS):
        maxDistancia = distEESS[0][0] + 10
        finalistas = []
        for eess in distEESS:
            if eess[0] <= maxDistancia:
                finalistas.append(eess)
            else:
                break
        precios = []
        for elegido in finalistas:
            value = elegido[0] * elegido[1].precio
            precios.append([value, elegido])

        precios.sort(key=operator.itemgetter(0))
        return precios[0][1]
