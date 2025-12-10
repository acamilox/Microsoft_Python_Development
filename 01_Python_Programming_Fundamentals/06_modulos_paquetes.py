"""
Módulos y Paquetes en Python
Importación, creación y uso de módulos propios
"""

# 1. IMPORTACIÓN DE MÓDULOS ESTÁNDAR
# ----------------------------------
print("=== MÓDULOS ESTÁNDAR ===")

import math
import random
import datetime
import os
from collections import Counter, defaultdict

# Usando el módulo math
print("=== MÓDULO MATH ===")
radio = 5
area_circulo = math.pi * math.pow(radio, 2)
circunferencia = 2 * math.pi * radio

print(f"Radio: {radio}")
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Circunferencia: {circunferencia:.2f}")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Factorial de 5: {math.factorial(5)}")

# Usando el módulo random
print("\n=== MÓDULO RANDOM ===")
numeros_aleatorios = [random.randint(1, 100) for _ in range(5)]
eleccion_aleatoria = random.choice(['rojo', 'verde', 'azul', 'amarillo'])

print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Color aleatorio: {eleccion_aleatoria}")
print(f"Decimal aleatorio: {random.uniform(1.0, 10.0):.2f}")

# Usando el módulo datetime
print("\n=== MÓDULO DATETIME ===")
ahora = datetime.datetime.now()
fecha_actual = datetime.date.today()
dentro_de_una_semana = ahora + datetime.timedelta(days=7)

print(f"Fecha y hora actual: {ahora}")
print(f"Fecha actual: {fecha_actual}")
print(f"Dentro de una semana: {dentro_de_una_semana}")
print(f"Año actual: {ahora.year}")
print(f"Día de la semana: {ahora.strftime('%A')}")

# 2. IMPORTACIONES ESPECÍFICAS Y ALIAS
# ------------------------------------
print("\n=== IMPORTACIONES CON ALIAS ===")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Ejemplo con numpy (simulado ya que no tenemos la librería instalada aquí)
def ejemplo_numpy():
    """Simula operaciones con numpy"""
    print("Operaciones similares a NumPy:")
    # En la práctica sería: array = np.array([1, 2, 3, 4, 5])
    array = [1, 2, 3, 4, 5]
    print(f"Array: {array}")
    print(f"Suma: {sum(array)}")
    print(f"Promedio: {sum(array) / len(array)}")


ejemplo_numpy()

# 3. CREACIÓN DE NUESTROS PROPIOS MÓDULOS
# ---------------------------------------
print("\n=== MÓDULOS PERSONALIZADOS ===")


# Vamos a crear funciones que simularían estar en módulos separados

# Módulo: calculos.py (simulado)
def calcular_iva(precio, tasa_iva=0.19):
    """Calcula el IVA de un precio"""
    return precio * tasa_iva


def aplicar_descuento(precio, porcentaje_descuento):
    """Aplica un descuento a un precio"""
    return precio * (1 - porcentaje_descuento / 100)


# Módulo: texto_utils.py (simulado)
def contar_palabras(texto):
    """Cuenta las palabras en un texto"""
    palabras = texto.split()
    return len(palabras)


def invertir_texto(texto):
    """Invierte un texto"""
    return texto[::-1]


def capitalizar_frases(texto):
    """Capitaliza la primera letra de cada oración"""
    oraciones = texto.split('. ')
    oraciones_capitalizadas = [oracion.capitalize() for oracion in oraciones]
    return '. '.join(oraciones_capitalizadas)


# Usando nuestros módulos "importados"
print("=== USANDO MÓDULOS PERSONALIZADOS ===")

precio_producto = 100000
iva = calcular_iva(precio_producto)
precio_con_descuento = aplicar_descuento(precio_producto, 15)

print(f"Precio original: ${precio_producto:,.0f}")
print(f"IVA (19%): ${iva:,.0f}")
print(f"Precio con 15% descuento: ${precio_con_descuento:,.0f}")

