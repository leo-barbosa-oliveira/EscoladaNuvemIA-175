# Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes.d

import re
import statistics

# Solicita o caminho do arquivo
arquivo_log = input("Digite o caminho completo do arquivo de log: ").strip()

tempos = []

try:
    # Abre e lê o arquivo linha por linha
    with open(arquivo_log, "r", encoding="utf-8") as f:
        for linha in f:
            # Procura um número seguido de 's' (ex: 12.34s ou 15s)
            match = re.search(r"([\d.]+)\s*s", linha)
            if match:
                tempos.append(float(match.group(1)))

    # Calcula média e desvio padrão
    if tempos:
        media = statistics.mean(tempos)
        desvio_padrao = statistics.pstdev(tempos)  # populacional
        print(f"\nMédia do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio_padrao:.2f} segundos")
    else:
        print("Nenhum tempo de execução encontrado no arquivo.")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho informado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

