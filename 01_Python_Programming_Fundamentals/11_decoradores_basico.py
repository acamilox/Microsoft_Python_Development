"""
Decoradores en Python
Funciones que modifican el comportamiento de otras funciones
"""

# 1. FUNCIONES COMO OBJETOS DE PRIMERA CLASE
# ------------------------------------------
print("=== FUNCIONES COMO OBJETOS DE PRIMERA CLASE ===")


def saludar(nombre):
    """Función simple que saluda"""
    return f"¡Hola {nombre}!"


def despedir(nombre):
    """Función simple que se despide"""
    return f"¡Adiós {nombre}!"


# Las funciones son objetos que se pueden asignar a variables
mi_saludo = saludar
mi_despedida = despedir

print("Funciones como variables:")
print(f"mi_saludo('Ana'): {mi_saludo('Ana')}")
print(f"mi_despedida('Carlos'): {mi_despedida('Carlos')}")


# Las funciones se pueden pasar como argumentos
def ejecutar_funcion(funcion, nombre):
    """Ejecuta una función con un nombre"""
    return funcion(nombre)


print(f"\nEjecutar función: {ejecutar_funcion(saludar, 'María')}")
print(f"Ejecutar función: {ejecutar_funcion(despedir, 'Pedro')}")


# Las funciones se pueden retornar desde otras funciones
def crear_saludo(estilo):
    """Retorna una función de saludo según el estilo"""
    if estilo == "formal":
        def saludo_formal(nombre):
            return f"Buenos días, {nombre}"

        return saludo_formal
    else:
        def saludo_informal(nombre):
            return f"¡Hey {nombre}! ¿Qué tal?"

        return saludo_informal


saludo_formal = crear_saludo("formal")
saludo_informal = crear_saludo("informal")

print(f"\nSaludo formal: {saludo_formal('Señor García')}")
print(f"Saludo informal: {saludo_informal('amigo')}")

# 2. DECORADORES BÁSICOS
# ----------------------
print("\n=== DECORADORES BÁSICOS ===")


def decorador_simple(funcion):
    """Decorador simple que agrega un mensaje antes y después"""

    def wrapper():
        print("🎉 ¡Antes de ejecutar la función!")
        funcion()
        print("✅ ¡Función ejecutada correctamente!")

    return wrapper


@decorador_simple
def mi_funcion():
    """Función decorada"""
    print("📝 Ejecutando la función principal...")


print("Ejecutando función decorada:")
mi_funcion()


