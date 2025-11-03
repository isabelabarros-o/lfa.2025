# Trabalho 2 de Linguagens Formais e Autômatos 2025/2
# Autora: Isabela Barros de Oliveira


from funcoes import extrair_emails_validos, validar_dados

  
texto_para_extrair = """
    Prezado usuário,
    Aqui estão os contatos do nosso time de suporte:
    - alice.souza@gmail.com
    - suporte_23@empresa-tech.com
    - joao99@dominio123.org
    - erro.email@gmail..com
    Por favor, envie suas dúvidas para qualquer um dos e-mails válidos acima.
    Atenciosamente,
    Equipe de Atendimento
    """
    
print(f"\nTexto para extração:\n{texto_para_extrair}")
    
emails_encontrados = extrair_emails_validos(texto_para_extrair)
    
print("E-mails válidos extraídos:") 
if emails_encontrados:
    for email in emails_encontrados:
            print(f"- {email}")
else:
    print("Nenhum e-mail válido encontrado.")

print("\nValidação de dados de formulário:")        
formulario = {
    'nome': "Alice Barros",
    'cpf': "123.456.789-10",
    'email': "alice.barros@gmail.com.br", 
    'telefone': "(63)00000-0000"
        }
    
print(f"\nTestando formulário: {formulario}")
erros_1 = validar_dados(formulario)
if not erros_1:
        print("Resultado: Formulário VÁLIDO")
else:
        print(f"Resultado: Formulário INVÁLIDO \nErros: {erros_1}")