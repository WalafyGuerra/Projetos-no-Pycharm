def somar(a,b):
    return a+b

def exibir_resultado(a,b, funçao):
    resultado = funçao(a,b)
    print(f"O resultado da operaçao {a} + {b} = {resultado}")

exibir_resultado(10,10, somar)   # O resultado da operaçao 10 + 10 = 20