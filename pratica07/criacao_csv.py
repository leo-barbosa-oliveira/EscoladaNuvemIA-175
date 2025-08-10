# Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.


import csv

# Nome do arquivo CSV
arquivo_csv = "dados_pessoais.csv"

# Dados para escrever
dados = [
    ["Nome", "Idade", "Cidade"],  # Cabeçalho
    ["Ana Silva", 28, "São Paulo"],
    ["Carlos Pereira", 35, "Rio de Janeiro"],
    ["Mariana Costa", 22, "Belo Horizonte"],
    ["João Souza", 40, "Curitiba"]
]

# Criando e escrevendo no arquivo CSV
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")