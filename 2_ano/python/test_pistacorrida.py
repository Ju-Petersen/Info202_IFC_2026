import unittest
from classpista_corrida import *

class TestVeiculo(unittest.TestCase):
    def test_veiculo(self):
        obj_vei1 = Veiculo("AAAAAAAA", "azul", 50, 0.0, 10.5, "...")
        obj_vei2 = Veiculo("BBBBBBBB", "vermelho", 60, 0.0, 12.0, "...")
        obj_vei3 = Veiculo("CCCCCCCC", "preto", 70, 0.0, 15.9, "...")
        self.assertEqual(obj_vei1.placa, "AAAAAAAA")
        self.assertEqual(obj_vei1.cor, "azul")
        self.assertEqual(obj_vei1.tanque, 50)
        self.assertEqual(obj_vei1.odometro, 0.0)
        self.assertEqual(obj_vei1.rendimento, 10.5)
        self.assertEqual(obj_vei1.desenho, "...")
        self.assertEqual(obj_vei2.placa, "BBBBBBBB")
        self.assertEqual(obj_vei2.cor, "vermelho")
        self.assertEqual(obj_vei2.tanque, 60)
        self.assertEqual(obj_vei2.odometro, 0.0)
        self.assertEqual(obj_vei2.rendimento, 12.0)
        self.assertEqual(obj_vei2.desenho, "...")
        self.assertEqual(obj_vei3.placa, "CCCCCCCC")
        self.assertEqual(obj_vei3.cor, "preto")
        self.assertEqual(obj_vei3.tanque, 70)
        self.assertEqual(obj_vei3.odometro, 0.0)
        self.assertEqual(obj_vei3.rendimento, 15.9)
        self.assertEqual(obj_vei3.desenho, "...")

class TestPistaCorrida(unittest.TestCase):
    def test_pista(self):
        obj_pista = Pista(10)
        obj_vei1 = Veiculo("AAAAAAAA", "azul", 50, 0.0, 10.5, "...")
        obj_vei2 = Veiculo("BBBBBBBB", "vermelho", 60, 0.0, 12.0, "...")
        obj_vei3 = Veiculo("CCCCCCCC", "preto", 70, 0.0, 15.9, "...")
        ls_veis = [obj_vei1, obj_vei2, obj_vei3]
        self.assertEqual(obj_pista.extensao, 10)
        self.assertEqual(ls_veis, [obj_vei1, obj_vei2, obj_vei3])

if __name__ == '__main__':
    unittest.main()