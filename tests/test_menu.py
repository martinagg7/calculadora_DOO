import unittest
from unittest.mock import patch
from source.menu import ejecutar_calculadora

class TestMenu(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '5', '3', '0'])  # Simula los inputs del usuario
    @patch('builtins.print')  # Simula las impresiones en consola
    def test_menu_suma(self, mock_print, mock_input):
        ejecutar_calculadora()
        mock_print.assert_any_call("Resultado: 8")  # Verifica que el resultado impreso es correcto

    @patch('builtins.input', side_effect=['2', '10', '5', '0'])
    @patch('builtins.print')
    def test_menu_resta(self, mock_print, mock_input):
        ejecutar_calculadora()
        mock_print.assert_any_call("Resultado: 5")  # Verifica el resultado de la resta

    @patch('builtins.input', side_effect=['3', '2', '3', '0'])
    @patch('builtins.print')
    def test_menu_multiplicacion(self, mock_print, mock_input):
        ejecutar_calculadora()
        mock_print.assert_any_call("Resultado: 6")  # Verifica el resultado de la multiplicación

    @patch('builtins.input', side_effect=['4', '10', '2', '0'])
    @patch('builtins.print')
    def test_menu_division(self, mock_print, mock_input):
        ejecutar_calculadora()
        mock_print.assert_any_call("Resultado: 5.0")  # Verifica el resultado de la división

    @patch('builtins.input', side_effect=['6', '5', '0'])
    @patch('builtins.print')
    def test_menu_factorial(self, mock_print, mock_input):
        ejecutar_calculadora()
        mock_print.assert_any_call("Resultado: 120")  # Verifica el resultado del factorial

if __name__ == '__main__':
    unittest.main()