# Decorador con argumentos
def decorador_con_argumentos(funcion):
    """Decorador que maneja argumentos"""

    def wrapper(*args, **kwargs):
        print(f"📋 Argumentos recibidos: args={args}, kwargs={kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"📦 Resultado: {resultado}")
        return resultado

    return wrapper


@decorador_con_argumentos
def sumar(a, b):
    """Suma dos números"""
    return a + b


@decorador_con_argumentos
def saludar_personal(nombre, saludo="Hola"):
    """Saluda personalmente"""
    return f"{saludo} {nombre}!"


print(f"\nProbando decorador con argumentos:")
print(f"sumar(5, 3): {sumar(5, 3)}")
print(f"saludar_personal('Ana', saludo='Buenos días'): {saludar_personal('Ana', saludo='Buenos días')}")

# 3. DECORADORES CON ARGUMENTOS PROPIOS
# -------------------------------------
print("\n=== DECORADORES CON ARGUMENTOS PROPIOS ===")


def repetir(n_veces):
    """Decorador que repite la ejecución de una función"""

    def decorador_real(funcion):
        def wrapper(*args, **kwargs):
            resultados = []
            for i in range(n_veces):
                print(f"🔄 Ejecución {i + 1}/{n_veces}")
                resultado = funcion(*args, **kwargs)
                resultados.append(resultado)
            return resultados

        return wrapper

    return decorador_real


@repetir(3)
def saludar_repetido(nombre):
    """Función que será repetida"""
    return f"¡Hola {nombre}!"


print("Función con repetición:")
resultados = saludar_repetido("Mundo")
print(f"Resultados: {resultados}")


def validar_tipo(*tipos_esperados):
    """Decorador que valida los tipos de los argumentos"""

    def decorador(funcion):
        def wrapper(*args, **kwargs):
            # Validar argumentos posicionales
            for i, (arg, tipo_esperado) in enumerate(zip(args, tipos_esperados)):
                if not isinstance(arg, tipo_esperado):
                    raise TypeError(f"Argumento {i} debe ser {tipo_esperado.__name__}, no {type(arg).__name__}")

            # Validar argumentos de palabra clave (simplificado)
            for clave, valor in kwargs.items():
                # Aquí podríamos agregar validación específica por nombre de parámetro
                pass

            return funcion(*args, **kwargs)

        return wrapper

    return decorador


@validar_tipo(int, int)
def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


print(f"\nValidación de tipos:")
try:
    resultado = dividir(10, 2)
    print(f"dividir(10, 2) = {resultado}")

    # Esto generará un error
    # resultado = dividir(10, "2")
    # print(f"dividir(10, '2') = {resultado}")
except TypeError as e:
    print(f"Error de tipo: {e}")

# 4. DECORADORES PRÁCTICOS
# ------------------------
print("\n=== DECORADORES PRÁCTICOS ===")

import time
import math


def medir_tiempo(funcion):
    """Decorador que mide el tiempo de ejecución"""

    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        print(f"⏱️  {funcion.__name__} ejecutado en {duracion:.6f} segundos")
        return resultado

    return wrapper


@medir_tiempo
def calcular_factorial(n):
    """Calcula el factorial de un número"""
    return math.factorial(n)


@medir_tiempo
def esperar_segundos(segundos):
    """Espera la cantidad especificada de segundos"""
    time.sleep(segundos)
    return f"Esperados {segundos} segundos"


print("Medición de tiempo:")
print(f"Factorial de 100: {calcular_factorial(100)}")
print(f"Espera: {esperar_segundos(1)}")


def cache_resultados(funcion):
    """Decorador que cachea los resultados de una función"""
    cache = {}

    def wrapper(*args, **kwargs):
        # Crear una clave única para los argumentos
        clave = str(args) + str(sorted(kwargs.items()))

        if clave not in cache:
            print(f"💾 Calculando nuevo resultado para {funcion.__name__}{args}")
            cache[clave] = funcion(*args, **kwargs)
        else:
            print(f"🚀 Recuperando resultado cacheado para {funcion.__name__}{args}")

        return cache[clave]

    return wrapper


@cache_resultados
@medir_tiempo
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci (ineficiente a propósito)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"\nCache de resultados (Fibonacci):")
print(f"Fibonacci(10) = {fibonacci(10)}")
print(f"Fibonacci(10) = {fibonacci(10)}")  # Esta vez debería usar cache


def reintentar(max_intentos=3, delay=1):
    """Decorador que reintenta una función si falla"""

    def decorador(funcion):
        def wrapper(*args, **kwargs):
            intentos = 0
            while intentos < max_intentos:
                try:
                    return funcion(*args, **kwargs)
                except Exception as e:
                    intentos += 1
                    if intentos == max_intentos:
                        print(f"❌ Todos los intentos fallaron: {e}")
                        raise
                    print(f"⚠️  Intento {intentos} fallado: {e}. Reintentando en {delay} segundos...")
                    time.sleep(delay)
            return None

        return wrapper

    return decorador


@reintentar(max_intentos=3, delay=1)
def conexion_inestable():
    """Simula una conexión inestable que puede fallar"""
    import random
    if random.random() < 0.7:  # 70% de probabilidad de fallo
        raise ConnectionError("Conexión fallida")
    return "Conexión exitosa"


print(f"\nReintentos:")
for i in range(3):
    try:
        resultado = conexion_inestable()
        print(f"Intento {i + 1}: {resultado}")
        break
    except Exception as e:
        print(f"Intento {i + 1}: {e}")

# 5. DECORADORES DE CLASE
# -----------------------
print("\n=== DECORADORES DE CLASE ===")


def agregar_metodos(cls):
    """Decorador de clase que agrega métodos dinámicamente"""

    def to_dict(self):
        """Convierte el objeto a diccionario"""
        return {atributo: valor for atributo, valor in self.__dict__.items()
                if not atributo.startswith('_')}

    def from_dict(cls, datos):
        """Crea una instancia desde un diccionario"""
        instancia = cls.__new__(cls)
        for clave, valor in datos.items():
            setattr(instancia, clave, valor)
        return instancia

    # Agregar métodos a la clase
    cls.to_dict = to_dict
    cls.from_dict = classmethod(from_dict)

    return cls


