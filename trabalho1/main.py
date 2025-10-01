from funcoes import aceitarPalavra
from afd import delta, q0, F

palavra = ""
if aceitarPalavra(delta, q0, F, palavra):
    print("Palavra aceita")
else:
    print("Not accepted")