import requests
import json
import operator

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from math import radians, cos, sin, asin, sqrt

import utils


class Localizacion:
    def __init__(self, direccion, cp, localidad, provincia, latitud=0.0, longitud=0.0):
        self.direccion = direccion
        self.cp = cp
        self.localidad = localidad
        self.provincia = provincia
        if latitud == 0.0 and longitud == 0.0:
            geolocalizador = Nominatim(user_agent="macime")
            location = geolocalizador.geocode(
                self.direccion
                + " "
                + self.cp
                + " "
                + self.localidad
                + " "
                + self.provincia
            )
            self._coordenadas = (location.latitude, location.longitude)
        else:
            self._coordenadas = (
                str(latitud).replace(",", "."),
                str(longitud).replace(",", "."),
            )
        self.logger = utils.log("macime")

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
            distancia = geodesic(self.coordenadas, destino).km
            distancias.append([distancia, es])

        self.logger.info(
            "Calculated all the distances in distancias (%s)", str(id(distancias))
        )
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
        self.logger.info(
            "Calculated gas stations that are nearer than 10km in finalistas (%s)",
            str(id(finalistas)),
        )
        precios = []
        for elegido in finalistas:
            value = elegido[0] * elegido[1].precio
            precios.append([value, elegido])

        self.logger.info("Calculated the best gas station")
        precios.sort(key=operator.itemgetter(0))
        return precios[0][1]
