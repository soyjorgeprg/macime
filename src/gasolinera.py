import requests
import json

from localizacion import Localizacion


class Gasolinera:

    def __init__(self, empresa="", precio=0, localizacion="", horario=""):
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

    def obtenerGasolineras(self, code):
        '''
            Los codigos que pueden enviarles son muy variados aunque los que nos interesan a nosotros son el 17 (GLP) y el 18 (GNC).
        '''
        url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroProducto/" + code
        
        respuesta = requests.get(url).json()

        gasolineras = []

        for x in respuesta['ListaEESSPrecio']:
            localizacion = Localizacion(x['Dirección'], x['C.P.'], x['Localidad'], x['Provincia'], x['Latitud'], x['Longitud (WGS84)'])
            gasolineras.append(Gasolinera(x['Rótulo'], x['PrecioProducto'], localizacion, x['Horario']))

        return gasolineras

    def guardarGasolineras(self, code):
        url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroProducto/" + code
        respuesta = requests.get(url).json()

        path = ""
        if code == "17":
            path = "src/data/glp.json"
        elif code == "18":
            path = "src/data/gnc.json"
        else:
            path = "src/data/eess.json"

        with open(path, 'w') as eess:
            json.dump(respuesta, eess)

        return 0

    def leerGasolineras(self, tipo):
        fichero = "src/data/" + tipo.lower() + '.json'

        with open(fichero, 'r') as f:
            respuesta = json.load(f)

        gasolineras = []
        for x in respuesta['ListaEESSPrecio']:
            localizacion = Localizacion(x['Dirección'], x['C.P.'], x['Localidad'], x['Provincia'], x['Latitud'], x['Longitud (WGS84)'])
            gasolineras.append(Gasolinera(x['Rótulo'], x['PrecioProducto'], localizacion, x['Horario']))

        return gasolineras