@agregar_metodos
class Producto:
    """Clase producto con métodos agregados por decorador"""

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"


# Probar la clase decorada
producto = Producto("Laptop", 1200, 15)
print(f"Producto: {producto}")
print(f"Como diccionario: {producto.to_dict()}")

# Crear desde diccionario
datos = {"nombre": "Mouse", "precio": 25, "stock": 50}
producto2 = Producto.from_dict(datos)
print(f"Producto desde dict: {producto2}")


def singleton(cls):
    """Decorador que convierte una clase en singleton"""
    instancias = {}

    def wrapper(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]

    return wrapper


@singleton
class Configuracion:
    """Clase de configuración que debe ser única"""

    def __init__(self):
        self.datos = {
            "servidor": "localhost",
            "puerto": 8080,
            "timeout": 30
        }
        print("🔧 Configuración inicializada")

    def get(self, clave):
        return self.datos.get(clave)


print(f"\nPatrón Singleton:")
config1 = Configuracion()
config2 = Configuracion()

print(f"¿Misma instancia? {config1 is config2}")
print(f"Config1 servidor: {config1.get('servidor')}")
print(f"Config2 puerto: {config2.get('puerto')}")

# 6. DECORADORES CON WRAPS
# ------------------------
print("\n=== DECORADORES CON WRAPS ===")

from functools import wraps


def decorador_con_wraps(funcion):
    """Decorador que preserva los metadatos de la función original"""

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f"📝 Ejecutando {funcion.__name__}")
        return funcion(*args, **kwargs)

    return wrapper


def decorador_sin_wraps(funcion):
    """Decorador que NO preserva los metadatos"""

    def wrapper(*args, **kwargs):
        print(f"📝 Ejecutando {funcion.__name__}")
        return funcion(*args, **kwargs)

    return wrapper


@decorador_con_wraps
def funcion_con_metadatos(nombre):
    """Función que preserva metadatos con wraps"""
    return f"Hola {nombre}"


@decorador_sin_wraps
def funcion_sin_metadatos(nombre):
    """Función que pierde metadatos sin wraps"""
    return f"Hola {nombre}"


print("Preservación de metadatos:")
print(f"Con wraps - nombre: {funcion_con_metadatos.__name__}")
print(f"Con wraps - doc: {funcion_con_metadatos.__doc__}")
print(f"Sin wraps - nombre: {funcion_sin_metadatos.__name__}")
print(f"Sin wraps - doc: {funcion_sin_metadatos.__doc__}")

# 7. EJEMPLO PRÁCTICO: SISTEMA DE LOGGING Y AUTENTICACIÓN
# -------------------------------------------------------
print("\n=== SISTEMA DE LOGGING Y AUTENTICACIÓN ===")


class SistemaAutenticacion:
    """Sistema simple de autenticación"""

    def __init__(self):
        self.usuarios = {
            "admin": "admin123",
            "usuario": "clave123"
        }
        self.sesion_activa = None

    def autenticar(self, usuario, clave):
        """Autentica un usuario"""
        if usuario in self.usuarios and self.usuarios[usuario] == clave:
            self.sesion_activa = usuario
            return True
        return False

    def obtener_usuario_actual(self):
        """Obtiene el usuario actualmente autenticado"""
        return self.sesion_activa


# Crear instancia del sistema
auth_system = SistemaAutenticacion()


def requiere_autenticacion(funcion):
    """Decorador que requiere autenticación"""

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        usuario_actual = auth_system.obtener_usuario_actual()
        if not usuario_actual:
            return "❌ Error: Debes autenticarte primero"

        print(f"🔐 Usuario autenticado: {usuario_actual}")
        return funcion(*args, **kwargs)

    return wrapper


def registrar_log(funcion):
    """Decorador que registra ejecución en log"""

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        usuario = auth_system.obtener_usuario_actual() or "Anónimo"
        print(f"📋 LOG: {usuario} ejecutó {funcion.__name__}")
        return funcion(*args, **kwargs)

    return wrapper


