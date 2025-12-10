"""
Comprensiones en Python
List, dict y set comprehensions para creación eficiente de colecciones
"""

# 1. LIST COMPREHENSIONS BÁSICAS
# ------------------------------
print("=== LIST COMPREHENSIONS BÁSICAS ===")

# Crear lista de cuadrados (forma tradicional vs comprehension)
print("1. CUADRADOS DE NÚMEROS:")

# Forma tradicional
cuadrados_tradicional = []
for i in range(1, 11):
    cuadrados_tradicional.append(i ** 2)

# Forma con list comprehension
cuadrados_comprehension = [i ** 2 for i in range(1, 11)]

print(f"Tradicional: {cuadrados_tradicional}")
print(f"Comprehension: {cuadrados_comprehension}")

# Crear lista de números pares
print("\n2. NÚMEROS PARES:")
pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"Números pares del 1 al 20: {pares}")

# Transformar lista de strings
print("\n3. TRANSFORMACIÓN DE STRINGS:")
nombres = ["ana", "carlos", "maria", "pedro"]
nombres_mayusculas = [nombre.upper() for nombre in nombres]
nombres_longitud = [len(nombre) for nombre in nombres]

print(f"Nombres originales: {nombres}")
print(f"En mayúsculas: {nombros_mayusculas}")
print(f"Longitudes: {nombres_longitud}")

# 2. LIST COMPREHENSIONS CON CONDICIONALES
# ----------------------------------------
print("\n=== LIST COMPREHENSIONS CON CONDICIONALES ===")

# Filtrar y transformar
numeros = list(range(1, 16))
print(f"Números del 1 al 15: {numeros}")

# Números pares al cuadrado, impares al cubo
transformados = [x ** 2 if x % 2 == 0 else x ** 3 for x in numeros]
print(f"Pares al cuadrado, impares al cubo: {transformados}")

# Clasificar números
clasificacion = ["par" if x % 2 == 0 else "impar" for x in numeros]
print(f"Clasificación par/impar: {clasificacion}")

# Múltiples condiciones
numeros_filtrados = [
    x for x in range(1, 31)
    if x % 2 == 0
    if x % 3 == 0
    if x > 10
]
print(f"Números pares, múltiplos de 3 y mayores que 10: {numeros_filtrados}")

# 3. LIST COMPREHENSIONS ANIDADAS
# -------------------------------
print("\n=== LIST COMPREHENSIONS ANIDADAS ===")

# Tabla de multiplicar
tabla_multiplicar = [[i * j for j in range(1, 6)] for i in range(1, 4)]
print("Tabla de multiplicar (3x5):")
for i, fila in enumerate(tabla_multiplicar, 1):
    print(f"  {i}: {fila}")

# Aplanar lista de listas
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_plana = [numero for sublista in lista_anidada for numero in sublista]
print(f"\nLista anidada: {lista_anidada}")
print(f"Lista plana: {lista_plana}")

# Producto cartesiano
colores = ["rojo", "verde", "azul"]
tamaños = ["S", "M", "L"]
combinaciones = [(color, tamaño) for color in colores for tamaño in tamaños]
print(f"\nCombinaciones colores-tamaños: {combinaciones}")

# 4. DICTIONARY COMPREHENSIONS
# ----------------------------
print("\n=== DICTIONARY COMPREHENSIONS ===")

# Crear diccionario de cuadrados
cuadrados_dict = {x: x ** 2 for x in range(1, 11)}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

# Transformar diccionario existente
precios_original = {"manzana": 1.5, "banana": 0.8, "naranja": 1.2, "uva": 2.5}
precios_con_iva = {fruta: precio * 1.19 for fruta, precio in precios_original.items()}
print(f"\nPrecios originales: {precios_original}")
print(f"Precios con IVA (19%): {precios_con_iva}")

# Filtrar diccionario
productos_caros = {fruta: precio for fruta, precio in precios_original.items() if precio > 1.0}
print(f"Productos caros (>$1.0): {productos_caros}")

