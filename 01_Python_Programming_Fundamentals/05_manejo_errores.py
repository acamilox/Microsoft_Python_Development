"""
Manejo de Errores en Python
Try, except, finally y creación de excepciones personalizadas
"""

# 1. MANEJO BÁSICO DE EXCEPCIONES
# -------------------------------
print("=== MANEJO BÁSICO DE EXCEPCIONES ===")


def dividir_numeros(a, b):
    """Función que divide dos números con manejo de errores"""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero"
    except TypeError:
        return "Error: Los argumentos deben ser números"


# Probando la función con diferentes casos
print(f"10 / 2 = {dividir_numeros(10, 2)}")
print(f"10 / 0 = {dividir_numeros(10, 0)}")
print(f"10 / 'a' = {dividir_numeros(10, 'a')}")

# 2. MÚLTIPLES EXCEPCIONES
# ------------------------
print("\n=== MÚLTIPLES EXCEPCIONES ===")


def procesar_entrada_usuario(entrada):
    """Procesa entrada del usuario con manejo de múltiples excepciones"""
    try:
        numero = float(entrada)
        inverso = 1 / numero
        cuadrado = numero ** 2

        return {
            'numero': numero,
            'inverso': inverso,
            'cuadrado': cuadrado
        }

    except ValueError:
        return "Error: La entrada debe ser un número válido"
    except ZeroDivisionError:
        return "Error: No se puede calcular el inverso de cero"
    except Exception as e:
        return f"Error inesperado: {type(e).__name__} - {str(e)}"


# Probando con diferentes entradas
entradas_prueba = ["25", "0", "abc", "3.14", "-5"]

for entrada in entradas_prueba:
    resultado = procesar_entrada_usuario(entrada)
    print(f"Entrada: '{entrada}' -> Resultado: {resultado}")

# 3. BLOQUES ELSE Y FINALLY
# -------------------------
print("\n=== BLOQUES ELSE Y FINALLY ===")


def leer_archivo_simple(nombre_archivo):
    """Intenta leer un archivo usando else y finally"""
    try:
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
        return None
    except PermissionError:
        print(f"Error: No tienes permisos para leer '{nombre_archivo}'")
        return None
    else:
        # Este bloque se ejecuta solo si no hubo excepciones
        contenido = archivo.read()
        archivo.close()
        print(f"Archivo '{nombre_archivo}' leído exitosamente")
        return contenido
    finally:
        # Este bloque SIEMPRE se ejecuta
        print(f"Operación con '{nombre_archivo}' completada\n")


# Probando la función (algunos archivos pueden no existir)
leer_archivo_simple("archivo_existente.txt")  # Cambiar por archivo real
leer_archivo_simple("archivo_inexistente.txt")

# 4. LEVANTAR EXCEPCIONES MANUALMENTE
# -----------------------------------
print("=== LEVANTAR EXCEPCIONES ===")


def calcular_edad(año_nacimiento):
    """Calcula la edad y valida el año de nacimiento"""
    año_actual = 2024

    if año_nacimiento > año_actual:
        raise ValueError("El año de nacimiento no puede ser en el futuro")
    elif año_nacimiento < 1900:
        raise ValueError("El año de nacimiento parece ser inválido (muy antiguo)")

    return año_actual - año_nacimiento


def verificar_contraseña(contraseña):
    """Verifica que una contraseña cumpla con requisitos mínimos"""
    if len(contraseña) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")
    if not any(c.isdigit() for c in contraseña):
        raise ValueError("La contraseña debe contener al menos un número")
    if not any(c.isalpha() for c in contraseña):
        raise ValueError("La contraseña debe contener al menos una letra")

    return "Contraseña válida"


# Probando las funciones con manejo de errores
años_prueba = [1990, 2025, 1850, 2000]

for año in años_prueba:
    try:
        edad = calcular_edad(año)
        print(f"Año {año}: Edad = {edad}")
    except ValueError as e:
        print(f"Año {año}: Error - {e}")

contraseñas_prueba = ["abc123", "contraseñalarga", "Contraseña123", "12345678"]

for contraseña in contraseñas_prueba:
    try:
        resultado = verificar_contraseña(contraseña)
        print(f"Contraseña '{contraseña}': {resultado}")
    except ValueError as e:
        print(f"Contraseña '{contraseña}': Error - {e}")

# 5. EXCEPCIONES PERSONALIZADAS
# -----------------------------
print("\n=== EXCEPCIONES PERSONALIZADAS ===")


class SaldoInsuficienteError(Exception):
    """Excepción personalizada para saldo insuficiente"""

    def __init__(self, saldo_actual, monto_retiro):
        self.saldo_actual = saldo_actual
        self.monto_retiro = monto_retiro
        self.falta = monto_retiro - saldo_actual
        super().__init__(f"Saldo insuficiente. Tienes ${saldo_actual}, necesitas ${self.falta} más")


