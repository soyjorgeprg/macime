from localizacion import Localizacion
from gasolinera import Gasolinera
from coche import Coche

import requests
import json

def obtenerGMapsApiKey():
    secrets_filename = 'key.json'
    api_keys = {}
    with open(secrets_filename, 'r') as f:
        api_keys = json.loads(f.read())

    return api_keys['MAPS_API_KEY']

def obtenerGasolineras(code):
    url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroProducto/" + code
    
    respuesta = requests.get(url).json()

    gasolineras = []

    for x in respuesta['ListaEESSPrecio']:
        l = Localizacion(x['Dirección'], x['C.P.'], x['Localidad'], x['Provincia'], x['Latitud'], x['Longitud (WGS84)'])
        gasolineras.append(Gasolinera(x['Rótulo'], x['PrecioProducto'], l, x['Horario']))

    return gasolineras

def distanciaMinima(direccion, gasolineras):
    origin = direccion.replace(" ", "+")

    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + origin +"&key=AIzaSyCiRfNspRJacWKMkE3osrjxsLYZnDcy1YQ"
    response = requests.get(url).json()
    lat_ori = response['results'][0]['geometry']['location'].get('lat')
    lng_ori = response['results'][0]['geometry']['location'].get('lng')

    distancias = []
    for es in gasolineras:
        lat, lng = es.getLocalizacion().getLocalizacionPrecisa()
        api_key = obtenerGMapsApiKey()

        lat_dest = str(lat).replace(',', '.')
        lng_dest = str(lng).replace(',', '.')

        url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(lat_ori) + "," + str(lng_ori)  + "&destination=" + lat_dest + "," + lng_dest + "&key=" + api_key
        response = requests.get(url).json()
        #print(response['routes'][0]['legs'][0]['distance'].get("value"))
        dist = response['routes'][0]['legs'][0]['distance'].get("value")
        distancias.append(dist)

    min_value = min(distancias)
    min_index = distancias.index(min_value)

    return min_index
    

def main():
    glp = obtenerGasolineras('17')
    #print(glp[0].getPrecio())
    # gnc = obtenerGasolineras('18')
    x = distanciaMinima("Calle Forja 22 28850 Torrejon de Ardoz", glp)
    print(glp[x])

if __name__ == "__main__":
    main()


