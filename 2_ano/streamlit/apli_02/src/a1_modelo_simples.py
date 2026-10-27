class Pessoa:
    def __init__(self, nome : str, email : str, telefone : str):
        self.nome = nome
        self.email = email
        self.telefone = telefone

# banco de dados "interno": apenas uma lista :-)
pessoas_interno = [
    Pessoa("João da Silva", "josilva@gmail.com", "47 9123 4567"),
    Pessoa("Maria Oliveira", "maliv@gmail.com", "47 98877665")
]