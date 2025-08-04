# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

import requests

def consultar_endereco(cep):
    # Remove caracteres não numéricos
    cep = ''.join(filter(str.isdigit, cep))
    
    # Validação simples
    if len(cep) != 8:
        print("CEP inválido. Certifique-se de que contém 8 dígitos.")
        return
    
    # Faz a requisição para a API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("\n=== Endereço encontrado ===")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro:     {dados.get('bairro', 'N/A')}")
            print(f"Cidade:     {dados.get('localidade', 'N/A')}")
            print(f"Estado:     {dados.get('uf', 'N/A')}")
    else:
        print("Erro ao acessar a API. Código de status:", resposta.status_code)

# Entrada do usuário
cep_usuario = input("Digite o CEP (apenas números ou com traço): ")
consultar_endereco(cep_usuario)
