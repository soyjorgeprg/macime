import requests
import json

from localizacion import Localizacion


class Gasolinera:
    def __init__(self, localizacion, empresa="", precio=0, horario=""):
        self.empresa = empresa
        self._precio = precio
        self._localizacion = localizacion
        self.horario = horario

    @property
    def precio(self):
        return self._precio

    @property
    def localizacion(self):
        return self._localizacion

    def __str__(self):
        return (
            "La gasolinera "
            + self.empresa
            + " con precio "
            + str(self._precio)
            + " localizada en "
            + str(self._localizacion)
        )

    def obtenerGasolineras(self, code):
        url = (
            "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroProducto/"
            + code
        )
        respuesta = requests.get(url).json()

        path = ""
        if code == "17":
            path = "macime/data/glp.json"
        elif code == "18":
            path = "macime/data/gnc.json"
        else:
            path = "macime/data/eess.json"

        with open(path, "w") as eess:
            json.dump(respuesta, eess)

        return 0

    def leerGasolineras(self, tipo):
        fichero = "macime/data/" + tipo.lower() + ".json"

        with open(fichero, "r") as f:
            respuesta = json.load(f)

        gasolineras = []
        for x in respuesta["ListaEESSPrecio"]:
            localizacion = Localizacion(
                x["Dirección"],
                x["C.P."],
                x["Localidad"],
                x["Provincia"],
                x["Latitud"],
                x["Longitud (WGS84)"],
            )
            gasolineras.append(
                Gasolinera(localizacion, x["Rótulo"], x["PrecioProducto"], x["Horario"])
            )

        return gasolineras
