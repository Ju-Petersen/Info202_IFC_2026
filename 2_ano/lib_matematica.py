# # CODIGO DO PROFESSOR PARA UTILIZAR BIBLIOTECA DE TESTES 

# funções a serem testadas

def somar(a, b):
    return a + b

def fatorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return -1
    else:
        return n * fatorial(n-1)