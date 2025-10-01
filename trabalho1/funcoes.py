from afd import *

def funcaoTransicao(estado, simbolo):
    return delta.get((estado, simbolo))

def funcaoTransicaoExtendida(estado, palavra):
    if palavra == "":
        return estado
    else:
        
        primeiroSimbolo = palavra[0]
        resto = palavra[1:]
        proxEstado = funcaoTransicao(estado, primeiroSimbolo)
        if proxEstado is None:
            return None 
        return funcaoTransicaoExtendida(proxEstado, resto)

def aceitarPalavra(dfa, estadoInicial, estadoFinal, palavra):
    estadoFinal = funcaoTransicaoExtendida(estadoInicial, palavra)
    return estadoFinal in estadoFinal