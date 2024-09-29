import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('tests')  # Busca todas las pruebas en la carpeta "tests"
    runner = unittest.TextTestRunner()
    runner.run(suite) 