import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(calculadora.sumar(3,3), 6)
        self.assertEqual(calculadora.sumar(3,-2), 1)
        self.assertEqual(calculadora.sumar(-3,-3), -6)

    def test_restar(self):
        self.assertEqual(calculadora.restar(3,3), 3-3)
        self.assertEqual(calculadora.restar(3,-2), 3+2)
        self.assertEqual(calculadora.restar(-3,-3), 0)

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(4,2),2)
        self.assertEqual(calculadora.dividir(5,2),2.5)

        self.assertRaises(ValueError, calculadora.dividir, 3,0)


if __name__ == "__main__":
    unittest.main()
