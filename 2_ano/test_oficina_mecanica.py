# Biblioteca unittest:

import unittest
from oficina_mecanica import *

class TestOficina(unittest.TestCase):

    def test_pessoa(self):
        obj = Pessoa("João", "(47)123456", "28/01/2010")
        self.assertEqual(obj.nome, "João")
        self.assertEqual(obj.telefone, "(47)123456")
        self.assertEqual(obj.data_nascimento, "28/01/2010")

    def test_pessoa1(self):
        obj1 = Pessoa("João", "(47)123456", "28/01/2010")
        self.assertEqual(obj1.nome, "-1")
        self.assertEqual(obj1.telefone, "ABCDE")
        self.assertEqual(obj1.data_nascimento, "-0/-10/-2919")

if __name__ == '__main__':
    # executa os testes
    unittest.main()