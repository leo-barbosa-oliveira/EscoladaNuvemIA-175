# Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.

import random
import string

def gerar_senha(tamanho):
    # Define os caracteres possíveis: letras, dígitos e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Entrada do usuário
try:
    tamanho = int(input("Informe o número de caracteres para a senha: "))
    if tamanho <= 0:
        print("Por favor, informe um número positivo.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
