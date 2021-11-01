import sys
sys.path.insert(1, 'src')

from gasolinera import Gasolinera
from localizacion import Localizacion


import unittest
import random

class Pruebas(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto...")
        self.l = Localizacion("Calle Atenas 13", "28850", "Torrejon de Ardoz", "Madrid", 40.452929045397944, -3.459447353367767)
        self.L = Localizacion("Calle Espronceda 3", "46520", "Puerto de Sagunto", "Valencia", 39.65821250951125, -0.21494956814433297)
        self.gasolineras = []
        
        self.gasolineras.append(Gasolinera("CEPSA", round(random.uniform(0.65, 0.89), 2), self.l, ""))
        self.gasolineras.append(Gasolinera("BP", round(random.uniform(0.65, 0.89), 2), self.L, ""))


    def test_cargas(self):
        # Testing if all the object Localizacion was correctly created
        self.assertEqual(type(self.gasolineras[0].getLocalizacion()), type(self.l))
        self.assertEqual(self.gasolineras[1].getLocalizacion(), self.L)

    
    def test_localizacion(self):
        # Testing it returns a tuple of floats
        self.assertEqual(type(self.l.getLocalizacionPrecisa()), type((float, float)))
        

    
    def tearDown(self):
        print("Limpiando contexto")
        del(self.gasolineras)

    if __name__ == "__main__":
        unittest.main()
