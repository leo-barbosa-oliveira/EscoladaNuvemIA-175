# 4- Conversor de Temperatura 

# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# Funções de conversão

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


# Entrada do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Conversão
resultado = None

if origem == destino:
    resultado = temperatura
elif origem == "C":
    if destino == "F":
        resultado = celsius_para_fahrenheit(temperatura)
    elif destino == "K":
        resultado = celsius_para_kelvin(temperatura)
elif origem == "F":
    if destino == "C":
        resultado = fahrenheit_para_celsius(temperatura)
    elif destino == "K":
        resultado = fahrenheit_para_kelvin(temperatura)
elif origem == "K":
    if destino == "C":
        resultado = kelvin_para_celsius(temperatura)
    elif destino == "F":
        resultado = kelvin_para_fahrenheit(temperatura)

# Saída
if resultado is not None:
    print(f"{temperatura:.2f}°{origem} equivale a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida! Use apenas C, F ou K.")