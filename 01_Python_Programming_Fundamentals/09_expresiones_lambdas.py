"""
Expresiones Lambda en Python
Funciones anónimas y programación funcional
"""

# 1. INTRODUCCIÓN A LAS EXPRESIONES LAMBDA
# -----------------------------------------
print("=== EXPRESIONES LAMBDA BÁSICAS ===")


# Función normal vs lambda
def cuadrado_normal(x):
    return x ** 2


cuadrado_lambda = lambda x: x ** 2

print("Función normal vs lambda:")
print(f"cuadrado_normal(5) = {cuadrado_normal(5)}")
print(f"cuadrado_lambda(5) = {cuadrado_lambda(5)}")

# Lambdas con múltiples parámetros
suma = lambda a, b: a + b
multiplicacion = lambda x, y, z: x * y * z

print(f"\nsuma(3, 7) = {suma(3, 7)}")
print(f"multiplicacion(2, 3, 4) = {multiplicacion(2, 3, 4)}")

# Lambdas sin parámetros
saludo = lambda: "¡Hola Mundo!"
hora_actual = lambda: __import__('datetime').datetime.now().strftime("%H:%M:%S")

print(f"\nsaludo() = {saludo()}")
print(f"hora_actual() = {hora_actual()}")

# 2. LAMBDAS CON CONDICIONALES
# ----------------------------
print("\n=== LAMBDAS CON CONDICIONALES ===")

# Clasificar números
clasificar_numero = lambda x: "positivo" if x > 0 else "negativo" if x < 0 else "cero"

# Determinar si es par o impar
par_impar = lambda x: "par" if x % 2 == 0 else "impar"

# Calcular descuento
calcular_precio = lambda precio, descuento: precio * (1 - descuento / 100) if descuento > 0 else precio

print("Clasificación de números:")
numeros = [5, -3, 0, 10, -7]
for num in numeros:
    print(f"  {num} es {clasificar_numero(num)} y {par_impar(num)}")

print(f"\nPrecio con descuento:")
print(f"  $100 con 20% descuento: ${calcular_precio(100, 20):.2f}")
print(f"  $50 sin descuento: ${calcular_precio(50, 0):.2f}")

# 3. LAMBDAS CON FUNCIONES DE ORDEN SUPERIOR
# ------------------------------------------
print("\n=== LAMBDAS CON MAP() ===")

# Transformar lista con map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
cubos = list(map(lambda x: x ** 3, numeros))

print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")
print(f"Cubos: {cubos}")

# Aplicar a strings
nombres = ["ana", "carlos", "maria", "pedro"]
nombres_mayusculas = list(map(lambda x: x.upper(), nombres))
nombres_capitalizados = list(map(lambda x: x.capitalize(), nombres))

print(f"\nNombres originales: {nombres}")
print(f"En mayúsculas: {nombres_mayusculas}")
print(f"Capitalizados: {nombres_capitalizados}")

print("\n=== LAMBDAS CON FILTER() ===")

# Filtrar números pares
numeros = list(range(1, 11))
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 != 0, numeros))
mayores_que_5 = list(filter(lambda x: x > 5, numeros))

print(f"Números del 1 al 10: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Mayores que 5: {mayores_que_5}")

# Filtrar strings
palabras = ["python", "java", "c", "javascript", "go", "rust"]
largas = list(filter(lambda x: len(x) > 4, palabras))
con_a = list(filter(lambda x: 'a' in x.lower(), palabras))

print(f"\nPalabras: {palabras}")
print(f"Palabras largas (>4 letras): {largas}")
print(f"Palabras con 'a': {con_a}")

print("\n=== LAMBDAS CON REDUCE() ===")
from functools import reduce

# Operaciones con reduce
numeros = [1, 2, 3, 4, 5]

suma_total = reduce(lambda x, y: x + y, numeros)
producto_total = reduce(lambda x, y: x * y, numeros)
maximo = reduce(lambda x, y: x if x > y else y, numeros)

print(f"Lista: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Producto total: {producto_total}")
print(f"Máximo: {maximo}")

# 4. LAMBDAS CON SORTED()
# -----------------------
print("\n=== LAMBDAS CON SORTED() ===")

# Ordenar listas simples
numeros = [45, 12, 78, 23, 56, 89, 34]
print(f"Números originales: {numeros}")
print(f"Ordenados: {sorted(numeros)}")
print(f"Ordenados descendente: {sorted(numeros, reverse=True)}")

# Ordenar por criterios personalizados
palabras = ["python", "java", "c", "javascript", "go", "rust"]
print(f"\nPalabras originales: {palabras}")
print(f"Ordenadas por longitud: {sorted(palabras, key=lambda x: len(x))}")
print(f"Ordenadas por última letra: {sorted(palabras, key=lambda x: x[-1])}")

# Ordenar lista de diccionarios
estudiantes = [
    {"nombre": "Ana", "edad": 22, "promedio": 8.5},
    {"nombre": "Carlos", "edad": 21, "promedio": 7.8},
    {"nombre": "María", "edad": 23, "promedio": 9.2},
    {"nombre": "Pedro", "edad": 20, "promedio": 8.9}
]

