import requests
import sys
import json
import logging
import logging.config


def obtenerGasolineras(code):
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


def log(name_logger):
    loggers = logging.getLogger(name_logger)
    loggers.setLevel(logging.INFO)

    # logger_handler = logging.FileHandler(filename='log.txt')
    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setLevel(logging.INFO)
    logger_formatter = logging.Formatter(
        "%(asctime)s : [ %(name)s ] - %(levelname)s - %(message)s"
    )
    logger_handler.setFormatter(logger_formatter)

    loggers.addHandler(logger_handler)

    return loggers
