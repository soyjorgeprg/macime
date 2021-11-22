import sys
import unittest
import random
import pathlib

sys.path.insert(2, "macime")

from gasolinera import Gasolinera
from localizacion import Localizacion


class Pruebas(unittest.TestCase):
    def setUp(self):
        self.localizacion = []
        self.gasolineras = []

        self.localizacion.append(
            Localizacion(
                "Calle Forja 22",
                "28850",
                "Torrejon de Ardoz",
                "Madrid",
                "40,4529061660252",
                "-3,459435975099579",
            )
        )
        self.localizacion.append(
            Localizacion(
                "Calle Atenas 13",
                "28850",
                "Torrejon de Ardoz",
                "Madrid",
                "40,45966642667289",
                "-3,469308315651375",
            )
        )
        self.localizacion.append(
            Localizacion(
                "Calle Espronceda 3",
                "46520",
                "Puerto de Sagunto",
                "Valencia",
                "39,65821250951125",
                "-0,21494956814433297",
            )
        )

        self.gasolineras.append(
            Gasolinera(
                self.localizacion[0], "CEPSA", round(random.uniform(0.65, 0.89), 2)
            )
        )
        self.gasolineras.append(
            Gasolinera(self.localizacion[2], "BP", round(random.uniform(0.65, 0.89), 2))
        )
        self.gasolineras.append(
            Gasolinera(
                self.localizacion[1], "SHELL", round(random.uniform(0.65, 0.89), 2)
            )
        )

    def test_cargas(self):
        """
        Testing if all the object Localizacion was correctly created
        """
        self.assertIsInstance(
            self.gasolineras[0].localizacion, type(self.localizacion[0])
        )
        self.assertEqual(self.gasolineras[1].localizacion, self.localizacion[2])

    def test_localizacion(self):
        """
        Testing if it returns a tuple
        """
        self.assertIsInstance(self.localizacion[1].coordenadas, tuple)

    def test_distancia(self):
        """
        Checking if it calculates distance correctly
        """
        distancias = self.localizacion[0].distanciasOrigen(self.gasolineras)
        self.assertIsInstance(distancias, list)
        self.assertIsInstance(distancias[0], list)
        self.assertEqual(distancias[0][0], 0)

    def test_gestiongasolineras(self):
        """
        Checking if it get the json
        """
        path = "macime/data/glp.json"
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("No existe el fichero: %s" % path)
        else:
            g = Gasolinera(self.localizacion[0])
            eess = g.leerGasolineras("GLP")
            self.assertIsInstance(eess, list)
            self.assertIsInstance(eess[0], type(g))
            self.assertIsInstance(eess[0].localizacion, type(self.localizacion[1]))

    def test_mejorestacionservicio(self):
        """
        The best eess is selected by the function
        """
        dist = self.localizacion[0].distanciasOrigen(self.gasolineras)
        es = self.localizacion[0].mejorEESS(dist)
        self.assertIsInstance(es[1], type(self.gasolineras[0]))
        self.assertEqual(es[0], 0.0)

    def tearDown(self):
        del self.gasolineras
        del self.localizacion


if __name__ == "__main__":
    unittest.main()
