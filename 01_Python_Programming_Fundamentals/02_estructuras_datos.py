"""
Estructuras de Datos en Python
Listas, tuplas, diccionarios y conjuntos
"""

# 1. LISTAS - Mutables y ordenadas
# --------------------------------
print("=== LISTAS ===")

# Creación de listas
frutas = ["manzana", "banana", "naranja", "uva"]
numeros = [1, 2, 3, 4, 5]
mezclada = [1, "hola", 3.14, True]

print(f"Frutas: {frutas}")
print(f"Números: {numeros}")
print(f"Lista mezclada: {mezclada}")

# Operaciones con listas
frutas.append("kiwi")  # Agregar elemento
frutas.insert(1, "fresa")  # Insertar en posición
eliminado = frutas.pop()  # Eliminar último elemento

print(f"\nDespués de operaciones: {frutas}")
print(f"Elemento eliminado: {eliminado}")

# Slicing (rebanado)
primeras_dos = frutas[:2]
ultimas_tres = frutas[-3:]
sub_lista = frutas[1:4]

print(f"Primeras dos: {primeras_dos}")
print(f"Últimas tres: {ultimas_tres}")
print(f"Sub-lista [1:4]: {sub_lista}")

# 2. TUPLAS - Inmutables y ordenadas
# ----------------------------------
print("\n=== TUPLAS ===")

coordenadas = (40.7128, -74.0060)  # Coordenadas de NYC
colores_rgb = (255, 0, 0)  # Rojo
persona = ("Carlos", 30, "Ingeniero")

print(f"Coordenadas NYC: {coordenadas}")
print(f"Color RGB rojo: {colores_rgb}")
print(f"Datos persona: {persona}")

# Las tuplas son inmutables
# coordenadas[0] = 50.0  # Esto daría error

# Desempaquetado de tuplas
latitud, longitud = coordenadas
rojo, verde, azul = colores_rgb

print(f"Latitud: {latitud}, Longitud: {longitud}")
print(f"Rojo: {rojo}, Verde: {verde}, Azul: {azul}")

# 3. DICCIONARIOS - Pares clave-valor
# -----------------------------------
print("\n=== DICCIONARIOS ===")

# Creación de diccionarios
estudiante = {
    "nombre": "María López",
    "edad": 22,
    "carrera": "Informática",
    "promedio": 8.5
}

producto = {
    "id": 12345,
    "nombre": "Laptop",
    "precio": 899.99,
    "stock": 15
}

print(f"Estudiante: {estudiante}")
print(f"Producto: {producto}")

# Acceso y modificación
print(f"Nombre del estudiante: {estudiante['nombre']}")
estudiante["semestre"] = 5  # Agregar nueva clave
estudiante["promedio"] = 8.7  # Modificar valor existente

print(f"Estudiante actualizado: {estudiante}")

# Métodos útiles
claves = estudiante.keys()
valores = estudiante.values()
pares = estudiante.items()

print(f"Claves: {list(claves)}")
print(f"Valores: {list(valores)}")
print(f"Pares clave-valor: {list(pares)}")

# 4. CONJUNTOS - Elementos únicos no ordenados
# --------------------------------------------
print("\n=== CONJUNTOS ===")

conjunto_numeros = {1, 2, 3, 4, 5, 5, 4}  # Los duplicados se eliminan
vocales = {'a', 'e', 'i', 'o', 'u'}
frutas_set = set(["manzana", "banana", "naranja", "manzana"])

print(f"Conjunto números: {conjunto_numeros}")
print(f"Vocales: {vocales}")
print(f"Frutas (set): {frutas_set}")

# Operaciones de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B  # Unión
interseccion = A & B  # Intersección
diferencia = A - B  # Diferencia

print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"Unión A|B: {union}")
print(f"Intersección A&B: {interseccion}")
print(f"Diferencia A-B: {diferencia}")

# 5. EJEMPLO PRÁCTICO: SISTEMA DE INVENTARIO
# ------------------------------------------
print("\n=== SISTEMA DE INVENTARIO ===")

inventario = [
    {"id": 1, "nombre": "Mouse", "precio": 25.99, "cantidad": 50},
    {"id": 2, "nombre": "Teclado", "precio": 45.50, "cantidad": 30},
    {"id": 3, "nombre": "Monitor", "precio": 199.99, "cantidad": 15}
]

# Calcular valor total del inventario
valor_total = sum(item["precio"] * item["cantidad"] for item in inventario)

print("Inventario actual:")
for producto in inventario:
    print(f"  {producto['nombre']}: {producto['cantidad']} unidades - ${producto['precio']} c/u")

print(f"Valor total del inventario: ${valor_total:.2f}")

# Buscar producto por ID
def buscar_producto(id_buscar):
    for producto in inventario:
        if producto["id"] == id_buscar:
            return producto
    return None

producto_encontrado = buscar_producto(2)
if producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado['nombre']}")