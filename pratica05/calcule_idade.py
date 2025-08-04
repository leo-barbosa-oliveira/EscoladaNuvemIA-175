# Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    # Obtém o ano atual
    ano_atual = date.today().year
    
    # Calcula a idade em anos
    idade_anos = ano_atual - ano_nascimento
    
    # Considera um ano com 365 dias (sem considerar anos bissextos)
    idade_dias = idade_anos * 365
    
    return idade_dias

# Exemplo de uso:
ano = int(input("Informe o ano de nascimento: "))
dias = calcular_idade_em_dias(ano)
print(f"Você tem aproximadamente {dias} dias de vida.")
