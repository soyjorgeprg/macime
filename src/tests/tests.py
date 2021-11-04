import sys
import unittest
import random
import pathlib

sys.path.insert(1, 'src')

from gasolinera import Gasolinera
from localizacion import Localizacion


class Pruebas(unittest.TestCase):

    def setUp(self):
        print("Montando entorno...")
        self.casa = Localizacion("Calle Forja 22", "28850", "Torrejon de Ardoz", "Madrid", 40.4529061660252, -3.459435975099579)
        self.tj = Localizacion("Calle Atenas 13", "28850", "Torrejon de Ardoz", "Madrid", 40.452929045397944, -3.459447353367767)
        self.sg = Localizacion("Calle Espronceda 3", "46520", "Puerto de Sagunto", "Valencia", 39.65821250951125, -0.21494956814433297)
        self.gasolineras = []

        self.gasolineras.append(Gasolinera("CEPSA", round(random.uniform(0.65, 0.89), 2), self.tj, ""))
        self.gasolineras.append(Gasolinera("BP", round(random.uniform(0.65, 0.89), 2), self.sg, ""))

    def test_cargas(self):
        '''
            Testing if all the object Localizacion was correctly created
        '''
        self.assertIsInstance(self.gasolineras[0].getLocalizacion(), type(self.tj))
        self.assertEqual(self.gasolineras[1].getLocalizacion(), self.sg)

    def test_localizacion(self):
        '''
            Testing if it returns a tuple
        '''
        self.assertIsInstance(self.tj.getLocalizacionPrecisa(), tuple)

    def test_distancia(self):
        '''
            Checking if it calculates distance correctly
        '''
        x = self.casa.distanciaMinima(self.gasolineras)
        self.assertEqual(x, 0)

    def test_gestiongasolineras(self):
        '''
            Checking if it get the json
        '''
        path = "src/data/glp.json"
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("No existe el fichero: %s" % path)
        else:
            g = Gasolinera()
            eess = g.leerGasolineras("GLP")
            self.assertIsInstance(eess, list)
            self.assertIsInstance(eess[0], type(g))
            self.assertIsInstance(eess[0].getLocalizacion(), type(self.tj))

    def tearDown(self):
        print("Destruyendo entorno...")
        del self.gasolineras

    if __name__ == "__main__":
        unittest.main()
