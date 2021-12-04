import json

import utils
from localizacion import Localizacion

class Gasolinera:
    def __init__(self, localizacion, empresa="", precio=0, horario=""):
        self.empresa = empresa
        self._precio = float(str(precio).replace(",", "."))
        self._localizacion = localizacion
        self.horario = horario
        
        self.logger = utils.log("macime")

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

    def leerGasolineras(self, tipo):
        fichero = "macime/data/" + tipo.lower() + ".json"

        try:
            with open(fichero, "r") as f:
                respuesta = json.load(f)     
            self.logger.info('Read from %s', fichero)
        except:
            self.logger.error('Reading from %s', fichero)

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
        self.logger.info('Created list of gasolineras %s', str(id(gasolineras)))

        return gasolineras
