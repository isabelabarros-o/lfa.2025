import re


PADROES = {
    'nome': re.compile(r'^[a-zA-Z ]{1,50}$'),
    
    'cpf': re.compile(r'(\d{3}\.\d{3}\.\d{3}-\d{2})|\d{11}'),

    'email': re.compile(r'^[\w\._-]{2,}@[\w-]{2,}\.[a-z]{3}(\.(br|ao|pt|es|de|uk))?$'),
    
    'telefone': re.compile(r'^(\d{11}|\(\d{2}\)\d{5}-\d{4})$')
}

REGEX_EXTRACAO_EMAIL = r'[\w\._-]{2,}@[\w\._-]{2,}\.[a-z]{3}(\.(br|ao|pt|es|de|uk))?'


def validar_dados(dados):
    erros = {}
    
    if not PADROES['nome'].fullmatch(dados.get('nome', '')):
        erros['nome'] = "Nome inválido. Deve ter entre 1-50 letras ou espaços."
    
    if not PADROES['cpf'].fullmatch(dados.get('cpf', '')):
        erros['cpf'] = "CPF inválido. Use 11 dígitos ou formato 000.000.000-00."

    if not PADROES['email'].fullmatch(dados.get('email', '')):
        erros['email'] = "E-mail inválido. Verifique o formato (ex: user@domain.com ou user@domain.com.br)."

    if not PADROES['telefone'].fullmatch(dados.get('telefone', '')):
        erros['telefone'] = "Telefone inválido. Use 11 dígitos (ex: 11988887777) ou (00)00000-0000."
        
    return erros


def extrair_emails_validos(texto):
    regex_extracao = re.compile(
    r'[\w\._-]{2,}@[\w-]{2,}\.[a-z]{3}(?:\.(?:br|ao|pt|es|de|uk))?'
)
    
    return regex_extracao.findall(texto)