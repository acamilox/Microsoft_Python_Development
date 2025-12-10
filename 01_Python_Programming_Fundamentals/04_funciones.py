"""
Funciones en Python
Definición, parámetros, retorno y alcance
"""

# 1. FUNCIONES BÁSICAS
# --------------------
print("=== FUNCIONES BÁSICAS ===")

def saludar():
    """Función simple sin parámetros que saluda al usuario"""
    print("¡Hola! Bienvenido al curso de Python")


def saludar_personalizado(nombre):
    """Función con un parámetro"""
    print(f"¡Hola {nombre}! Es un placer verte aquí")


def calcular_area_rectangulo(largo, ancho):
    """Función con múltiples parámetros y retorno"""
    area = largo * ancho
    return area


# Llamando las funciones
saludar()
saludar_personalizado("Carlos")
area = calcular_area_rectangulo(5, 3)
print(f"Área del rectángulo: {area} m²")

# 2. PARÁMETROS POR DEFECTO Y ARGUMENTOS NOMBRADOS
# ------------------------------------------------
print("\n=== PARÁMETROS POR DEFECTO ===")


def crear_usuario(nombre, edad, pais="Colombia", activo=True):
    """Función con parámetros por defecto"""
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "pais": pais,
        "activo": activo
    }
    return usuario


# Diferentes formas de llamar la función
usuario1 = crear_usuario("Ana", 25)  # Usa valores por defecto
usuario2 = crear_usuario("Luis", 30, "México")  # Sobrescribe país
usuario3 = crear_usuario("Maria", 28, activo=False)  # Argumentos nombrados

print(f"Usuario 1: {usuario1}")
print(f"Usuario 2: {usuario2}")
print(f"Usuario 3: {usuario3}")

# 3. FUNCIONES CON NÚMERO VARIABLE DE ARGUMENTOS
# ----------------------------------------------
print("\n=== ARGUMENTOS VARIABLES ===")


def calcular_promedio(*numeros):
    """Función que acepta cualquier número de argumentos"""
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


def crear_perfil(**datos):
    """Función que acepta argumentos de palabras clave variables"""
    perfil = {
        "nombre": datos.get('nombre', 'Desconocido'),
        "edad": datos.get('edad', 0),
        "profesion": datos.get('profesion', 'No especificada'),
        "ciudad": datos.get('ciudad', 'No especificada')
    }
    # Agregar cualquier dato adicional
    for clave, valor in datos.items():
        if clave not in perfil:
            perfil[clave] = valor

    return perfil


# Probando las funciones
promedio1 = calcular_promedio(85, 90, 78, 92)
promedio2 = calcular_promedio(100, 95, 89)

print(f"Promedio 1: {promedio1:.2f}")
print(f"Promedio 2: {promedio2:.2f}")

perfil1 = crear_perfil(nombre="Pedro", edad=35, profesion="Ingeniero")
perfil2 = crear_perfil(nombre="Laura", ciudad="Bogotá", hobby="Pintura")

print(f"Perfil 1: {perfil1}")
print(f"Perfil 2: {perfil2}")

# 4. FUNCIONES QUE RETORNAN MÚLTIPLES VALORES
# -------------------------------------------
print("\n=== MÚLTIPLES VALORES DE RETORNO ===")


def analizar_numeros(lista_numeros):
    """Analiza una lista de números y retorna múltiples estadísticas"""
    if not lista_numeros:
        return None, None, None, None

    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros)
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)

    return suma, promedio, maximo, minimo


def convertir_temperatura(grados_celsius):
    """Convierte temperatura entre Celsius, Fahrenheit y Kelvin"""
    fahrenheit = (grados_celsius * 9 / 5) + 32
    kelvin = grados_celsius + 273.15
    return fahrenheit, kelvin


# Probando las funciones
numeros = [23, 45, 12, 67, 89, 34]
suma_total, prom, max_num, min_num = analizar_numeros(numeros)

print(f"Lista: {numeros}")
print(f"Suma: {suma_total}, Promedio: {prom:.2f}")
print(f"Máximo: {max_num}, Mínimo: {min_num}")

temp_celsius = 25
fahr, kelv = convertir_temperatura(temp_celsius)
print(f"{temp_celsius}°C = {fahr:.2f}°F = {kelv:.2f}K")

