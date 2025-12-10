"""
Gestión de Memoria en Python
Understanding memory management, garbage collection, and optimization
"""

import sys
import gc
import tracemalloc
from memory_profiler import profile
import weakref

# 1. VISUALIZACIÓN DEL USO DE MEMORIA
# -----------------------------------
print("=== VISUALIZACIÓN DEL USO DE MEMORIA ===")


def mostrar_info_objeto(objeto, nombre=""):
    """Muestra información de memoria de un objeto"""
    tamaño = sys.getsizeof(objeto)
    tipo_objeto = type(objeto).__name__

    print(f"{nombre:15} | Tipo: {tipo_objeto:10} | Tamaño: {tamaño:6} bytes | ID: {id(objeto)}")


print("1. TAMAÑOS DE OBJETOS BÁSICOS:")
mostrar_info_objeto(10, "Entero")
mostrar_info_objeto(3.14159, "Float")
mostrar_info_objeto("Hola", "String corto")
mostrar_info_objeto("Este es un string muy largo para ver la diferencia", "String largo")
mostrar_info_objeto([1, 2, 3, 4, 5], "Lista pequeña")
mostrar_info_objeto(list(range(1000)), "Lista grande")
mostrar_info_objeto({"clave": "valor"}, "Diccionario")

# 2. GARBAGE COLLECTION
# ---------------------
print("\n=== GARBAGE COLLECTION ===")