@registrar_log
@requiere_autenticacion
def acceder_datos_sensibles():
    """Accede a datos sensibles (requiere autenticación)"""
    return "🔓 Acceso concedido a datos sensibles"


@registrar_log
def acceder_datos_publicos():
    """Accede a datos públicos"""
    return "📖 Acceso a datos públicos"


# Probar el sistema
print("1. Acceso sin autenticación:")
print(f"   Datos públicos: {acceder_datos_publicos()}")
print(f"   Datos sensibles: {acceder_datos_sensibles()}")

print("\n2. Autenticando usuario...")
if auth_system.autenticar("admin", "admin123"):
    print("   ✅ Autenticación exitosa")

print("\n3. Acceso con autenticación:")
print(f"   Datos sensibles: {acceder_datos_sensibles()}")

# 8. EJEMPLO AVANZADO: SISTEMA DE CACHÉ DISTRIBUIDO
# -------------------------------------------------
print("\n=== SISTEMA DE CACHÉ AVANZADO ===")


class SistemaCache:
    """Sistema de cache avanzado con decoradores"""

    def __init__(self):
        self.cache = {}
        self.estadisticas = {
            'aciertos': 0,
            'fallos': 0,
            'total_llamadas': 0
        }

    def cachear(self, tiempo_vida=60):
        """Decorador para cachear resultados con tiempo de vida"""

        def decorador(funcion):
            @wraps(funcion)
            def wrapper(*args, **kwargs):
                self.estadisticas['total_llamadas'] += 1

                # Crear clave única
                clave = f"{funcion.__name__}_{str(args)}_{str(kwargs)}"
                tiempo_actual = time.time()

                # Verificar si está en cache y no ha expirado
                if (clave in self.cache and
                        tiempo_actual - self.cache[clave]['timestamp'] < tiempo_vida):
                    self.estadisticas['aciertos'] += 1
                    print(f"🚀 Cache HIT para {funcion.__name__}")
                    return self.cache[clave]['resultado']

                # Ejecutar función y guardar en cache
                self.estadisticas['fallos'] += 1
                print(f"💾 Cache MISS para {funcion.__name__}, calculando...")
                resultado = funcion(*args, **kwargs)

                self.cache[clave] = {
                    'resultado': resultado,
                    'timestamp': tiempo_actual,
                    'funcion': funcion.__name__
                }

                return resultado

            return wrapper

        return decorador

    def obtener_estadisticas(self):
        """Obtiene estadísticas del cache"""
        total = self.estadisticas['total_llamadas']
        if total == 0:
            return "Sin llamadas registradas"

        tasa_aciertos = (self.estadisticas['aciertos'] / total) * 100
        return {
            'total_llamadas': total,
            'aciertos': self.estadisticas['aciertos'],
            'fallos': self.estadisticas['fallos'],
            'tasa_aciertos': f"{tasa_aciertos:.1f}%",
            'items_en_cache': len(self.cache)
        }


# Crear sistema de cache
sistema_cache = SistemaCache()


@sistema_cache.cachear(tiempo_vida=2)  # Cache por 2 segundos
@medir_tiempo
def operacion_costosa(n):
    """Simula una operación computacionalmente costosa"""
    time.sleep(0.5)  # Simular procesamiento
    return sum(i ** 2 for i in range(n))


print("Sistema de cache avanzado:")
print("Primeras ejecuciones (deberían ser MISS):")
for i in range(3):
    resultado = operacion_costosa(1000)
    print(f"   Resultado {i + 1}: {resultado}")

print("\nEjecuciones inmediatas (deberían ser HIT):")
for i in range(2):
    resultado = operacion_costosa(1000)
    print(f"   Resultado {i + 1}: {resultado}")

print("\nEsperando 3 segundos para que expire el cache...")
time.sleep(3)

print("Ejecución después de expiración (debería ser MISS):")
resultado = operacion_costosa(1000)
print(f"   Resultado: {resultado}")

# Mostrar estadísticas
print(f"\nEstadísticas del cache:")
stats = sistema_cache.obtener_estadisticas()
for clave, valor in stats.items():
    print(f"   {clave}: {valor}")

print("\n" + "=" * 60)
print("¡Decoradores demostrados exitosamente!")