# Invertir clave-valor
invertido = {precio: fruta for fruta, precio in precios_original.items()}
print(f"Diccionario invertido: {invertido}")

# 5. SET COMPREHENSIONS
# ---------------------
print("\n=== SET COMPREHENSIONS ===")

# Crear set de cuadrados
cuadrados_set = {x ** 2 for x in range(1, 11)}
print(f"Set de cuadrados: {cuadrados_set}")

# Eliminar duplicados y transformar
palabras = ["python", "java", "python", "c", "java", "javascript"]
longitudes_unicas = {len(palabra) for palabra in palabras}
print(f"Palabras: {palabras}")
print(f"Longitudes únicas: {longitudes_unicas}")

# Filtrar y transformar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10]
pares_unicos = {x for x in numeros if x % 2 == 0}
print(f"Números: {numeros}")
print(f"Pares únicos: {pares_unicos}")

# 6. COMPREHENSIONS ANIDADAS MIXTAS
# ---------------------------------
print("\n=== COMPREHENSIONS ANIDADAS MIXTAS ===")

# Lista de diccionarios
estudiantes = [
    {"nombre": "Ana", "notas": [85, 90, 78]},
    {"nombre": "Carlos", "notas": [92, 88, 95]},
    {"nombre": "Maria", "notas": [76, 85, 80]},
    {"nombre": "Pedro", "notas": [65, 70, 72]}
]

# Promedio de cada estudiante
promedios = {est["nombre"]: sum(est["notas"]) / len(est["notas"]) for est in estudiantes}
print(f"Promedios de estudiantes: {promedios}")

# Todas las notas en una lista plana
todas_las_notas = [nota for est in estudiantes for nota in est["notas"]]
print(f"Todas las notas: {todas_las_notas}")

# Estudiantes con promedio mayor a 85
excelentes_estudiantes = [est["nombre"] for est in estudiantes if sum(est["notas"]) / len(est["notas"]) > 85]
print(f"Estudiantes excelentes (>85): {excelentes_estudiantes}")

# 7. EJEMPLOS PRÁCTICOS AVANZADOS
# -------------------------------
print("\n=== EJEMPLOS PRÁCTICOS AVANZADOS ===")

# Procesamiento de texto
texto = """
Python es un lenguaje de programación interpretado cuya filosofía 
hace hincapié en la legibilidad de su código. Se trata de un 
lenguaje de programación multiparadigma, ya que soporta 
orientación a objetos, programación imperativa y, en menor 
medida, programación funcional.
"""

# Estadísticas del texto
palabras = texto.lower().split()
estadisticas = {
    'total_palabras': len(palabras),
    'palabras_unicas': len({palabra for palabra in palabras}),
    'longitud_promedio': sum(len(palabra) for palabra in palabras) / len(palabras),
    'palabra_mas_larga': max(palabras, key=len),
    'frecuencia_letras': {letra: texto.lower().count(letra) for letra in set(texto.lower()) if letra.isalpha()}
}

print("Estadísticas del texto:")
for clave, valor in estadisticas.items():
    if clave != 'frecuencia_letras':
        print(f"  {clave}: {valor}")

print("  Frecuencia de letras (primeras 10):")
letras_ordenadas = sorted(estadisticas['frecuencia_letras'].items(), key=lambda x: x[1], reverse=True)
for letra, freq in letras_ordenadas[:10]:
    print(f"    {letra}: {freq}")

# 8. SISTEMA DE GESTIÓN DE INVENTARIO
# -----------------------------------
print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")


