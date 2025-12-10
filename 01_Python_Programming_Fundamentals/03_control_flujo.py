"""
Control de Flujo en Python
Condicionales, bucles y estructuras de control
"""

# 1. CONDICIONALES: if, elif, else
# --------------------------------
print("=== CONDICIONALES ===")


# Ejemplo 1: Calificación académica
def evaluar_calificacion(nota):
    """Evalúa una calificación y devuelve su categoría"""
    if nota >= 90:
        return "Excelente (A)"
    elif nota >= 80:
        return "Muy Bueno (B)"
    elif nota >= 70:
        return "Bueno (C)"
    elif nota >= 60:
        return "Suficiente (D)"
    else:
        return "Insuficiente (F)"


# Probar la función con diferentes notas
notas_ejemplo = [95, 85, 75, 65, 55]
for nota in notas_ejemplo:
    resultado = evaluar_calificacion(nota)
    print(f"Nota {nota}: {resultado}")

# Ejemplo 2: Verificación de acceso
edad = 20
tiene_permiso = True
es_miembro = False

print("\n=== VERIFICACIÓN DE ACCESO ===")
if edad >= 18 and tiene_permiso:
    if es_miembro:
        print("Acceso completo permitido - Miembro premium")
    else:
        print("Acceso básico permitido")
elif edad >= 16 and tiene_permiso:
    print("Acceso limitado para menores")
else:
    print("Acceso denegado")

# 2. BUCLES: for y while
# ----------------------
print("\n=== BUCLES FOR ===")

# Bucle for con lista
frutas = ["manzana", "banana", "cereza", "dátil"]
print("Lista de frutas:")
for i, fruta in enumerate(frutas):
    print(f"  {i + 1}. {fruta.capitalize()}")

# Bucle for con range
print("\nTabla del 5:")
for i in range(1, 11):
    print(f"  5 × {i} = {5 * i}")

# Bucle for con diccionario
estudiante = {"nombre": "Ana", "edad": 22, "carrera": "Ingeniería"}
print("\nDatos del estudiante:")
for clave, valor in estudiante.items():
    print(f"  {clave}: {valor}")

print("\n=== BUCLES WHILE ===")
# Ejemplo: Adivinar número
import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

print("Adivina el número entre 1 y 10")

while not adivinado and intentos < 3:
    try:
        guess = int(input("Tu intento: "))
        intentos += 1

        if guess == numero_secreto:
            print(f"¡Correcto! Adivinaste en {intentos} intentos")
            adivinado = True
        elif guess < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")

    except ValueError:
        print("Por favor ingresa un número válido")

if not adivinado:
    print(f"Lo siento, el número era {numero_secreto}")

# 3. CONTROL DE BUCLES: break, continue, pass
# -------------------------------------------
print("\n=== CONTROL DE BUCLES ===")

# break: salir del bucle
print("Números hasta encontrar el 5:")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")
print()

# continue: saltar a la siguiente iteración
print("Números impares del 1 al 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# pass: placeholder (no hace nada)
for i in range(5):
    pass  # Implementar más tarde

# 4. EJEMPLO PRÁCTICO: ANALIZADOR DE TEXTO
# ----------------------------------------
print("\n=== ANALIZADOR DE TEXTO ===")


def analizar_texto(texto):
    """Analiza un texto y proporciona estadísticas"""
    palabras = texto.split()
    caracteres_totales = len(texto)
    caracteres_sin_espacios = len(texto.replace(" ", ""))
    numero_palabras = len(palabras)

    # Contar palabras únicas
    palabras_unicas = set(palabras)

    # Encontrar palabra más larga
    palabra_mas_larga = max(palabras, key=len) if palabras else ""

    print(f"Estadísticas del texto:")
    print(f"  Caracteres totales: {caracteres_totales}")
    print(f"  Caracteres sin espacios: {caracteres_sin_espacios}")
    print(f"  Número de palabras: {numero_palabras}")
    print(f"  Palabras únicas: {len(palabras_unicas)}")
    print(f"  Palabra más larga: '{palabra_mas_larga}' ({len(palabra_mas_larga)} caracteres)")


# Texto de ejemplo
texto_ejemplo = "Python es un lenguaje de programación poderoso y fácil de aprender"
analizar_texto(texto_ejemplo)

# 5. EJEMPLO PRÁCTICO: GENERADOR DE PATRONES
# ------------------------------------------
print("\n=== GENERADOR DE PATRONES ===")


def generar_patron(tipo, filas):
    """Genera diferentes patrones con asteriscos"""
    print(f"Patrón {tipo} ({filas} filas):")

    if tipo == "triangulo":
        for i in range(1, filas + 1):
            print("*" * i)

    elif tipo == "piramide":
        for i in range(1, filas + 1):
            espacios = " " * (filas - i)
            asteriscos = "*" * (2 * i - 1)
            print(espacios + asteriscos)

    elif tipo == "cuadrado":
        for i in range(filas):
            if i == 0 or i == filas - 1:
                print("*" * filas)
            else:
                print("*" + " " * (filas - 2) + "*")


# Generar diferentes patrones
generar_patron("triangulo", 5)
print()
generar_patron("piramide", 4)
print()
generar_patron("cuadrado", 6)

