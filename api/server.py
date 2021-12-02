import sys

from blacksheep.server import Application
from blacksheep.contents import Content
from blacksheep.messages import Response

sys.path.insert(2, "macime")

from localizacion import Localizacion
from gasolinera import Gasolinera

app = Application()

def correccion_gestion(tipo, lat, lon, x=1):
    try:
        x = int(x)
    except:
        return Response(400, content=Content(b"text/plain", b"Problema con el numero de gasolineras"))
    try:
        lat = float(lat)
        lon = float(lon)
    except:
        return Response(400, content=Content(b"text/plain", b"Problema con las coordenadas"))
    if tipo not in str(["GLP", "GNC", "glp", "gnc"]):
        return Response(400, content=Content(b"text/plain", b"Problema con el tipo de combustible"))
    localizacion = Localizacion("", 0, "", "", lat, lon)
    g = Gasolinera(localizacion)
    eess = g.leerGasolineras(tipo)
    dist = localizacion.distanciasOrigen(eess)
    return (dist, localizacion)

def mejor_gasolinera(tipo, lat, lon):
    salida = correccion_gestion(tipo, lat, lon)
    if type(salida) == Response:
        return salida
    es = salida[1].mejorEESS(salida[0])
    result = es[1].__str__()
    return Response(200, content=Content(b"text/plain", bytes(result, 'utf-8')))

def gasolinera_cercana(tipo, lat, lon):
    salida = correccion_gestion(tipo, lat, lon)
    if type(salida) == Response:
        return salida
    result = salida[0]
    return Response(200, content=Content(b"text/plain", bytes(result[0][1].__str__(), 'utf-8')))

def x_gasolineras_cercanas(tipo, lat, lon, x):
    salida = correccion_gestion(tipo, lat, lon, x)
    if type(salida) == Response:
        return salida
    result = [gas[1].__str__() for gas in salida[0][:int(x)]]
    return Response(200, content=Content(b"text/plain", bytes(result.__str__(), 'utf-8'))) 

app.router.add_get("/api/mejorES/:tipo/:lat/:lon", mejor_gasolinera)
app.router.add_get("/api/cercanas/:tipo/:lat/:lon", gasolinera_cercana)
app.router.add_get("/api/cercanas/:tipo/:lat/:lon/:x", x_gasolineras_cercanas)

