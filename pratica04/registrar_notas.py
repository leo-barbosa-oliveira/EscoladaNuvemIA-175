
# Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.

notas = []

print("Digite as notas dos alunos (de 0 a 10). Para encerrar, digite 'fim'.")

while True:
    entrada = input("Nota: ").strip().lower()
    
    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um número entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim' para encerrar.")

# Cálculo da média
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")