"""
Manejo de Strings en Python
Operaciones, métodos y formatos de cadenas de texto
"""

# 1. CREACIÓN Y OPERACIONES BÁSICAS
# ---------------------------------
print("=== OPERACIONES BÁSICAS CON STRINGS ===")

# Diferentes formas de crear strings
cadena1 = "Hola Mundo"
cadena2 = 'Python es genial'
cadena3 = """Este es un string
multilínea que permite
escribir en varias líneas"""
cadena4 = '''Otro string
multilínea con comillas simples'''

print(cadena1)
print(cadena2)
print(cadena3)
print(cadena4)

# Concatenación
nombre = "Ana"
apellido = "García"
nombre_completo = nombre + " " + apellido
print(f"\nConcatenación: {nombre_completo}")

# Repetición
risa = "ja" * 3 + "!"
print(f"Repetición: {risa}")

# 2. MÉTODOS COMUNES DE STRINGS
# -----------------------------
print("\n=== MÉTODOS DE STRINGS ===")

texto = "  Python es un lenguaje de programación PODEROSO  "

# Métodos de transformación
print(f"Original: '{texto}'")
print(f"strip(): '{texto.strip()}'")  # Elimina espacios al inicio y final
print(f"lower(): '{texto.lower()}'")  # Todo a minúsculas
print(f"upper(): '{texto.upper()}'")  # Todo a mayúsculas
print(f"title(): '{texto.title()}'")  # Formato título
print(f"capitalize(): '{texto.capitalize()}'")  # Primera letra mayúscula
print(f"swapcase(): '{texto.swapcase()}'")  # Intercambia mayúsculas/minúsculas

# Métodos de búsqueda y verificación
texto_limpio = texto.strip()
print(f"\nTexto limpio: '{texto_limpio}'")
print(f"startswith('Python'): {texto_limpio.startswith('Python')}")
print(f"endswith('PODEROSO'): {texto_limpio.endswith('PODEROSO')}")
print(f"find('lenguaje'): {texto_limpio.find('lenguaje')}")  # Posición de la palabra
print(f"count('a'): {texto_limpio.count('a')}")  # Cuenta apariciones de 'a'

# Métodos de reemplazo y división
print(f"\nreplace('PODEROSO', 'fantástico'): {texto_limpio.replace('PODEROSO', 'fantástico')}")
print(f"split(): {texto_limpio.split()}")  # Divide por espacios
print(f"split('de'): {texto_limpio.split('de')}")  # Divide por 'de'

# 3. FORMATEO DE STRINGS
# ----------------------
print("\n=== FORMATEO DE STRINGS ===")

nombre = "Carlos"
edad = 30
salario = 45000.50

# Método format()
mensaje1 = "Hola, me llamo {} y tengo {} años".format(nombre, edad)
mensaje2 = "Salario: ${:,.2f}".format(salario)
mensaje3 = "Coordenadas: ({x}, {y})".format(x=10, y=20)

print(f"format() básico: {mensaje1}")
print(f"format() con números: {mensaje2}")
print(f"format() con nombres: {mensaje3}")

# f-strings (Python 3.6+)
mensaje4 = f"Hola {nombre}, tienes {edad} años y ganas ${salario:,.2f}"
mensaje5 = f"Operación: {5 + 3} = {5 + 3}"
mensaje6 = f"Nombre en mayúsculas: {nombre.upper()}"

print(f"f-string básico: {mensaje4}")
print(f"f-string con operaciones: {mensaje5}")
print(f"f-string con métodos: {mensaje6}")

# 4. STRINGS COMO SECUENCIAS
# --------------------------
print("\n=== STRINGS COMO SECUENCIAS ===")

texto = "Python"

# Acceso por índice
print(f"Texto: {texto}")
print(f"Primer carácter: {texto[0]}")
print(f"Último carácter: {texto[-1]}")
print(f"Tercer carácter: {texto[2]}")

# Slicing (rebanado)
print(f"\nSlicing:")
print(f"texto[0:3]: {texto[0:3]}")  # 'Pyt'
print(f"texto[2:]: {texto[2:]}")  # 'thon'
print(f"texto[:4]: {texto[:4]}")  # 'Pyth'
print(f"texto[::2]: {texto[::2]}")  # 'Pto' (cada 2 caracteres)
print(f"texto[::-1]: {texto[::-1]}")  # 'nohtyP' (invertido)