# 5. FUNCIONES ANIDADAS Y ALCANCE
# -------------------------------
print("\n=== FUNCIONES ANIDADAS Y ALCANCE ===")


def calculadora_avanzada(operacion, *numeros):
    """Función principal que contiene funciones anidadas"""

    def sumar(*args):
        return sum(args)

    def multiplicar(*args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

    def promedio(*args):
        return sum(args) / len(args) if args else 0

    # Diccionario de operaciones
    operaciones = {
        'suma': sumar,
        'multiplicacion': multiplicar,
        'promedio': promedio
    }

    if operacion in operaciones:
        return operaciones[operacion](*numeros)
    else:
        return "Operación no válida"


# Probando la calculadora
resultado_suma = calculadora_avanzada('suma', 2, 3, 5, 7)
resultado_mult = calculadora_avanzada('multiplicacion', 2, 3, 4)
resultado_prom = calculadora_avanzada('promedio', 10, 20, 30)

print(f"Suma de 2,3,5,7: {resultado_suma}")
print(f"Multiplicación de 2,3,4: {resultado_mult}")
print(f"Promedio de 10,20,30: {resultado_prom}")

# 6. FUNCIONES RECURSIVAS
# -----------------------
print("\n=== FUNCIONES RECURSIVAS ===")


def factorial(n):
    """Calcula el factorial de un número de forma recursiva"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """Genera el n-ésimo número de la secuencia Fibonacci"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def contar_digitos(numero):
    """Cuenta los dígitos de un número de forma recursiva"""
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)


# Probando funciones recursivas
print(f"Factorial de 5: {factorial(5)}")
print(f"Fibonacci posición 7: {fibonacci(7)}")
print(f"Dígitos en 12345: {contar_digitos(12345)}")

# 7. EJEMPLO PRÁCTICO: SISTEMA DE GESTIÓN DE LIBROS
# -------------------------------------------------
print("\n=== SISTEMA DE GESTIÓN DE LIBROS ===")


def crear_biblioteca():
    """Crea una biblioteca vacía"""
    return []


def agregar_libro(biblioteca, titulo, autor, año, genero, leido=False):
    """Agrega un libro a la biblioteca"""
    libro = {
        'titulo': titulo,
        'autor': autor,
        'año': año,
        'genero': genero,
        'leido': leido
    }
    biblioteca.append(libro)
    return f"Libro '{titulo}' agregado exitosamente"


def buscar_libros(biblioteca, criterio, valor):
    """Busca libros por diferentes criterios"""
    resultados = []
    for libro in biblioteca:
        if str(libro.get(criterio, '')).lower() == str(valor).lower():
            resultados.append(libro)
    return resultados


def marcar_como_leido(biblioteca, titulo):
    """Marca un libro como leído"""
    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            libro['leido'] = True
            return f"Libro '{titulo}' marcado como leído"
    return f"Libro '{titulo}' no encontrado"


def estadisticas_biblioteca(biblioteca):
    """Proporciona estadísticas de la biblioteca"""
    total_libros = len(biblioteca)
    libros_leidos = sum(1 for libro in biblioteca if libro['leido'])
    autores_unicos = len(set(libro['autor'] for libro in biblioteca))

    return {
        'total_libros': total_libros,
        'libros_leidos': libros_leidos,
        'libros_por_leer': total_libros - libros_leidos,
        'autores_unicos': autores_unicos,
        'porcentaje_leido': (libros_leidos / total_libros * 100) if total_libros > 0 else 0
    }


# Usando el sistema de biblioteca
mi_biblioteca = crear_biblioteca()

# Agregar libros
agregar_libro(mi_biblioteca, "Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico", True)
agregar_libro(mi_biblioteca, "1984", "George Orwell", 1949, "Ciencia ficción", False)
agregar_libro(mi_biblioteca, "El principito", "Antoine de Saint-Exupéry", 1943, "Fábula", True)

# Buscar libros
resultados = buscar_libros(mi_biblioteca, 'autor', 'Gabriel García Márquez')
print(f"Libros de Gabriel García Márquez: {len(resultados)}")

# Estadísticas
stats = estadisticas_biblioteca(mi_biblioteca)
print(f"Estadísticas de la biblioteca: {stats}")