texto_ejemplo = "python es un lenguaje de programación. es muy versátil y poderoso."
print(f"\nTexto original: {texto_ejemplo}")
print(f"Palabras: {contar_palabras(texto_ejemplo)}")
print(f"Texto invertido: {invertir_texto(texto_ejemplo)}")
print(f"Texto capitalizado: {capitalizar_frases(texto_ejemplo)}")

# 4. SISTEMA DE PAQUETES
# ----------------------
print("\n=== SISTEMA DE PAQUETES ===")


# Simulando una estructura de paquetes
class PaqueteMatematicas:
    """Simula un paquete de funciones matemáticas"""

    @staticmethod
    def estadisticas_basicas(numeros):
        """Calcula estadísticas básicas de una lista de números"""
        if not numeros:
            return {}

        return {
            'suma': sum(numeros),
            'promedio': sum(numeros) / len(numeros),
            'maximo': max(numeros),
            'minimo': min(numeros),
            'rango': max(numeros) - min(numeros)
        }

    @staticmethod
    def geometria():
        """Proporciona funciones geométricas"""

        class Geometria:
            @staticmethod
            def area_rectangulo(largo, ancho):
                return largo * ancho

            @staticmethod
            def area_circulo(radio):
                return math.pi * radio ** 2

            @staticmethod
            def volumen_esfera(radio):
                return (4 / 3) * math.pi * radio ** 3

        return Geometria


# Usando nuestro "paquete" matemático
matematicas = PaqueteMatematicas()
geometria = matematicas.geometria()

numeros = [23, 45, 12, 67, 89, 34]
stats = matematicas.estadisticas_basicas(numeros)

print(f"Estadísticas de {numeros}:")
for clave, valor in stats.items():
    print(f"  {clave}: {valor:.2f}")

print(f"\nÁrea rectángulo 5x3: {geometria.area_rectangulo(5, 3)}")
print(f"Área círculo radio 4: {geometria.area_circulo(4):.2f}")
print(f"Volumen esfera radio 3: {geometria.volumen_esfera(3):.2f}")

# 5. EJEMPLO PRÁCTICO: SISTEMA DE GESTIÓN DE ESTUDIANTES
# -------------------------------------------------------
print("\n=== SISTEMA DE GESTIÓN DE ESTUDIANTES ===")


class ModuloEstudiantes:
    """Módulo para gestionar estudiantes"""

    estudiantes = []

    @classmethod
    def agregar_estudiante(cls, nombre, edad, carrera, promedio):
        """Agrega un nuevo estudiante"""
        estudiante = {
            'id': len(cls.estudiantes) + 1,
            'nombre': nombre,
            'edad': edad,
            'carrera': carrera,
            'promedio': promedio
        }
        cls.estudiantes.append(estudiante)
        return estudiante

    @classmethod
    def buscar_estudiante(cls, criterio, valor):
        """Busca estudiantes por diferentes criterios"""
        resultados = []
        for estudiante in cls.estudiantes:
            if str(estudiante.get(criterio, '')).lower() == str(valor).lower():
                resultados.append(estudiante)
        return resultados

    @classmethod
    def obtener_estadisticas(cls):
        """Obtiene estadísticas de los estudiantes"""
        if not cls.estudiantes:
            return {}

        promedios = [est['promedio'] for est in cls.estudiantes]
        edades = [est['edad'] for est in cls.estudiantes]

        return {
            'total_estudiantes': len(cls.estudiantes),
            'promedio_general': sum(promedios) / len(promedios),
            'mejor_promedio': max(promedios),
            'peor_promedio': min(promedios),
            'edad_promedio': sum(edades) / len(edades),
            'carreras_unicas': len(set(est['carrera'] for est in cls.estudiantes))
        }