# Longitud y iteración
print(f"\nLongitud: {len(texto)} caracteres")
print("Iteración:")
for i, caracter in enumerate(texto):
    print(f"  Posición {i}: '{caracter}'")

# 5. MÉTODOS DE VALIDACIÓN
# ------------------------
print("\n=== MÉTODOS DE VALIDACIÓN ===")

test_cases = [
    "Python123",
    "12345",
    "SoloLetras",
    "con espacios",
    "CONMAYUSCULAS",
    "minusculas",
    "Título Ejemplo",
    "  ",
    ""
]

for caso in test_cases:
    print(f"'{caso}':")
    print(f"  isalnum(): {caso.isalnum()}")  # Alfanumérico
    print(f"  isalpha(): {caso.isalpha()}")  # Solo letras
    print(f"  isdigit(): {caso.isdigit()}")  # Solo dígitos
    print(f"  islower(): {caso.islower()}")  # Solo minúsculas
    print(f"  isupper(): {caso.isupper()}")  # Solo mayúsculas
    print(f"  istitle(): {caso.istitle()}")  # Formato título
    print(f"  isspace(): {caso.isspace()}")  # Solo espacios
    print()

# 6. EJEMPLO PRÁCTICO: PROCESADOR DE TEXTO
# ----------------------------------------
print("=== PROCESADOR DE TEXTO ===")


class ProcesadorTexto:
    """Clase para procesar y analizar texto"""

    def __init__(self, texto):
        self.texto = texto.strip()

    def estadisticas_basicas(self):
        """Calcula estadísticas básicas del texto"""
        palabras = self.texto.split()
        caracteres_totales = len(self.texto)
        caracteres_sin_espacios = len(self.texto.replace(" ", ""))

        return {
            'palabras': len(palabras),
            'caracteres_totales': caracteres_totales,
            'caracteres_sin_espacios': caracteres_sin_espacios,
            'palabra_mas_larga': max(palabras, key=len) if palabras else "",
            'palabra_mas_corta': min(palabras, key=len) if palabras else ""
        }

    def analizar_frecuencia(self):
        """Analiza frecuencia de palabras y caracteres"""
        palabras = self.texto.lower().split()
        caracteres = self.texto.lower().replace(" ", "")

        from collections import Counter

        freq_palabras = Counter(palabras)
        freq_caracteres = Counter(caracteres)

        return {
            'palabras_comunes': freq_palabras.most_common(5),
            'caracteres_comunes': freq_caracteres.most_common(5)
        }

    def formatear_texto(self, formato):
        """Formatea el texto según el formato especificado"""
        formatos = {
            'titulo': self.texto.title(),
            'oracion': self.texto.capitalize(),
            'invertido': self.texto[::-1],
            'alternando': self._alternar_mayus_minus()
        }
        return formatos.get(formato, self.texto)

    def _alternar_mayus_minus(self):
        """Alterna entre mayúsculas y minúsculas"""
        resultado = ""
        for i, char in enumerate(self.texto):
            if i % 2 == 0:
                resultado += char.upper()
            else:
                resultado += char.lower()
        return resultado


# Usando el procesador de texto
texto_ejemplo = "Python es un lenguaje de programación versátil y poderoso"
procesador = ProcesadorTexto(texto_ejemplo)

print(f"Texto original: {texto_ejemplo}")

# Estadísticas
stats = procesador.estadisticas_basicas()
print("\nEstadísticas:")
for clave, valor in stats.items():
    print(f"  {clave}: {valor}")

# Frecuencia
freq = procesador.analizar_frecuencia()
print("\nFrecuencias:")
print("  Palabras más comunes:", freq['palabras_comunes'])
print("  Caracteres más comunes:", freq['caracteres_comunes'])

# Formatos
print("\nFormatos:")
print(f"  Título: {procesador.formatear_texto('titulo')}")
print(f"  Oración: {procesador.formatear_texto('oracion')}")
print(f"  Invertido: {procesador.formatear_texto('invertido')}")
print(f"  Alternando: {procesador.formatear_texto('alternando')}")

# 7. EJEMPLO PRÁCTICO: VALIDADOR DE CONTRASEÑAS
# ---------------------------------------------
print("\n=== VALIDADOR DE CONTRASEÑAS ===")


