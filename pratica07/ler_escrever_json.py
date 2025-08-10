# Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

import json

# Nome do arquivo JSON
arquivo_json = "pessoa.json"

# ---------- Escrita no arquivo JSON ----------
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "cidade": "São Paulo"
}

# Salva os dados no arquivo JSON
with open(arquivo_json, "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

print(f"Arquivo '{arquivo_json}' criado com sucesso!")

# ---------- Leitura do arquivo JSON ----------
with open(arquivo_json, "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

print("\n📄 Dados lidos do arquivo JSON:")
print(f"Nome: {dados_lidos['nome']}")
print(f"Idade: {dados_lidos['idade']}")
print(f"Cidade: {dados_lidos['cidade']}")
