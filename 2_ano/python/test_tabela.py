import unittest
from tabela import *

class TestJogadores(unittest.TestCase):
    
    def test_jogadores(self):
        j1 = Jogador("Goleiro", "Alisson", "Liverpool FC")
        j2 = Jogador("Lateral", "Danilo", "CR Flamengo")
        j3 = Jogador("Atacante", "Endrick", "Olympique Lyonnais")
        j4 = Jogador("Meio-campo", "Bruno", "Newcastle United FC")
        j5 = Jogador("Zagueiro", "Bremer", "Juventus FC")
        self.assertEqual(j1.posicao, "Goleiro")
        self.assertEqual(j1.nome, "Alisson")
        self.assertEqual(j1.clube, "Liverpool FC")
        self.assertEqual(j2.posicao, "Lateral")
        self.assertEqual(j2.nome, "Danilo")
        self.assertEqual(j2.clube, "CR Flamengo")
        self.assertEqual(j3.posicao, "Atacante")
        self.assertEqual(j3.nome, "Endrick")
        self.assertEqual(j3.clube, "Olympique Lyonnais")
        self.assertEqual(j4.posicao, "Meio-campo")
        self.assertEqual(j4.nome, "Bruno")
        self.assertEqual(j4.clube, "Newcastle United FC")
        self.assertEqual(j5.posicao, "Zagueiro")
        self.assertEqual(j5.nome, "Bremer")
        self.assertEqual(j5.clube, "Juventus FC")

class TestSelecao:
    def teste_selecao(self):
        lst_j1 = [j1, j2, j3, j4, j5]
        s1 = Selecao("Sei lá", lst_j1)
        self.assertEqual(s1.nome, "Sei lá")

if __name__ == '__main__':
    # executa os testes
    unittest.main()