class ValidadorContraseña:
    """Valida que una contraseña cumpla con requisitos de seguridad"""

    @staticmethod
    def validar(contraseña):
        """Valida una contraseña y retorna detalles de la validación"""
        errores = []
        advertencias = []

        # Verificar longitud
        if len(contraseña) < 8:
            errores.append("Debe tener al menos 8 caracteres")
        elif len(contraseña) < 12:
            advertencias.append("Recomendado: 12 o más caracteres")

        # Verificar complejidad
        if not any(c.isupper() for c in contraseña):
            errores.append("Debe contener al menos una mayúscula")

        if not any(c.islower() for c in contraseña):
            errores.append("Debe contener al menos una minúscula")

        if not any(c.isdigit() for c in contraseña):
            errores.append("Debe contener al menos un número")

        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in contraseña):
            advertencias.append("Recomendado: incluir caracteres especiales")

        # Calcular fortaleza
        fortaleza = ValidadorContraseña._calcular_fortaleza(contraseña, errores)

        return {
            'es_valida': len(errores) == 0,
            'errores': errores,
            'advertencias': advertencias,
            'fortaleza': fortaleza,
            'longitud': len(contraseña)
        }

    @staticmethod
    def _calcular_fortaleza(contraseña, errores):
        """Calcula la fortaleza de la contraseña"""
        if errores:
            return "Débil"

        puntaje = 0

        # Longitud
        if len(contraseña) >= 12:
            puntaje += 2
        elif len(contraseña) >= 8:
            puntaje += 1

        # Complejidad
        tipos_caracteres = 0
        if any(c.isupper() for c in contraseña):
            tipos_caracteres += 1
        if any(c.islower() for c in contraseña):
            tipos_caracteres += 1
        if any(c.isdigit() for c in contraseña):
            tipos_caracteres += 1
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in contraseña):
            tipos_caracteres += 1

        puntaje += min(tipos_caracteres, 3)

        if puntaje >= 4:
            return "Muy fuerte"
        elif puntaje >= 3:
            return "Fuerte"
        elif puntaje >= 2:
            return "Moderada"
        else:
            return "Débil"


# Probar el validador
contraseñas_prueba = [
    "abc",  # Muy débil
    "password",  # Débil
    "Password123",  # Moderada
    "P@ssw0rd123!",  # Fuerte
    "MyV3ryS3cur3P@ssw0rd!"  # Muy fuerte
]

print("Validación de contraseñas:")
for contraseña in contraseñas_prueba:
    resultado = ValidadorContraseña.validar(contraseña)
    print(f"\nContraseña: '{contraseña}'")
    print(f"  Válida: {resultado['es_valida']}")
    print(f"  Fortaleza: {resultado['fortaleza']}")
    print(f"  Longitud: {resultado['longitud']}")

    if resultado['errores']:
        print("  Errores:")
        for error in resultado['errores']:
            print(f"    - {error}")

    if resultado['advertencias']:
        print("  Advertencias:")
        for advertencia in resultado['advertencias']:
            print(f"    - {advertencia}")

# 8. MANIPULACIÓN AVANZADA
# ------------------------
print("\n=== MANIPULACIÓN AVANZADA ===")

# Justificación de texto
texto = "Python"
print(f"Texto: '{texto}'")
print(f"center(10): '{texto.center(10)}'")
print(f"ljust(10): '{texto.ljust(10)}'")
print(f"rjust(10): '{texto.rjust(10)}'")

# Partición y unión
frase = "Python,Java,C++,JavaScript"
print(f"\nFrase: {frase}")
partes = frase.split(",")
print(f"split(','): {partes}")
unido = "-".join(partes)
print(f"'-'.join(): {unido}")

# Eliminación de prefijos/sufijos
archivo = "documento.txt"
print(f"\nArchivo: {archivo}")
print(f"removeprefix('doc'): {archivo.removeprefix('doc')}")
print(f"removesuffix('.txt'): {archivo.removesuffix('.txt')}")

# Codificación y decodificación
texto_original = "Hola ñandú"
texto_codificado = texto_original.encode('utf-8')
texto_decodificado = texto_codificado.decode('utf-8')

print(f"\nCodificación:")
print(f"Original: {texto_original}")
print(f"Codificado (bytes): {texto_codificado}")
print(f"Decodificado: {texto_decodificado}")