print(f"\nEstudiantes ordenados por edad:")
for est in sorted(estudiantes, key=lambda x: x['edad']):
    print(f"  {est['nombre']} - {est['edad']} años")

print(f"\nEstudiantes ordenados por promedio (descendente):")
for est in sorted(estudiantes, key=lambda x: x['promedio'], reverse=True):
    print(f"  {est['nombre']} - {est['promedio']}")

# 5. LAMBDAS EN COMPRENSIONES DE LISTAS
# -------------------------------------
print("\n=== LAMBDAS EN COMPRENSIONES ===")

# Aplicar lambda en comprensión
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando lambda con map en comprensión
transformados = [(lambda x: x ** 2 if x % 2 == 0 else x ** 3)(x) for x in numeros]
print(f"Números transformados: {transformados}")

# Filtrar y transformar
resultado_complejo = [
    (lambda x: f"{x}-PAR" if x % 2 == 0 else f"{x}-IMPAR")(x)
    for x in numeros
    if x > 5
]
print(f"Resultado complejo: {resultado_complejo}")

# 6. EJEMPLOS PRÁCTICOS AVANZADOS
# -------------------------------
print("\n=== EJEMPLOS PRÁCTICOS AVANZADOS ===")

# Calculadora con lambdas
calculadora = {
    'suma': lambda x, y: x + y,
    'resta': lambda x, y: x - y,
    'multiplicacion': lambda x, y: x * y,
    'division': lambda x, y: x / y if y != 0 else "Error: División por cero",
    'potencia': lambda x, y: x ** y,
    'modulo': lambda x, y: x % y if y != 0 else "Error: Módulo por cero"
}

print("Calculadora con lambdas:")
a, b = 10, 3
for operacion, funcion in calculadora.items():
    resultado = funcion(a, b)
    print(f"  {operacion}({a}, {b}) = {resultado}")

# Procesador de texto con lambdas
procesador_texto = {
    'mayusculas': lambda s: s.upper(),
    'minusculas': lambda s: s.lower(),
    'capitalizar': lambda s: s.capitalize(),
    'invertir': lambda s: s[::-1],
    'contar_vocales': lambda s: sum(1 for c in s.lower() if c in 'aeiouáéíóú'),
    'es_palindromo': lambda s: s.lower().replace(' ', '') == s.lower().replace(' ', '')[::-1]
}

texto = "Anita lava la tina"
print(f"\nProcesador de texto - Texto: '{texto}'")
for proceso, funcion in procesador_texto.items():
    resultado = funcion(texto)
    print(f"  {proceso}: {resultado}")

# 7. LAMBDAS EN PROGRAMACIÓN FUNCIONAL
# ------------------------------------
print("\n=== PROGRAMACIÓN FUNCIONAL CON LAMBDAS ===")


def pipeline(*funciones):
    """Crea un pipeline de funciones"""
    return lambda data: reduce(lambda x, f: f(x), funciones, data)


# Pipeline de procesamiento de datos
procesamiento_datos = pipeline(
    lambda x: x * 2,  # Duplicar
    lambda x: x + 10,  # Sumar 10
    lambda x: x ** 2,  # Elevar al cuadrado
    lambda x: f"Resultado: {x}"  # Formatear
)

resultado = procesamiento_datos(5)
print(f"Pipeline(5) = {resultado}")

# Pipeline de procesamiento de texto
procesamiento_texto = pipeline(
    lambda s: s.strip(),  # Quitar espacios
    lambda s: s.upper(),  # A mayúsculas
    lambda s: s.replace(' ', '_'),  # Reemplazar espacios
    lambda s: f"@{s}"  # Agregar @
)

texto_procesado = procesamiento_texto("  hola mundo python  ")
print(f"Pipeline texto = {texto_procesado}")

# 8. EJEMPLO PRÁCTICO: SISTEMA DE FILTRADO Y TRANSFORMACIÓN
# ---------------------------------------------------------
print("\n=== SISTEMA DE FILTRADO Y TRANSFORMACIÓN ===")


class ProcesadorDatos:
    """Sistema para procesar datos usando programación funcional"""

    def __init__(self, datos):
        self.datos = datos

    def aplicar_filtros(self, *filtros):
        """Aplica múltiples filtros a los datos"""
        datos_filtrados = self.datos

        for filtro in filtros:
            datos_filtrados = list(filter(filtro, datos_filtrados))

        return ProcesadorDatos(datos_filtrados)

    def aplicar_transformaciones(self, *transformaciones):
        """Aplica múltiples transformaciones a los datos"""
        datos_transformados = self.datos

        for transformacion in transformaciones:
            datos_transformados = list(map(transformacion, datos_transformados))

        return ProcesadorDatos(datos_transformados)

    def reducir(self, funcion_reduccion, valor_inicial=None):
        """Aplica una reducción a los datos"""
        if valor_inicial is not None:
            return reduce(funcion_reduccion, self.datos, valor_inicial)
        else:
            return reduce(funcion_reduccion, self.datos)

    def mostrar(self, limite=None):
        """Muestra los datos"""
        datos_mostrar = self.datos[:limite] if limite else self.datos
        print(f"Datos: {datos_mostrar}")
        return self


