"""
Fundamentos de Python - Variables y Tipos de Datos
Ejemplos prácticos de variables y tipos básicos en Python
"""

# 1. VARIABLES BÁSICAS
# --------------------
# Enteros (int)
edad = 25
temperatura = -5
poblacion_mundial = 8000000000

print(f"Edad: {edad}")
print(f"Temperatura: {temperatura}°C")
print(f"Población mundial: {poblacion_mundial}")

# Flotantes (float)
precio = 19.99
pi = 3.14159
temperatura_promedio = 23.5

print(f"\nPrecio: ${precio}")
print(f"Valor de π: {pi}")
print(f"Temperatura promedio: {temperatura_promedio}°C")

# 2. CADENAS DE TEXTO (str)
# -------------------------
nombre = "Ana García"
mensaje = 'Hola mundo'
direccion = """Calle Principal 123,
Ciudad, País"""

print(f"\nNombre: {nombre}")
print(f"Mensaje: {mensaje}")
print(f"Dirección: {direccion}")

# Operaciones con strings
nombre_completo = nombre + " - Estudiante"
print(f"Nombre completo: {nombre_completo}")
print(f"Longitud del nombre: {len(nombre)} caracteres")

# 3. BOOLEANOS (bool)
# -------------------
es_estudiante = True
tiene_trabajo = False
mayor_de_edad = edad >= 18

print(f"\n¿Es estudiante? {es_estudiante}")
print(f"¿Tiene trabajo? {tiene_trabajo}")
print(f"¿Es mayor de edad? {mayor_de_edad}")

# 4. CONVERSIÓN DE TIPOS
# ----------------------
# De string a número
numero_texto = "100"
numero_entero = int(numero_texto)
numero_decimal = float("3.14")

print(f"\nConversiones:")
print(f"Texto '100' a entero: {numero_entero}")
print(f"Texto '3.14' a float: {numero_decimal}")

# De número a string
edad_texto = str(edad)
precio_texto = str(precio)

print(f"Edad {edad} a texto: '{edad_texto}'")
print(f"Precio {precio} a texto: '{precio_texto}'")

# 5. OPERACIONES MATEMÁTICAS
# --------------------------
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
potencia = a ** b

print(f"\nOperaciones con {a} y {b}:")
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} × {b} = {multiplicacion}")
print(f"División: {a} ÷ {b} = {division:.2f}")
print(f"División entera: {a} // {b} = {division_entera}")
print(f"Módulo: {a} % {b} = {modulo}")
print(f"Potencia: {a} ^ {b} = {potencia}")

# 6. ENTRADA DEL USUARIO
# ----------------------
# nombre_usuario = input("¿Cuál es tu nombre? ")
# edad_usuario = int(input("¿Cuántos años tienes? "))

# print(f"\nHola {nombre_usuario}, tienes {edad_usuario} años")