class ModuloNotas:
    """Módulo para gestionar calificaciones"""

    @staticmethod
    def calcular_calificacion_letra(promedio):
        """Convierte promedio numérico a calificación con letra"""
        if promedio >= 90:
            return 'A'
        elif promedio >= 80:
            return 'B'
        elif promedio >= 70:
            return 'C'
        elif promedio >= 60:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def evaluar_rendimiento(estudiante):
        """Evalúa el rendimiento de un estudiante"""
        promedio = estudiante['promedio']
        calificacion = ModuloNotas.calcular_calificacion_letra(promedio)

        if calificacion in ['A', 'B']:
            estado = "Excelente rendimiento"
        elif calificacion == 'C':
            estado = "Rendimiento satisfactorio"
        elif calificacion == 'D':
            estado = "Necesita mejorar"
        else:
            estado = "Rendimiento insuficiente"

        return {
            'estudiante': estudiante['nombre'],
            'promedio': promedio,
            'calificacion': calificacion,
            'estado': estado
        }


# Usando nuestro sistema de gestión
print("=== GESTIÓN DE ESTUDIANTES ===")

# Agregar estudiantes
ModuloEstudiantes.agregar_estudiante("Ana García", 22, "Ingeniería", 92.5)
ModuloEstudiantes.agregar_estudiante("Carlos López", 21, "Medicina", 88.0)
ModuloEstudiantes.agregar_estudiante("María Rodríguez", 23, "Derecho", 76.5)
ModuloEstudiantes.agregar_estudiante("Pedro Martínez", 20, "Ingeniería", 65.0)

# Buscar estudiantes
estudiantes_ingenieria = ModuloEstudiantes.buscar_estudiante('carrera', 'Ingeniería')
print("Estudiantes de Ingeniería:")
for est in estudiantes_ingenieria:
    print(f"  - {est['nombre']} (Promedio: {est['promedio']})")

# Obtener estadísticas
stats = ModuloEstudiantes.obtener_estadisticas()
print(f"\nEstadísticas del sistema:")
for clave, valor in stats.items():
    print(f"  {clave}: {valor}")

# Evaluar rendimiento
print(f"\nEvaluación de rendimiento:")
for estudiante in ModuloEstudiantes.estudiantes:
    evaluacion = ModuloNotas.evaluar_rendimiento(estudiante)
    print(f"  {evaluacion['estudiante']}: {evaluacion['calificacion']} - {evaluacion['estado']}")

# 6. IMPORTACIÓN CONDICIONAL
# --------------------------
print("\n=== IMPORTACIÓN CONDICIONAL ===")


def verificar_modulos():
    """Verifica qué módulos están disponibles"""
    modulos_disponibles = []
    modulos_no_disponibles = []

    # Lista de módulos a verificar
    modulos_a_verificar = ['numpy', 'pandas', 'matplotlib', 'requests', 'tkinter']

    for modulo in modulos_a_verificar:
        try:
            __import__(modulo)
            modulos_disponibles.append(modulo)
        except ImportError:
            modulos_no_disponibles.append(modulo)

    print(f"Módulos disponibles: {modulos_disponibles}")
    print(f"Módulos no disponibles: {modulos_no_disponibles}")

    return modulos_disponibles, modulos_no_disponibles


# Ejecutar verificación
disponibles, no_disponibles = verificar_modulos()

# 7. EJECUCIÓN COMO SCRIPT vs MÓDULO
# -----------------------------------
print("\n=== EJECUCIÓN COMO SCRIPT ===")

if __name__ == "__main__":
    print("Este archivo se está ejecutando como script principal")
    print("Puedo incluir código de prueba o demostración aquí")


    # Código que solo se ejecuta cuando el archivo es el principal
    def demostracion():
        print("¡Demostración del sistema de módulos!")
        print(f"Total de estudiantes: {len(ModuloEstudiantes.estudiantes)}")


    demostracion()
else:
    print("Este archivo se está importando como módulo")

print("\n" + "=" * 50)
print("¡Sistema de módulos demostrado exitosamente!")

