# Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

import string

def eh_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo.
    
    Parâmetros:
        texto (str): A palavra ou frase a ser verificada.

    Retorna:
        str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    # Remove espaços, pontuação e coloca tudo em minúsculas
    texto_limpo = ''.join(
        c.lower() for c in texto if c.isalnum()
    )
    
    # Verifica se o texto é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)
print(f"É palíndromo? {resultado}")