class SistemaInventario:
    """Sistema de gestión de inventario usando comprehensions"""

    def __init__(self):
        self.productos = [
            {"id": 1, "nombre": "Laptop", "categoria": "tecnologia", "precio": 1200, "stock": 15},
            {"id": 2, "nombre": "Mouse", "categoria": "tecnologia", "precio": 25, "stock": 50},
            {"id": 3, "nombre": "Libro Python", "categoria": "educacion", "precio": 45, "stock": 30},
            {"id": 4, "nombre": "Silla", "categoria": "oficina", "precio": 150, "stock": 20},
            {"id": 5, "nombre": "Monitor", "categoria": "tecnologia", "precio": 300, "stock": 8},
            {"id": 6, "nombre": "Teclado", "categoria": "tecnologia", "precio": 80, "stock": 25},
            {"id": 7, "nombre": "Escritorio", "categoria": "oficina", "precio": 200, "stock": 12}
        ]

    def productos_por_categoria(self, categoria):
        """Filtra productos por categoría"""
        return [p for p in self.productos if p["categoria"] == categoria]

    def productos_bajo_stock(self, limite=10):
        """Encuentra productos con stock bajo"""
        return [p for p in self.productos if p["stock"] < limite]

    def aplicar_descuento(self, categoria, porcentaje):
        """Aplica descuento a productos de una categoría"""
        return [
            {**p, "precio_descuento": p["precio"] * (1 - porcentaje / 100)}
            for p in self.productos
            if p["categoria"] == categoria
        ]

    def valor_inventario_por_categoria(self):
        """Calcula el valor del inventario por categoría"""
        categorias = {p["categoria"] for p in self.productos}
        return {
            categoria: sum(p["precio"] * p["stock"] for p in self.productos if p["categoria"] == categoria)
            for categoria in categorias
        }

    def estadisticas_categoria(self, categoria):
        """Estadísticas detalladas por categoría"""
        productos_categoria = self.productos_por_categoria(categoria)
        if not productos_categoria:
            return {}

        return {
            'total_productos': len(productos_categoria),
            'precio_promedio': sum(p["precio"] for p in productos_categoria) / len(productos_categoria),
            'stock_total': sum(p["stock"] for p in productos_categoria),
            'producto_mas_caro': max(productos_categoria, key=lambda x: x["precio"]),
            'producto_menos_stock': min(productos_categoria, key=lambda x: x["stock"])
        }


# Usar el sistema de inventario
inventario = SistemaInventario()

print("1. PRODUCTOS DE TECNOLOGÍA:")
tech_productos = inventario.productos_por_categoria("tecnologia")
for p in tech_productos:
    print(f"  - {p['nombre']}: ${p['precio']} (Stock: {p['stock']})")

print("\n2. PRODUCTOS CON STOCK BAJO (<15):")
bajo_stock = inventario.productos_bajo_stock(15)
for p in bajo_stock:
    print(f"  - {p['nombre']}: Stock {p['stock']}")

print("\n3. DESCUENTO DEL 20% EN TECNOLOGÍA:")
con_descuento = inventario.aplicar_descuento("tecnologia", 20)
for p in con_descuento:
    print(f"  - {p['nombre']}: ${p['precio']} → ${p['precio_descuento']:.2f}")

print("\n4. VALOR DEL INVENTARIO POR CATEGORÍA:")
valor_por_categoria = inventario.valor_inventario_por_categoria()
for categoria, valor in valor_por_categoria.items():
    print(f"  - {categoria}: ${valor:,.2f}")

print("\n5. ESTADÍSTICAS DE CATEGORÍA 'tecnologia':")
stats_tech = inventario.estadisticas_categoria("tecnologia")
for clave, valor in stats_tech.items():
    if clave in ['producto_mas_caro', 'producto_menos_stock']:
        print(f"  - {clave}: {valor['nombre']} (${valor['precio']})")
    else:
        print(f"  - {clave}: {valor}")

# 9. COMPREHENSIONS CON FUNCIONES
# -------------------------------
print("\n=== COMPREHENSIONS CON FUNCIONES ===")


