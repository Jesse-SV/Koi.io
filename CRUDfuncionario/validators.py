import re
from django.core.exceptions import ValidationError

def valida_cnpj(cnpj):
    # Remove caracteres especiais e espaços
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verifica se o CNPJ possui 14 dígitos
    if len(cnpj) != 14:
        raise ValidationError(("Error"), code="invalid_text")

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(12):
        soma += int(cnpj[i]) * (i % 8 + 2)
    digito1 = (11 - soma % 11) % 10

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(13):
        soma += int(cnpj[i]) * (i % 8 + 2)
    digito2 = (11 - soma % 11) % 10

    # Verifica se os dígitos calculados são iguais aos dígitos informados
#    if(cnpj[12:14] == f'{digito1}{digito2}'):
#        rais
    return cnpj[12:14] == f'{digito1}{digito2}'
        
def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
        # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

        # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

        # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

        # Verifica se os dígitos verificadores são iguais aos dois últimos dígitos do CPF
    return cpf[-2:] == f"{digito1}{digito2}"
def valida_texto(text):
    text = re.sub(r"\s+", "", text)
    print(text)
    if not text.isalpha():
        raise ValidationError(
            ("O nome de usuário está incorreto, apenas caracteres aceitos"),
            code="invalid_text",
            )
def valida_cep(cep):
    # Remove qualquer caractere não numérico
    cep = re.sub(r'\D', '', cep)
    
    # Verifica se o CEP tem 8 dígitos
    if len(cep) != 8:
        raise ValidationError(("Formato CEP não aceito."), 
                               code="invalid_text"
                               )
    
    # Verifica se o CEP está no formato correto (cinco dígitos, hífen, três dígitos)
    if not re.match(r'^\d{5}-\d{3}$', cep):
        raise ValidationError(("Formato CEP não aceito."), 
                               code="invalid_text"
                               )