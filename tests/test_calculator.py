import unittest
from source.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):

        self.calc = Calculator()

    def test_suma(self):
        self.assertEqual(self.calc.suma(2, 3), 5)
        self.assertEqual(self.calc.suma(8, 7), 15)
        self.assertEqual(self.calc.suma(-5, 5), 0)  
        self.assertEqual(self.calc.suma(0, 0), 0)   

    def test_resta(self):
        self.assertEqual(self.calc.resta(5, 3), 2)
        self.assertEqual(self.calc.resta(8, 7), 1)
        self.assertEqual(self.calc.resta(5, 0), 5)   

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicacion(2, 3), 6)
        self.assertEqual(self.calc.multiplicacion(5, 0), 0)  
        self.assertEqual(self.calc.multiplicacion(-4, 3), -12) 
       

    def test_division(self):

        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(9, 3), 3)
        #self.assertRaisses(ValueError)->para lanzar error al dividir x0
        with self.assertRaises(ValueError):
            self.calc.division(5, 0)  

    def test_potencia(self):

        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)  

    def test_factorial(self):

        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)  
        #sel.assertRaises(ValueError)->Factorial num negativo
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)  

if __name__ == '__main__':
    unittest.main()
