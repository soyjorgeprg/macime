from localizacion import Localizacion
from gasolinera import Gasolinera
from coche import Coche

import requests

def obtenerGasolineras(code):
    url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroProducto/" + code
    
    respuesta = requests.get(url).json()

    gasolineras = []

    for x in respuesta['ListaEESSPrecio']:
        l = Localizacion(x['Dirección'], x['C.P.'], x['Localidad'], x['Provincia'], x['Latitud'], x['Longitud (WGS84)'])
        gasolineras.append(Gasolinera(x['Rótulo'], x['PrecioProducto'], l, x['Horario']))

    return gasolineras


def main():
    glp = obtenerGasolineras('17')
    print(glp[0].getPrecio())
    # gnc = obtenerGasolineras('18')

if __name__ == "__main__":
    main()