# Datos de ejemplo
productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "tecnologia", "stock": 15},
    {"nombre": "Mouse", "precio": 25, "categoria": "tecnologia", "stock": 50},
    {"nombre": "Libro", "precio": 15, "categoria": "educacion", "stock": 100},
    {"nombre": "Silla", "precio": 150, "categoria": "oficina", "stock": 20},
    {"nombre": "Monitor", "precio": 300, "categoria": "tecnologia", "stock": 10},
    {"nombre": "Teclado", "precio": 45, "categoria": "tecnologia", "stock": 30},
    {"nombre": "Mesa", "precio": 200, "categoria": "oficina", "stock": 5}
]

print("PROCESAMIENTO DE PRODUCTOS:")

# Crear procesador
procesador = ProcesadorDatos(productos)

print("\n1. PRODUCTOS ORIGINALES:")
procesador.mostrar()

print("\n2. FILTRAR PRODUCTOS DE TECNOLOGÍA:")
tecnologia = procesador.aplicar_filtros(
    lambda p: p['categoria'] == 'tecnologia'
).mostrar()

print("\n3. FILTRAR PRODUCTOS CAROS Y CON STOCK:")
caros_con_stock = procesador.aplicar_filtros(
    lambda p: p['precio'] > 50,
    lambda p: p['stock'] > 10
).mostrar()

print("\n4. APLICAR DESCUENTO DEL 20% A TECNOLOGÍA:")
con_descuento = procesador.aplicar_filtros(
    lambda p: p['categoria'] == 'tecnologia'
).aplicar_transformaciones(
    lambda p: {**p, 'precio': p['precio'] * 0.8, 'con_descuento': True}
).mostrar()

print("\n5. CALCULAR VALOR TOTAL DEL INVENTARIO:")
valor_total = procesador.reducir(
    lambda total, p: total + (p['precio'] * p['stock']), 0
)
print(f"Valor total del inventario: ${valor_total:,.2f}")

print("\n6. PRODUCTOS MÁS CAROS POR CATEGORÍA:")
from itertools import groupby

# Agrupar por categoría y encontrar el más caro
productos_ordenados = sorted(productos, key=lambda x: x['categoria'])
por_categoria = groupby(productos_ordenados, key=lambda x: x['categoria'])

for categoria, grupo in por_categoria:
    productos_grupo = list(grupo)
    mas_caro = max(productos_grupo, key=lambda x: x['precio'])
    print(f"  {categoria}: {mas_caro['nombre']} - ${mas_caro['precio']}")

# 9. LAMBDAS EN INTERFACES GRÁFICAS (SIMULACIÓN)
# ----------------------------------------------
print("\n=== LAMBDAS EN INTERFACES GRÁFICAS (SIMULACIÓN) ===")


class SimuladorEventos:
    """Simula un sistema de manejo de eventos como en interfaces gráficas"""

    def __init__(self):
        self.event_handlers = {}

    def registrar_evento(self, evento, handler):
        """Registra un manejador de eventos"""
        if evento not in self.event_handlers:
            self.event_handlers[evento] = []
        self.event_handlers[evento].append(handler)

    def disparar_evento(self, evento, *args, **kwargs):
        """Dispara un evento y ejecuta todos sus manejadores"""
        if evento in self.event_handlers:
            for handler in self.event_handlers[evento]:
                resultado = handler(*args, **kwargs)
                print(f"  Evento '{evento}': {resultado}")
        else:
            print(f"  Evento '{evento}' sin manejadores registrados")

    def simular_interfaz(self):
        """Simula una interfaz con diferentes eventos"""
        print("Simulando interfaz de usuario...")

        # Simular clicks de botón
        self.disparar_evento('click_boton', 'btn_guardar')
        self.disparar_evento('click_boton', 'btn_cancelar')

        # Simular entrada de texto
        self.disparar_evento('cambio_texto', 'campo_nombre', 'Juan Pérez')
        self.disparar_evento('cambio_texto', 'campo_email', 'juan@email.com')

        # Simular movimiento de mouse
        self.disparar_evento('mouse_mover', 150, 200)
        self.disparar_evento('mouse_click', 300, 400, 'izquierdo')


# Configurar simulador
simulador = SimuladorEventos()

# Registrar manejadores de eventos con lambdas
simulador.registrar_evento('click_boton',
                           lambda
                               boton: f"Botón '{boton}' clickeado - Guardando datos..." if 'guardar' in boton else f"Botón '{boton}' clickeado")

simulador.registrar_evento('cambio_texto',
                           lambda campo, valor: f"Campo '{campo}' actualizado: '{valor}'")

simulador.registrar_evento('mouse_mover',
                           lambda x, y: f"Mouse movido a posición ({x}, {y})")

simulador.registrar_evento('mouse_click',
                           lambda x, y, boton: f"Click {boton} en ({x}, {y})")

# Ejecutar simulación
simulador.simular_interfaz()

print("\n" + "=" * 60)
print("¡Expresiones lambda demostradas exitosamente!")