def es_primo(n):
    """Verifica si un número es primo"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Lista de números primos
primos = [x for x in range(2, 101) if es_primo(x)]
print(f"Números primos del 1 al 100: {primos}")

# Diccionario de números y si son primos
primos_dict = {x: es_primo(x) for x in range(1, 21)}
print(f"¿Es primo? (1-20): {primos_dict}")

# 10. EJEMPLO COMPLEJO: ANALIZADOR DE DATOS
# -----------------------------------------
print("\n=== ANALIZADOR DE DATOS CON COMPREHENSIONS ===")

# Datos de ventas simulados
ventas = [
    {"producto": "Laptop", "vendedor": "Ana", "mes": "Enero", "ventas": 5, "region": "Norte"},
    {"producto": "Mouse", "vendedor": "Ana", "mes": "Enero", "ventas": 20, "region": "Norte"},
    {"producto": "Laptop", "vendedor": "Carlos", "mes": "Enero", "ventas": 3, "region": "Sur"},
    {"producto": "Teclado", "vendedor": "Carlos", "mes": "Enero", "ventas": 15, "region": "Sur"},
    {"producto": "Laptop", "vendedor": "Ana", "mes": "Febrero", "ventas": 7, "region": "Norte"},
    {"producto": "Monitor", "vendedor": "Maria", "mes": "Febrero", "ventas": 4, "region": "Este"},
    {"producto": "Mouse", "vendedor": "Carlos", "mes": "Febrero", "ventas": 25, "region": "Sur"},
    {"producto": "Teclado", "vendedor": "Maria", "mes": "Febrero", "ventas": 12, "region": "Este"},
]

print("ANÁLISIS DE VENTAS:")

# Ventas totales por producto
ventas_por_producto = {
    producto: sum(v["ventas"] for v in ventas if v["producto"] == producto)
    for producto in {v["producto"] for v in ventas}
}
print(f"\n1. VENTAS TOTALES POR PRODUCTO:")
for producto, total in sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True):
    print(f"   {producto}: {total} unidades")

# Ventas por vendedor
ventas_por_vendedor = {
    vendedor: sum(v["ventas"] for v in ventas if v["vendedor"] == vendedor)
    for vendedor in {v["vendedor"] for v in ventas}
}
print(f"\n2. VENTAS TOTALES POR VENDEDOR:")
for vendedor, total in sorted(ventas_por_vendedor.items(), key=lambda x: x[1], reverse=True):
    print(f"   {vendedor}: {total} unidades")

# Productos vendidos por región
productos_por_region = {
    region: {v["producto"] for v in ventas if v["region"] == region}
    for region in {v["region"] for v in ventas}
}
print(f"\n3. PRODUCTOS VENDIDOS POR REGIÓN:")
for region, productos in productos_por_region.items():
    print(f"   {region}: {', '.join(sorted(productos))}")

# Mejor vendedor por producto
mejor_vendedor_por_producto = {}
for producto in {v["producto"] for v in ventas}:
    ventas_producto = [v for v in ventas if v["producto"] == producto]
    mejor = max(ventas_producto, key=lambda x: x["ventas"])
    mejor_vendedor_por_producto[producto] = (mejor["vendedor"], mejor["ventas"])

print(f"\n4. MEJOR VENDEDOR POR PRODUCTO:")
for producto, (vendedor, ventas) in mejor_vendedor_por_producto.items():
    print(f"   {producto}: {vendedor} ({ventas} unidades)")

# Resumen mensual
resumen_mensual = {
    mes: {
        "total_ventas": sum(v["ventas"] for v in ventas if v["mes"] == mes),
        "productos_vendidos": len({v["producto"] for v in ventas if v["mes"] == mes}),
        "vendedores_activos": len({v["vendedor"] for v in ventas if v["mes"] == mes})
    }
    for mes in {v["mes"] for v in ventas}
}

print(f"\n5. RESUMEN MENSUAL:")
for mes, datos in resumen_mensual.items():
    print(f"   {mes}:")
    print(f"     Total ventas: {datos['total_ventas']} unidades")
    print(f"     Productos vendidos: {datos['productos_vendidos']}")
    print(f"     Vendedores activos: {datos['vendedores_activos']}")

print("\n" + "=" * 60)
print("¡Comprensiones demostradas exitosamente!")