
# Define una función para calcular el IMC (Índice de Masa Corporal)
def calcular_imc(peso, altura_cm):

# Convertir la altura de centímetros a metros
    altura_m = altura_cm / 100
    
# Calcular el IMC
    imc = peso / (altura_m ** 2)
    return imc

# Define una función para clasificar el IMC según la OMS
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"
    
# Ingresar el peso y la altura
peso = float(input("Ingrese su peso en Kg: \n"))
altura_cm = float(input("Ingrese su altura en centímetros: \n"))

# Calcular el IMC
imc = calcular_imc(peso, altura_cm)

# Clasificar el IMC
clasificacion = clasificar_imc(imc)

# Imprimir los resultados
print(f"Su IMC es: {imc:.2f}, lo que indica que la clasificación dada por la OMS es: {clasificacion}.")