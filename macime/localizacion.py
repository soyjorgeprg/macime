import requests
import json

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
        return self.direccion + self.cp + self.localidad + self.provincia

    def getLocalizacionPrecisa(self):
        return self.latitud, self.longitud

    def __str__(self):
        # return (self.latitud + "," + self.longitud)
        return self.direccion + " " + self.cp + " " + self.localidad + " " + self.provincia

    def obtenerGMapsApiKey(self):
        secrets_filename = 'macime/claves.json'
        with open(secrets_filename, 'r') as f:
            api_keys = json.loads(f.read())

        return api_keys['MAPS_API_KEY']

    def distanciaMinima(self, gasolineras):
        origin = self.getLocalizacion().replace(" ", "+")
        api_key = self.obtenerGMapsApiKey()

        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + origin + "&key=" + api_key
        response = requests.get(url).json()
        lat_ori = response['results'][0]['geometry']['location'].get('lat')
        lng_ori = response['results'][0]['geometry']['location'].get('lng')

        distancias = []
        for es in gasolineras:
            lat, lng = es.getLocalizacion().getLocalizacionPrecisa()
            api_key = self.obtenerGMapsApiKey()

            lat_dest = str(lat).replace(',', '.')
            lng_dest = str(lng).replace(',', '.')

            url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(lat_ori) + "," + str(lng_ori) + "&destination=" + lat_dest + "," + lng_dest + "&key=" + api_key
            response = requests.get(url).json()
            # print(response['routes'][0]['legs'][0]['distance'].get("value"))
            dist = response['routes'][0]['legs'][0]['distance'].get("value")
            distancias.append(dist)

        min_value = min(distancias)
        min_index = distancias.index(min_value)

        return min_index
