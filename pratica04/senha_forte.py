# Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

def senha_forte(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

print("Verificador de Senha Forte")
print("A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
print("Digite 'sair' para encerrar.")

while True:
    senha = input("Digite a senha: ").strip()
    
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    if senha_forte(senha):
        print("Senha forte cadastrada com sucesso!")
        break
    else:
        print("Senha fraca. Tente novamente.")
