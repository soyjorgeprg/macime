import requests
import json
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


class Localizacion:

    def __init__(self, direccion, cp, localidad, provincia, latitud=0.0, longitud=0.0):
        self.direccion = direccion
        self.cp = cp
        self.localidad = localidad
        self.provincia = provincia

        if latitud == 0.0 and longitud == 0.0:
            geolocalizador = Nominatim(user_agent="macime")
            location = geolocalizador.geocode(self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia)
            self._coordenadas = (location.latitude, location.longitude)
        else:
            self._coordenadas = (str(latitud).replace(',', '.'), str(longitud).replace(',', '.'))

    @property
    def coordenadas(self):
        return self._coordenadas

    def domicilio(self):
        return self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia

    def __str__(self):
        return self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia


    def distanciaMinima(self, gasolineras):
        origen = self.coordenadas

        distancias = []
        for es in gasolineras:
            destino = es.localizacion.coordenadas
            distancia = geodesic(origen, destino).km
            distancias.append(distancia)

        min_value = min(distancias)
        min_index = distancias.index(min_value)
        return min_index