class ReferenciaCircular:
    """Clase para demostrar referencias circulares"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.otro = None

    def __repr__(self):
        return f"ReferenciaCircular('{self.nombre}')"

    def __del__(self):
        print(f"🔓 Destructor llamado para {self.nombre}")


def demostrar_garbage_collection():
    """Demuestra el funcionamiento del garbage collector"""
    print("1. CREANDO REFERENCIAS CIRCULARES:")

    # Crear referencias circulares
    obj1 = ReferenciaCircular("Objeto 1")
    obj2 = ReferenciaCircular("Objeto 2")
    obj3 = ReferenciaCircular("Objeto 3")

    # Crear referencias circulares
    obj1.otro = obj2
    obj2.otro = obj3
    obj3.otro = obj1

    print(f"   Objetos creados: {obj1}, {obj2}, {obj3}")

    # Mostrar conteo de referencias
    print(f"\n2. CONTEO DE REFERENCIAS:")
    print(f"   Referencias a obj1: {sys.getrefcount(obj1) - 1}")  # -1 porque getrefcount agrega una referencia temporal
    print(f"   Referencias a obj2: {sys.getrefcount(obj2) - 1}")
    print(f"   Referencias a obj3: {sys.getrefcount(obj3) - 1}")

    # Mostrar objetos rastreados por GC
    print(f"\n3. OBJETOS RASTREADOS POR GC:")
    objetos_rastreados = gc.get_objects()
    print(f"   Total objetos rastreados: {len(objetos_rastreados)}")

    # Buscar nuestros objetos en GC
    nuestros_objetos = [obj for obj in objetos_rastreados if isinstance(obj, ReferenciaCircular)]
    print(f"   Nuestros objetos en GC: {len(nuestros_objetos)}")

    # Forzar garbage collection
    print(f"\n4. EJECUTANDO GARBAGE COLLECTION:")
    recolectados = gc.collect()
    print(f"   Objetos recolectados: {recolectados}")

    # Configurar y mostrar configuración de GC
    print(f"\n5. CONFIGURACIÓN DE GC:")
    print(f"   GC habilitado: {gc.isenabled()}")
    print(f"   Umbrales: {gc.get_threshold()}")
    print(f"   Conteos: {gc.get_count()}")


# Ejecutar demostración
demostrar_garbage_collection()

# 3. WEAK REFERENCES
# ------------------
print("\n=== WEAK REFERENCES ===")


def demostrar_weak_references():
    """Demuestra el uso de referencias débiles"""

    class RecursoCostoso:
        """Simula un recurso que consume mucha memoria"""

        def __init__(self, nombre):
            self.nombre = nombre
            self.datos = list(range(10000))  # Datos "pesados"
            print(f"🔄 RecursoCostoso '{self.nombre}' creado")

        def __del__(self):
            print(f"🗑️  RecursoCostoso '{self.nombre}' destruido")

    print("1. REFERENCIA FUERTE (normal):")
    recurso_fuerte = RecursoCostoso("Fuerte")
    print(f"   Referencias: {sys.getrefcount(recurso_fuerte) - 1}")

    print("\n2. REFERENCIA DÉBIL:")
    recurso_debil = RecursoCostoso("Débil")
    referencia_debil = weakref.ref(recurso_debil)

    print(f"   Referencia débil válida: {referencia_debil() is not None}")
    print(f"   Accediendo a través de referencia débil: {referencia_debil().nombre}")

    # Eliminar referencia fuerte
    print("\n3. ELIMINANDO REFERENCIA FUERTE:")
    del recurso_debil

    print(f"   Referencia débil válida: {referencia_debil() is not None}")

    print("\n4. WEAK VALUE DICTIONARY:")
    weak_dict = weakref.WeakValueDictionary()

    recurso1 = RecursoCostoso("Para WeakDict 1")
    recurso2 = RecursoCostoso("Para WeakDict 2")

    weak_dict['recurso1'] = recurso1
    weak_dict['recurso2'] = recurso2

    print(f"   Elementos en weak_dict: {list(weak_dict.keys())}")

    # Eliminar referencias fuertes
    del recurso1
    del recurso2

    # Ejecutar GC para limpiar inmediatamente
    gc.collect()

    print(f"   Elementos en weak_dict después de eliminar referencias: {list(weak_dict.keys())}")


# Ejecutar demostración
demostrar_weak_references()

# 4. PROFILING DE MEMORIA
# -----------------------
print("\n=== PROFILING DE MEMORIA ===")


# Función para demostrar uso de memoria
@profile
def funcion_intensiva_memoria():
    """Función que usa mucha memoria intencionalmente"""
    print("Ejecutando función intensiva en memoria...")

    # Crear estructuras de datos grandes
    lista_grande = list(range(100000))
    diccionario_grande = {i: f"valor_{i}" for i in range(50000)}
    matriz = [[i * j for j in range(1000)] for i in range(100)]

    # Realizar algunas operaciones
    resultado = sum(lista_grande)
    valores = [v for v in diccionario_grande.values()]

    # Liberar algunas referencias
    del matriz
    del diccionario_grande

    return resultado


# Ejecutar función con profiling (comentado para evitar output extenso)
# print("Ejecutando función con memory profiler...")
# funcion_intensiva_memoria()

# 5. TRACEMALLOC PARA DETECTAR FUGA DE MEMORIA
# --------------------------------------------
print("\n=== DETECCIÓN DE FUGAS DE MEMORIA ===")


def demostrar_tracemalloc():
    """Demuestra el uso de tracemalloc para detectar fugas de memoria"""

    print("1. INICIANDO TRACEMALLOC:")
    tracemalloc.start()

    # Tomar snapshot inicial
    snapshot1 = tracemalloc.take_snapshot()

    def crear_fuga_memoria():
        """Función que crea una fuga de memoria intencional"""
        datos_fugados = []

        for i in range(1000):
            # Crear datos que no se liberan
            datos = list(range(1000))
            datos_fugados.append(datos)

        return datos_fugados

    def uso_normal_memoria():
        """Función que usa memoria de forma normal"""
        datos_temporales = []

        for i in range(1000):
            datos = list(range(1000))
            datos_temporales.append(datos)

        # Liberar memoria correctamente
        datos_temporales.clear()
        return len(datos_temporales)

    print("2. EJECUTANDO FUNCIONES:")
    # Ejecutar función con fuga
    fuga = crear_fuga_memoria()
    print(f"   Fuga creada: {len(fuga)} listas en memoria")

    # Ejecutar función normal
    resultado_normal = uso_normal_memoria()
    print(f"   Uso normal: {resultado_normal}")

    # Tomar snapshot final
    snapshot2 = tracemalloc.take_snapshot()

    print("\n3. COMPARANDO SNAPSHOTS:")
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')

    print("   Cambios más significativos en memoria:")
    for stat in top_stats[:5]:  # Mostrar solo los top 5
        print(f"   {stat}")

    # Detener tracemalloc
    tracemalloc.stop()


# Ejecutar demostración
demostrar_tracemalloc()

# 6. OPTIMIZACIÓN DE MEMORIA
# --------------------------
print("\n=== OPTIMIZACIÓN DE MEMORIA ===")


def demostrar_optimizacion():
    """Demuestra técnicas de optimización de memoria"""

    print("1. USO DE __SLOTS__:")

    class ClaseNormal:
        """Clase normal sin optimización"""

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    class ClaseOptimizada:
        """Clase optimizada usando __slots__"""

        __slots__ = ['x', 'y', 'z']

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    # Crear instancias
    normal = ClaseNormal(1, 2, 3)
    optimizada = ClaseOptimizada(1, 2, 3)

    print(f"   Tamaño ClaseNormal: {sys.getsizeof(normal)} bytes")
    print(f"   Tamaño ClaseOptimizada: {sys.getsizeof(optimizada)} bytes")

    # Verificar que no se pueden agregar atributos dinámicos a la clase optimizada
    try:
        optimizada.nuevo_atributo = 10
    except AttributeError as e:
        print(f"   Error esperado al agregar atributo: {e}")

    print("\n2. COMPRESIÓN DE DATOS:")

    # Lista normal vs generador
    lista_numeros = list(range(1000000))
    generador_numeros = (x for x in range(1000000))

    print(f"   Tamaño lista: {sys.getsizeof(lista_numeros):,} bytes")
    print(f"   Tamaño generador: {sys.getsizeof(generador_numeros):,} bytes")

    print("\n3. USO DE ARRAYS PARA DATOS NUMÉRICOS:")
    import array

    # Lista normal vs array
    lista_enteros = [i for i in range(1000)]
    array_enteros = array.array('i', lista_enteros)  # 'i' para integers

    print(f"   Tamaño lista enteros: {sys.getsizeof(lista_enteros)} bytes")
    print(f"   Tamaño array enteros: {sys.getsizeof(array_enteros)} bytes")

    print("\n4. MEMORYVIEWS PARA BUFFERS:")

    # Crear array y memoryview
    datos = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])  # 'd' para doubles
    vista_memoria = memoryview(datos)

    print(f"   Array original: {datos}")
    print(f"   Memoryview: {vista_memoria}")
    print(f"   Tamaño array: {sys.getsizeof(datos)} bytes")
    print(f"   Tamaño memoryview: {sys.getsizeof(vista_memoria)} bytes")

    # Modificar a través de memoryview
    vista_memoria[0] = 99.0
    print(f"   Array después de modificar memoryview: {datos}")


# Ejecutar demostración
demostrar_optimizacion()

# 7. EJEMPLO PRÁCTICO: CACHÉ INTELIGENTE
# ---------------------------------------
print("\n=== CACHÉ INTELIGENTE CON GESTIÓN DE MEMORIA ===")


class CacheInteligente:
    """
    Sistema de cache que monitorea el uso de memoria
    y limpia automáticamente cuando es necesario
    """

    def __init__(self, max_memoria_mb=10):
        self.max_memoria_bytes = max_memoria_mb * 1024 * 1024
        self.cache = {}
        self.estadisticas = {
            'aciertos': 0,
            'fallos': 0,
            'limpiezas_automaticas': 0
        }

    def _calcular_memoria_actual(self):
        """Calcula la memoria total usada por el cache"""
        return sum(sys.getsizeof(key) + sys.getsizeof(value)
                   for key, value in self.cache.items())

    def _limpiar_cache_si_es_necesario(self):
        """Limpia el cache si se excede el límite de memoria"""
        memoria_actual = self._calcular_memoria_actual()

        if memoria_actual > self.max_memoria_bytes:
            print(f"⚠️  Memoria cache: {memoria_actual / (1024 * 1024):.2f} MB - Limpiando...")

            # Eliminar elementos más antiguos (simplificado)
            elementos_a_eliminar = len(self.cache) // 2  # Eliminar la mitad
            claves_a_eliminar = list(self.cache.keys())[:elementos_a_eliminar]

            for clave in claves_a_eliminar:
                del self.cache[clave]

            self.estadisticas['limpiezas_automaticas'] += 1
            print(f"   Elementos eliminados: {elementos_a_eliminar}")

    def obtener(self, clave):
        """Obtiene un valor del cache"""
        if clave in self.cache:
            self.estadisticas['aciertos'] += 1
            return self.cache[clave]
        else:
            self.estadisticas['fallos'] += 1
            return None

    def guardar(self, clave, valor):
        """Guarda un valor en el cache"""
        self.cache[clave] = valor
        self._limpiar_cache_si_es_necesario()

    def obtener_estadisticas(self):
        """Obtiene estadísticas del cache"""
        memoria_actual = self._calcular_memoria_actual()
        total_operaciones = self.estadisticas['aciertos'] + self.estadisticas['fallos']
        tasa_aciertos = (self.estadisticas['aciertos'] / total_operaciones * 100) if total_operaciones > 0 else 0

        return {
            'elementos_en_cache': len(self.cache),
            'memoria_actual_mb': memoria_actual / (1024 * 1024),
            'tasa_aciertos': f"{tasa_aciertos:.1f}%",
            'limpiezas_automaticas': self.estadisticas['limpiezas_automaticas']
        }


# Probar el cache inteligente
print("Probando cache inteligente...")
cache = CacheInteligente(max_memoria_mb=1)  # Límite bajo para demostración

# Llenar el cache con datos
for i in range(1000):
    clave = f"clave_{i}"
    valor = list(range(1000))  # Valor que ocupa memoria
    cache.guardar(clave, valor)

    if i % 100 == 0:
        stats = cache.obtener_estadisticas()
        print(f"  Iteración {i}: {stats['elementos_en_cache']} elementos, "
              f"{stats['memoria_actual_mb']:.2f} MB")

# Mostrar estadísticas finales
print("\nEstadísticas finales del cache:")
stats_finales = cache.obtener_estadisticas()
for clave, valor in stats_finales.items():
    print(f"  {clave}: {valor}")

# 8. MONITOREO EN TIEMPO REAL
# ---------------------------
print("\n=== MONITOREO EN TIEMPO REAL ===")


def monitor_sistema():
    """Monitorea el uso de memoria del sistema en tiempo real"""

    import psutil
    import os

    proceso = psutil.Process(os.getpid())

    print("Monitoreo de memoria del proceso:")
    print(f"  Memoria RSS: {proceso.memory_info().rss / (1024 * 1024):.2f} MB")
    print(f"  Memoria VMS: {proceso.memory_info().vms / (1024 * 1024):.2f} MB")
    print(f"  Porcentaje de memoria: {proceso.memory_percent():.2f}%")

    print("\nMemoria del sistema:")
    memoria_sistema = psutil.virtual_memory()
    print(f"  Total: {memoria_sistema.total / (1024 ** 3):.2f} GB")
    print(f"  Disponible: {memoria_sistema.available / (1024 ** 3):.2f} GB")
    print(f"  Usado: {memoria_sistema.used / (1024 ** 3):.2f} GB")
    print(f"  Porcentaje: {memoria_sistema.percent}%")


# Ejecutar monitor (comentado si no se tiene psutil instalado)
try:
    monitor_sistema()
except ImportError:
    print("⚠️  psutil no está instalado. Instala con: pip install psutil")

print("\n" + "=" * 60)
print("¡Gestión de memoria demostrada exitosamente!")
print("\nRESUMEN DE TÉCNICAS:")
print("1. Use __slots__ para clases con muchos objetos")
print("2. Prefiera generadores sobre listas para datos grandes")
print("3. Use arrays para datos numéricos homogéneos")
print("4. Monitoree fugas con tracemalloc")
print("5. Use weak references para cache de objetos grandes")
print("6. Configure garbage collection thresholds apropiadamente")

