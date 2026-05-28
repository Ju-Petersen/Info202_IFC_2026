import mysql.connector
class Pessoa:
    def __init__(self, nm, dt_nasc, cpf, em):
        self.nome = nm
        self.data_nascimento = dt_nasc
        self.cpf = cpf
        self.email = em

conn = mysql.connector.connect(
    host="10.10.8.17",
    user="root",
    password="root"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS pessoas_db")
cursor.execute("USE pessoas_db")
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
                  (id INT AUTO_INCREMENT PRIMARY KEY,
                   nome VARCHAR(255) NOT NULL,
                   email VARCHAR(255) NOT NULL,
                   telefone VARCHAR(50) NOT NULL)''')
conn.commit()

pessoa1 = Pessoa("João Silva", "jo@gmail.com", "47 91234567")

cursor.execute('INSERT INTO pessoas (nome, email, telefone) VALUES (%s, %s, %s)', 
               (pessoa1.nome, pessoa1.email, pessoa1.telefone))
conn.commit()
conn.close()

#feito no vscode da máquina local