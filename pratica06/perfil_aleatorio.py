# Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.

import requests

def gerar_usuario_aleatorio():
    # Faz a requisição para a API
    resposta = requests.get("https://randomuser.me/api/")
    
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("=== Perfil Gerado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API. Código de status:", resposta.status_code)

# Executa o programa
gerar_usuario_aleatorio()
