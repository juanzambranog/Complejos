import operaciones_complejos as lc
import unittest

class TestOperations(unittest.TestCase):

    def test_suma(self):
        suma1= lc.suma((3,2),(-5,5.2))
        self.assertAlmostEqual(suma1[0],-2)
        self.assertAlmostEqual(suma1[1],7.2)

        suma2= lc.suma((7,3),(5.5,1.2))
        self.assertAlmostEqual(suma2[0],12.5)
        self.assertAlmostEqual(suma2[1],4.2)

    def test_mult(self):
        mult1 = lc.mult((3, 2), (-5, 5.2))
        self.assertAlmostEqual(mult1[0], -25.4)
        self.assertAlmostEqual(mult1[1], 5.60)

        mult2 = lc.mult((7, 3), (5.5, 1.2))
        self.assertAlmostEqual(mult2[0], 34.9)
        self.assertAlmostEqual(mult2[1], 24.9)

    def test_resta(self):
        resta1 = lc.resta((3, 2), (-5, 5.2))
        self.assertAlmostEqual(resta1[0], 8)
        self.assertAlmostEqual(resta1[1], -3.2)

        resta2 = lc.resta((7, 3), (5.5, 1.2))
        self.assertAlmostEqual(resta2[0], 1.5)
        self.assertAlmostEqual(resta2[1], 1.8)

    def test_divi(self):
        divi1 = lc.divi((3, 2), (-5, 5.2))
        self.assertAlmostEqual(divi1[0], -0.08839354342813219)
        self.assertAlmostEqual(divi1[1], -0.49192928516525747)

        divi2 = lc.divi((7, 3), (5.5, 1.2))
        self.assertAlmostEqual(divi2[0], 1.3284947933101925)
        self.assertAlmostEqual(divi2[1], 0.2556011360050489)


    def test_modulo(self):
        self.assertAlmostEqual(lc.modulo((3, 2)), 3.605551275463989)
        self.assertAlmostEqual(lc.modulo((7, 3)), 7.615773105863909)

    def test_conjugado(self):
        self.assertEqual(lc.conjugado((3, 2)), (3, -2))
        self.assertEqual(lc.conjugado((7, 3)), (7, -3))

    def test_polar(self):
        polar1 = lc.polar((3, 2))
        self.assertAlmostEqual(polar1[0], 3.0)
        self.assertAlmostEqual(polar1[1], 1.9999999999999996)
        polar2 = lc.polar((7, 3))
        self.assertAlmostEqual(polar2[0], 7.000000000000001)
        self.assertAlmostEqual(polar2[1], 3.0)





if __name__ == '__main__':
    unittest.main()