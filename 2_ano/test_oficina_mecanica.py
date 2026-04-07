# Biblioteca unittest:

import unittest
from oficina_mecanica import *

class TestOficina(unittest.TestCase):

    def test_pessoa(self):
        pess = Pessoa("João", "(47)123456", "28/01/2010")
        self.assertTrue(pess, Pessoa("João", "(47)123456", "28/01/2010"))

    def test_pess1(self):
        pess1 = Pessoa("Mario", "(47)654321", "02/12/2009")
        self.assertEqual(pess1, Pessoa("João", "(47)123456", "28/01/2010"))

if __name__ == '__main__':
    # executa os testes
    unittest.main()