class CuentaBancaria:
    """Clase que representa una cuenta bancaria con manejo de errores"""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        """Deposita dinero en la cuenta"""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo")
        self.saldo += monto
        print(f"Depositado ${monto}. Nuevo saldo: ${self.saldo}")

    def retirar(self, monto):
        """Retira dinero de la cuenta"""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo")
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)

        self.saldo -= monto
        print(f"Retirado ${monto}. Nuevo saldo: ${self.saldo}")

    def transferir(self, otra_cuenta, monto):
        """Transfiere dinero a otra cuenta"""
        try:
            self.retirar(monto)
            otra_cuenta.depositar(monto)
            print(f"Transferencia exitosa de ${monto} a {otra_cuenta.titular}")
        except (ValueError, SaldoInsuficienteError) as e:
            print(f"Error en transferencia: {e}")


# Probando el sistema bancario
cuenta1 = CuentaBancaria("Juan Pérez", 1000)
cuenta2 = CuentaBancaria("María García", 500)

try:
    cuenta1.depositar(200)
    cuenta1.retirar(300)
    cuenta1.retirar(1000)  # Esto generará error
except SaldoInsuficienteError as e:
    print(f"Error bancario: {e}")

try:
    cuenta1.transferir(cuenta2, 200)
    cuenta1.transferir(cuenta2, 2000)  # Esto generará error
except Exception as e:
    print(f"Error en transferencia: {e}")

# 6. CONTEXT MANAGERS (with)
# --------------------------
print("\n=== CONTEXT MANAGERS ===")


class GestorArchivo:
    """Context manager personalizado para manejar archivos"""

    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None

    def __enter__(self):
        """Se ejecuta al entrar al bloque with"""
        self.archivo = open(self.nombre_archivo, self.modo, encoding='utf-8')
        print(f"Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'")
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Se ejecuta al salir del bloque with"""
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado")

        if exc_type is not None:
            print(f"Ocurrió un error: {exc_type.__name__} - {exc_val}")
            # Retornar True para suprimir la excepción, False para propagarla
            return False

        return True


# Usando el context manager personalizado
try:
    with GestorArchivo("ejemplo.txt", "w") as archivo:
        archivo.write("Línea 1: Hola mundo\n")
        archivo.write("Línea 2: Python es genial\n")
        # Simular un error
        # resultado = 10 / 0

    with GestorArchivo("ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print(f"Contenido del archivo:\n{contenido}")

except Exception as e:
    print(f"Error general: {e}")

# 7. EJEMPLO PRÁCTICO: VALIDACIÓN DE DATOS DE USUARIO
# ---------------------------------------------------
print("\n=== VALIDACIÓN DE DATOS DE USUARIO ===")


class ValidacionError(Exception):
    """Excepción base para errores de validación"""
    pass


class EmailInvalidoError(ValidacionError):
    """Error para emails inválidos"""
    pass


class EdadInvalidaError(ValidacionError):
    """Error para edades inválidas"""
    pass


def validar_usuario(nombre, email, edad):
    """
    Valida los datos de un usuario y levanta excepciones personalizadas
    si hay errores
    """
    errores = []

    # Validar nombre
    if not nombre or len(nombre.strip()) < 2:
        errores.append("El nombre debe tener al menos 2 caracteres")

    # Validar email
    if not email or '@' not in email or '.' not in email:
        raise EmailInvalidoError("El formato del email es inválido")

    # Validar edad
    try:
        edad_num = int(edad)
        if edad_num < 0 or edad_num > 120:
            raise EdadInvalidaError("La edad debe estar entre 0 y 120 años")
    except ValueError:
        raise EdadInvalidaError("La edad debe ser un número válido")

    if errores:
        raise ValidacionError("; ".join(errores))

    return {
        'nombre': nombre.strip(),
        'email': email.lower(),
        'edad': edad_num,
        'estado': 'validado'
    }


# Probando el sistema de validación
usuarios_prueba = [
    ("Ana", "ana@email.com", "25"),
    ("A", "anaemail.com", "25"),  # Nombre corto y email inválido
    ("Carlos", "carlos@email.com", "150"),  # Edad inválida
    ("Maria", "maria@email.com", "veinte"),  # Edad no numérica
    ("", "luis@email.com", "30")  # Nombre vacío
]

for nombre, email, edad in usuarios_prueba:
    try:
        usuario_valido = validar_usuario(nombre, email, edad)
        print(f"✓ Usuario válido: {usuario_valido}")
    except EmailInvalidoError as e:
        print(f"✗ Error en email: {e}")
    except EdadInvalidaError as e:
        print(f"✗ Error en edad: {e}")
    except ValidacionError as e:
        print(f"✗ Error de validación: {e}")
    except Exception as e:
        print(f"✗ Error inesperado: {e}")