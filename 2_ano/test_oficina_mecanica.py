# Biblioteca unittest:
import unittest
from oficina_mecanica import *

class TestPessoa(unittest.TestCase):

    def test_pessoa(self):
        obj = Pessoa("João", "(47)123456", "28/01/2010")
        self.assertEqual(obj.nome, "João")
        self.assertEqual(obj.telefone, "(47)123456")
        self.assertEqual(obj.data_nascimento, "28/01/2010")

class TestMecanico(unittest.TestCase):

    def test_mecanico(self):
        obj_mec = Pessoa("Mario", "(47)654321", "02/12/2009")
        self.assertEqual(obj_mec.nome, "Mario")
        self.assertEqual(obj_mec.telefone, "(47)654321")
        self.assertEqual(obj_mec.data_nascimento, "02/12/2009")

class TestCliente(unittest.TestCase):
    def test_cliente(self):
         obj = Pessoa("João", "(47)123456", "28/01/2010")
         obj_cli = Cliente(obj, "joaoo@gmail.com")
         self.assertEqual(obj.nome, "João")
         self.assertEqual(obj_cli.email, "joaoo@gmail.com")

class TestServico(unittest.TestCase):
    def test_servico(self):
        obj_ser = Servico("troca de pneu", 250)
        self.assertEqual(obj_ser.descricao, "troca de pneu")
        self.assertEqual(obj_ser.valor, 250)

class TestOrdemservico(unittest.TestCase):
    def test_ordemservico(self):
        obj_vei = Carro("AAAAAAAA", 5, "azul", 4)
        obj = Pessoa("João", "(47)123456", "28/01/2010")
        obj_cli = Cliente(obj, "joaoo@gmail.com")
        obj_ordser = Ordem_servico("31/03/2026", obj_vei, "01/04/2026", obj_cli, f"{20}%")
        self.assertEqual(obj_ordser.cliente.pessoa.nome, "João")
        self.assertEqual(obj_ordser.cliente.pessoa.data_nascimento, "28/01/2010")
        self.assertEqual(obj_ordser.cliente.pessoa.telefone, "(47)123456")
        self.assertEqual(obj_ordser.cliente.email, "joaoo@gmail.com")
        self.assertEqual(obj_ordser.data_entrada, "31/03/2026")
        self.assertEqual(obj_ordser.data_saida, "01/04/2026")
        self.assertEqual(obj_ordser.desconto, f"{20}%")
        self.assertEqual(obj_ordser.veiculo.cor, "azul")
        self.assertEqual(obj_ordser.veiculo.lugares, 5)
        self.assertEqual(obj_ordser.veiculo.placa, "AAAAAAAA")
        self.assertEqual(obj_ordser.veiculo.portas, 4)

class TestServicorealizado(unittest.TestCase):
    def test_servicorealizado(self):
        obj = Pessoa("João", "(47)123456", "28/01/2010")
        obj_ser = Servico("troca de pneu", 250)
        obj_mec = Pessoa("Mario", "(47)654321", "02/12/2009")
        obj_vei = Carro("AAAAAAAA", 5, "azul", 4)
        obj_cli = Cliente(obj, "joaoo@gmail.com")
        obj_ordser = Ordem_servico("31/03/2026", obj_vei, "01/04/2026", obj_cli, 20)
        obj_serre = Servico_realizado(obj_ser, obj_mec, obj_ordser)
        self.assertEqual(obj_serre.mecanico.nome, "Mario")
        self.assertEqual(obj_serre.mecanico.data_nascimento, "02/12/2009")
        self.assertEqual(obj_serre.mecanico.telefone, "(47)654321")
        self.assertEqual(obj_serre.ordem_servico.cliente.pessoa.nome, "João")
        self.assertEqual(obj_serre.ordem_servico.cliente.email, "joaoo@gmail.com")
        self.assertEqual(obj_serre.ordem_servico.data_entrada, "31/03/2026")
        self.assertEqual(obj_serre.ordem_servico.data_saida, "01/04/2026")
        self.assertEqual(obj_serre.ordem_servico.desconto, 20)

class TestOrdemservico(unittest.TestCase):
    def test_ordemservico(self):
        obj = Pessoa("João", "(47)123456", "28/01/2010")
        obj_cli = Cliente(obj, "joaoo@gmail.com")
        obj_vei = Carro("AAAAAAAA", 5, "azul", 4)
        obj_ordser = Ordem_servico("31/03/2026", obj_vei, "01/04/2026", obj_cli, 20)
        self.assertEqual(obj_ordser.data_entrada, "31/03/2026")
        self.assertEqual(obj_ordser.cliente.pessoa.nome, "João")
        self.assertEqual(obj_ordser.cliente.pessoa.data_nascimento, "28/01/2010")
        self.assertEqual(obj_ordser.cliente.pessoa.telefone, "(47)123456")
        self.assertEqual(obj_ordser.cliente.email, "joaoo@gmail.com")
        self.assertEqual(obj_ordser.veiculo.cor, "azul")
        self.assertEqual(obj_ordser.veiculo.lugares, 5)
        self.assertEqual(obj_ordser.veiculo.placa, "AAAAAAAA")
        self.assertEqual(obj_ordser.veiculo.portas, 4)
        self.assertEqual(obj_ordser.data_saida, "01/04/2026")
        self.assertEqual(obj_ordser.desconto, 20)

class TestVeiculo(unittest.TestCase):
    def test_veiculo(self):
        obj_vei = Veiculo("AAAAAAAA", "azul")
        self.assertEqual(obj_vei.placa, "AAAAAAAA")
        self.assertEqual(obj_vei.cor, "azul")

class TestMoto(unittest.TestCase):
    def test_moto(self):
        obj_mot = Moto("BBBBBBBB", "preta")
        self.assertEqual(obj_mot.placa, "BBBBBBBB")
        self.assertEqual(obj_mot.cor, "preta")

class TestVeiculoComPassageiro(unittest.TestCase):
    def test_veiculocompassageiros(self):
        obj_vei = VeiculoComPassageiro("CCCCCCCC", "verde", 10)
        self.assertEqual(obj_vei.placa, "CCCCCCCC")
        self.assertEqual(obj_vei.cor, "verde")
        self.assertEqual(obj_vei.lugares, 10)

class TestCarro(unittest.TestCase):
    def test_carro(self):
        obj_car = Carro("DDDDDDDD", 5, "branco", 4)
        self.assertEqual(obj_car.placa, "DDDDDDDD")
        self.assertEqual(obj_car.lugares, 5)
        self.assertEqual(obj_car.cor, "branco")
        self.assertEqual(obj_car.portas, 4)

class TestOnibus(unittest.TestCase):
    def test_onibus(self):
        obj_oni = Onibus("EEEEEEEE", "vermelho", 50)
        self.assertEqual(obj_oni.placa, "EEEEEEEE")
        self.assertEqual(obj_oni.cor, "vermelho")
        self.assertEqual(obj_oni.lugares, 50)

if __name__ == '__main__':
    # executa os testes
    unittest.main()
# terminar de fazer os testes para todas as classes.