# main.py

from funcoes import TransformadorGramatica

def main():
    print("GLC: Remoção de Recursão + Fatoração")

    input_rules = [
        "A -> Aa | Ab | c",
        "B -> Bx | By | z",
        "S -> Xa | Xb | c",
        "X -> dX | e"
    ]
    
    print("\nGLC de Entrada:")
    for rule in input_rules:
        print(f"   {rule}")

    transformador = TransformadorGramatica()
    
    glc_inicial = transformador.analisar_glc(input_rules)

    glc_sem_recursao = transformador.remover_recursao_esquerda(glc_inicial)
    
    print("\nGLC Após Remoção da Recursão à Esquerda (Direta):")
    transformador.imprimir_glc(glc_sem_recursao)

    glc_final_fatorada = transformador.fatorar_esquerda(glc_sem_recursao)
    
    print("\nGLC Final (Sem Recursão + Fatorada à Esquerda):")
    transformador.imprimir_glc(glc_final_fatorada)

    print("Processo de Transformação Concluído")


if __name__ == "__main__":
    main()