# importações
from pony.orm import *
import os # comandos do sistema operacional
import random

# criando variável de acesso ao pony
db = Database()

# definição da classe: 
# é preciso herdar da classe Entity
class Pessoa(db.Entity):
    _table_ = "pessoa_db_julia"
    nome = Required(str)   # atributo string obrigatório
    email = Required(str, 100)  # atributo string obrigatório com máximo de 100 caracteres
    telefone = Optional(str, nullable=True) # atributo opcional
    # cpf = Required(str, 11, unique=True) # atributo obrigatório com tamanho fixo e único

# obtendo dados de conexão com o banco, 
# a partir de variáveis de ambiente
dname    = os.getenv("DATABASE_NAME")
host     = os.getenv("DATABASE_HOST")
user     = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
port     = os.getenv("DATABASE_PORT")

db.bind(provider='mysql', host=host, 
        user=user, password=password, database=dname)

# innformando que deve criar as tabelas, caso não existam
db.generate_mapping(create_tables=True)

# solicitando para mostrar os comandos SQL que vão sendo executados
set_sql_debug(True)

# iniciando uma sessão
with db_session:

    # criando uma pessoa
    jo = Pessoa(nome='João da Silva', email='josilva@gmail.com') # cpf='12345678901')
    ma = Pessoa(nome='Mário do Armário', email='marionarmario@gmail.com', telefone='(11) 91234-5678') # cpf='98765432109')

    #criando várias pessoas:
    nomes = [
   'João', 'Maria', 'Pedro', 'Ana', 'Lucas',
   'Juliana', 'Carlos', 'Fernanda', 'Rafael',
   'Camila', 'Gabriel', 'Beatriz', 'Mateus',
   'Larissa', 'Bruno', 'Mariana', 'Felipe',
   'Amanda', 'Gustavo', 'Letícia'
   ]
    sobrenomes = [
    'Silva', 'Santos', 'Oliveira', 'Souza', 'Costa',
    'Pereira', 'Rodrigues', 'Almeida', 'Nascimento',
    'Lima', 'Araújo', 'Fernandes', 'Carvalho',
    'Gomes', 'Martins', 'Ribeiro', 'Alves'
        ]

    for i in range(10000): # i entre 10 mil pessoas:
        novo = f'{random.choice(nomes)} {random.choice(sobrenomes)}'
        # seleciona uma nova pessoa com informações 
        # variáveis dentro da lista de nomes e sobrenomes
        pessoa = Pessoa(nome=novo, email=f'pessoa{i}@gmail.com') # cria a nova pessoa (de acordo com onde i está no loop)

    # salvando
    commit()

    # exibindo os dados
    print(pessoa.nome, pessoa.email)
    # existe um ID?
    print(pessoa.id)

'''
Exercícios:

1) Conecte-se a um banco de dados MySql com o DBeaver para ver se
a tabela foi criada e os dados estão lá

2) Descomente a linha 30 e execute novamente o programa, para ver
os códigos SQL que estão sendo executados

- contar quantos registros existem na tabela - FEITO
- verificar se existem nomes duplicados na tabela - FEITO
- mostrar quantas vezes cada nome aparece na tabela - FEITO
- mostrar os nomes em ordem alfabética - FEITO
- descobrir qual é o nome que mais se repete na tabela - FEITO
'''