def resultado_lista_inteiro(resultado):
    resultado = list(map(int, resultado.split(",")))
    return resultado

def compara_resultado(resultado, x):
    resultado_ = set(resultado).intersection(x)
    acertos = len(resultado_)
    return acertos
