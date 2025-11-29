import re

EPSILON = 'ε'

class TransformadorGramatica:
    def __init__(self):
        self.contador_variaveis = 0

    def _obter_nova_variavel(self):
        new_var = f"A{self.contador_variaveis}'" if self.contador_variaveis > 0 else "A'"
        self.contador_variaveis += 1
        return new_var

    def analisar_glc(self, linhas_glc):
        gramatica = {}
        for line in linhas_glc:
            line = line.strip()
            if not line:
                continue
            
            if '->' not in line:
                print(f"Aviso: Linha de produção inválida: {line}")
                continue

            head, bodies_str = line.split('->', 1)
            head = head.strip()
            bodies = [body.strip() for body in bodies_str.split('|') if body.strip()]
            
            if head in gramatica:
                gramatica[head].extend(bodies)
            else:
                gramatica[head] = bodies
                
        for head in gramatica:
            gramatica[head] = list(set(gramatica[head]))

        return gramatica

    def imprimir_glc(self, gramatica):
        print("\n--- GLC Resultante ---")
        for head in sorted(gramatica.keys()):
            bodies = sorted(list(set(gramatica[head])))
            production = f"{head} -> {' | '.join(bodies)}"
            print(production)
        print("----------------------")
        return production

    def remover_recursao_esquerda(self, gramatica_original):
        print("-> Iniciando Remoção de Recursão à Esquerda (Direta)...")
        nova_gramatica = {}

        self.contador_variaveis = 0 
        
        for A, producoes in gramatica_original.items():
            alphas = []
            betas = []

            for producao in producoes:
                if producao.startswith(A):
                    alpha = producao[len(A):].strip()
                    if alpha:
                        alphas.append(alpha)
                    elif producao == A:
                        alphas.append(EPSILON)
                else:
                    betas.append(producao)
            
            if not alphas:
                nova_gramatica[A] = producoes
            else:
                
                A_linha = self._obter_nova_variavel()

                if not betas:
                    nova_gramatica[A] = [EPSILON]
                else:
                    nova_producoes_A = [f"{beta}{A_linha}" for beta in betas]
                    nova_gramatica[A] = nova_producoes_A

                nova_producoes_A_linha = [f"{alpha}{A_linha}" for alpha in alphas]
                nova_producoes_A_linha.append(EPSILON) 
                
                nova_gramatica[A_linha] = nova_producoes_A_linha
                
        return nova_gramatica

    def fatorar_esquerda(self, gramatica_original):
        print("-> Iniciando Fatoração à Esquerda...")
        gramatica_fatorada = {}
        
        self.contador_variaveis = 0 
        
        for A, producoes in gramatica_original.items():

            grupos_prefixo = {} 
            for p in producoes:
                prefixo = p[0] if p and p != EPSILON else p
                if prefixo not in grupos_prefixo:
                    grupos_prefixo[prefixo] = []
                grupos_prefixo[prefixo].append(p)
            
            
            novas_producoes_A = []
            
            for prefixo, grupo in grupos_prefixo.items():
                
                if len(grupo) == 1:
                    novas_producoes_A.extend(grupo)
                    continue

                prefixo_comum = grupo[0]
                for p in grupo[1:]:
                    i = 0
                    while i < len(prefixo_comum) and i < len(p) and prefixo_comum[i] == p[i]:
                        i += 1
                    prefixo_comum = prefixo_comum[:i]

                if prefixo_comum:
                    
                    A_linha = self._obter_nova_variavel()

                    novas_producoes_A.append(f"{prefixo_comum}{A_linha}")
                    
                    novas_producoes_A_linha = []
                    for p in grupo:
                        resto = p[len(prefixo_comum):].strip()
                        novas_producoes_A_linha.append(resto if resto else EPSILON)
                  
                    gramatica_fatorada[A_linha] = list(set(novas_producoes_A_linha))
                else:
                    novas_producoes_A.extend(grupo)

            gramatica_fatorada[A] = list(set(novas_producoes_A))

        return gramatica_fatorada