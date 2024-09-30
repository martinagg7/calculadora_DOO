import unittest
#tuve que poner esto porque como los arhivos tests están en una carpeta sino no me los lee
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('tests')  
    runner = unittest.TextTestRunner()
    runner.run(suite) 