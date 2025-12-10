"""
Pruebas de Unidad en Python
Unit testing with unittest and pytest-style testing
"""

import unittest
import sys
import io
from datetime import datetime, timedelta


# 1. FUNCIONES PARA PROBAR
# ------------------------

def sumar(a, b):
    """Suma dos números"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    return a + b


def dividir(a, b):
    """Divide dos números"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def es_palindromo(texto):
    """Verifica si un texto es palíndromo"""
    if not isinstance(texto, str):
        raise TypeError("El argumento debe ser un string")

    texto_limpio = texto.lower().replace(' ', '').replace(',', '').replace('.', '')
    return texto_limpio == texto_limpio[::-1]


def calcular_edad(fecha_nacimiento):
    """Calcula la edad a partir de la fecha de nacimiento"""
    if not isinstance(fecha_nacimiento, datetime):
        raise TypeError("La fecha debe ser un objeto datetime")

    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year

    # Ajustar si aún no ha pasado el cumpleaños este año
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad


class Calculadora:
    """Clase Calculadora para demostrar pruebas de clases"""

    def __init__(self):
        self.historial = []

    def sumar(self, a, b):
        """Suma dos números y guarda en historial"""
        resultado = a + b
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        """Multiplica dos números y guarda en historial"""
        resultado = a * b
        self.historial.append(f"{a} × {b} = {resultado}")
        return resultado

    def limpiar_historial(self):
        """Limpia el historial de operaciones"""
        self.historial.clear()

    def obtener_historial(self):
        """Retorna el historial de operaciones"""
        return self.historial.copy()


# 2. PRUEBAS CON UNITTEST
# -----------------------

class TestFuncionesMatematicas(unittest.TestCase):
    """Pruebas para las funciones matemáticas"""

    def test_sumar_numeros_positivos(self):
        """Prueba suma de números positivos"""
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(10, 5), 15)

    def test_sumar_numeros_negativos(self):
        """Prueba suma de números negativos"""
        self.assertEqual(sumar(-2, -3), -5)
        self.assertEqual(sumar(-10, 5), -5)

    def test_sumar_decimales(self):
        """Prueba suma de números decimales"""
        self.assertAlmostEqual(sumar(1.1, 2.2), 3.3, places=1)
        self.assertAlmostEqual(sumar(0.1, 0.2), 0.3, places=1)

    def test_sumar_tipos_invalidos(self):
        """Prueba que se lance TypeError con tipos inválidos"""
        with self.assertRaises(TypeError):
            sumar("2", 3)
        with self.assertRaises(TypeError):
            sumar(2, "3")

    def test_dividir_numeros_positivos(self):
        """Prueba división de números positivos"""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)

    def test_dividir_por_cero(self):
        """Prueba que se lance ValueError al dividir por cero"""
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_dividir_decimales(self):
        """Prueba división con números decimales"""
        self.assertAlmostEqual(dividir(1, 3), 0.333, places=3)
        self.assertAlmostEqual(dividir(5, 2), 2.5)


class TestFuncionesTexto(unittest.TestCase):
    """Pruebas para funciones de texto"""

    def test_es_palindromo_simple(self):
        """Prueba palíndromos simples"""
        self.assertTrue(es_palindromo("ana"))
        self.assertTrue(es_palindromo("reconocer"))
        self.assertFalse(es_palindromo("python"))

    def test_es_palindromo_con_espacios(self):
        """Prueba palíndromos con espacios y puntuación"""
        self.assertTrue(es_palindromo("anita lava la tina"))
        self.assertTrue(es_palindromo("A man, a plan, a canal: Panama"))

    def test_es_palindromo_mayusculas(self):
        """Prueba que las mayúsculas no afecten"""
        self.assertTrue(es_palindromo("Ana"))
        self.assertTrue(es_palindromo("Reconocer"))

    def test_es_palindromo_tipo_invalido(self):
        """Prueba que se lance TypeError con tipo inválido"""
        with self.assertRaises(TypeError):
            es_palindromo(123)
        with self.assertRaises(TypeError):
            es_palindromo([])


class TestCalculadora(unittest.TestCase):
    """Pruebas para la clase Calculadora"""

    def setUp(self):
        """Configuración antes de cada prueba"""
        self.calc = Calculadora()

    def tearDown(self):
        """Limpieza después de cada prueba"""
        self.calc.limpiar_historial()

    def test_sumar(self):
        """Prueba el método sumar"""
        resultado = self.calc.sumar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertIn("5 + 3 = 8", self.calc.historial)

    def test_multiplicar(self):
        """Prueba el método multiplicar"""
        resultado = self.calc.multiplicar(4, 7)
        self.assertEqual(resultado, 28)
        self.assertIn("4 × 7 = 28", self.calc.historial)

    def test_limpiar_historial(self):
        """Prueba limpiar historial"""
        self.calc.sumar(1, 1)
        self.calc.multiplicar(2, 2)

        self.assertEqual(len(self.calc.historial), 2)

        self.calc.limpiar_historial()
        self.assertEqual(len(self.calc.historial), 0)

    def test_obtener_historial_copia(self):
        """Prueba que obtener_historial retorna una copia"""
        self.calc.sumar(1, 2)
        historial = self.calc.obtener_historial()

        # Modificar la copia no debería afectar el original
        historial.append("operación falsa")
        self.assertNotIn("operación falsa", self.calc.historial)


class TestCalcularEdad(unittest.TestCase):
    """Pruebas para la función calcular_edad"""

    def test_edad_correcta(self):
        """Prueba cálculo de edad correcto"""
        # Persona que ya cumplió años este año
        fecha_nacimiento = datetime(1990, 5, 15)
        # Asumimos que hoy es después del 15 de mayo
        with unittest.mock.patch('__main__.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 6, 1)
            mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

            edad = calcular_edad(fecha_nacimiento)
            self.assertEqual(edad, 34)

    def test_edad_antes_cumpleanos(self):
        """Prueba cálculo de edad antes del cumpleaños"""
        fecha_nacimiento = datetime(1990, 8, 15)
        # Asumimos que hoy es antes del 15 de agosto
        with unittest.mock.patch('__main__.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 7, 1)
            mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

            edad = calcular_edad(fecha_nacimiento)
            self.assertEqual(edad, 33)

    def test_tipo_invalido(self):
        """Prueba que se lance TypeError con tipo inválido"""
        with self.assertRaises(TypeError):
            calcular_edad("1990-01-01")
        with self.assertRaises(TypeError):
            calcular_edad(1990)


# 3. PRUEBAS DE INTEGRACIÓN
# -------------------------

class TestIntegracion(unittest.TestCase):
    """Pruebas de integración entre componentes"""

    def test_calculadora_con_funciones(self):
        """Prueba integración entre Calculadora y funciones"""
        calc = Calculadora()

        # Usar calculadora y verificar con función independiente
        resultado_calc = calc.sumar(10, 20)
        resultado_func = sumar(10, 20)

        self.assertEqual(resultado_calc, resultado_func)
        self.assertEqual(resultado_calc, 30)

    def test_historial_operaciones_complejas(self):
        """Prueba historial con operaciones complejas"""
        calc = Calculadora()

        # Realizar múltiples operaciones
        calc.sumar(5, 3)  # 8
        calc.multiplicar(4, 2)  # 8
        calc.sumar(10, 5)  # 15

        historial = calc.obtener_historial()

        self.assertEqual(len(historial), 3)
        self.assertIn("5 + 3 = 8", historial)
        self.assertIn("4 × 2 = 8", historial)
        self.assertIn("10 + 5 = 15", historial)


# 4. PRUEBAS CON MOCKING
# -----------------------

class TestConMocking(unittest.TestCase):
    """Pruebas que utilizan mocking"""

    def test_mock_datetime(self):
        """Prueba con datetime mockeado"""
        with unittest.mock.patch('__main__.datetime') as mock_datetime:
            # Configurar el mock
            fecha_fija = datetime(2024, 1, 15)
            mock_datetime.now.return_value = fecha_fija
            mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

            # Probar con fecha de nacimiento
            fecha_nacimiento = datetime(1990, 5, 20)
            edad = calcular_edad(fecha_nacimiento)

            # Verificar que se usó el mock
            mock_datetime.now.assert_called_once()
            self.assertEqual(edad, 33)  # 2024 - 1990 - 1 (porque no ha cumplido)

    def test_mock_input(self):
        """Prueba mocking de input()"""
        with unittest.mock.patch('builtins.input', return_value='42'):
            # Esta función simularía usar input()
            def leer_numero():
                return int(input("Ingresa un número: "))

            resultado = leer_numero()
            self.assertEqual(resultado, 42)

    def test_mock_print(self):
        """Prueba mocking de print()"""
        with unittest.mock.patch('builtins.print') as mock_print:
            # Función que usa print
            def saludar(nombre):
                print(f"Hola {nombre}!")

            saludar("Mundo")

            # Verificar que print fue llamado correctamente
            mock_print.assert_called_once_with("Hola Mundo!")


# 5. PRUEBAS DE RENDIMIENTO
# --------------------------

class TestRendimiento(unittest.TestCase):
    """Pruebas de rendimiento y tiempo de ejecución"""

    def test_tiempo_ejecucion_sumar(self):
        """Prueba que sumar sea rápido"""
        import time

        inicio = time.time()
        for _ in range(10000):
            sumar(100, 200)
        fin = time.time()

        tiempo_total = fin - inicio
        self.assertLess(tiempo_total, 1.0)  # Debe tomar menos de 1 segundo

    def test_palindromo_grande(self):
        """Prueba rendimiento con palíndromo grande"""
        texto_largo = "a" * 1000 + "b" + "a" * 1000

        inicio = time.time()
        resultado = es_palindromo(texto_largo)
        fin = time.time()

        self.assertFalse(resultado)
        self.assertLess(fin - inicio, 0.1)  # Debe ser rápido


# 6. PRUEBAS DE ERRORES Y EXCEPCIONES
# -----------------------------------

class TestErrores(unittest.TestCase):
    """Pruebas específicas para manejo de errores"""

    def test_mensajes_error_sumar(self):
        """Prueba mensajes de error específicos"""
        with self.assertRaises(TypeError) as context:
            sumar("a", 1)

        self.assertEqual(str(context.exception), "Los argumentos deben ser números")

    def test_mensajes_error_dividir(self):
        """Prueba mensajes de error al dividir"""
        with self.assertRaises(ValueError) as context:
            dividir(10, 0)

        self.assertEqual(str(context.exception), "No se puede dividir por cero")

    def test_error_encadenado(self):
        """Prueba manejo de múltiples errores"""
        # Debe lanzar TypeError, no ValueError
        with self.assertRaises(TypeError):
            dividir("10", 0)


# 7. EJECUCIÓN DE PRUEBAS Y REPORTES
# -----------------------------------

def ejecutar_pruebas_individuales():
    """Ejecuta pruebas individuales y muestra reportes"""

    print("=== EJECUCIÓN DE PRUEBAS INDIVIDUALES ===\n")

    # Crear test suite
    suite = unittest.TestSuite()

    # Agregar pruebas específicas
    suite.addTest(TestFuncionesMatematicas('test_sumar_numeros_positivos'))
    suite.addTest(TestFuncionesMatematicas('test_dividir_por_cero'))
    suite.addTest(TestFuncionesTexto('test_es_palindromo_simple'))
    suite.addTest(TestCalculadora('test_sumar'))

    # Ejecutar suite
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)

    print(f"\nResumen: {resultado.testsRun} pruebas ejecutadas")
    print(f"Fallos: {len(resultado.failures)}")
    print(f"Errores: {len(resultado.errors)}")

    return resultado


def generar_reporte_cobertura():
    """Genera un reporte simple de cobertura"""
    print("\n=== REPORTE DE COBERTURA ===")

    # Esta es una simulación - en la práctica usarías coverage.py
    funciones_a_probar = [
        'sumar', 'dividir', 'es_palindromo', 'calcular_edad',
        'Calculadora.sumar', 'Calculadora.multiplicar',
        'Calculadora.limpiar_historial', 'Calculadora.obtener_historial'
    ]

    funciones_probadas = [
        'sumar', 'dividir', 'es_palindromo', 'calcular_edad',
        'Calculadora.sumar', 'Calculadora.multiplicar',
        'Calculadora.limpiar_historial', 'Calculadora.obtener_historial'
    ]

    cobertura = (len(funciones_probadas) / len(funciones_a_probar)) * 100

    print(f"Funciones a probar: {len(funciones_a_probar)}")
    print(f"Funciones probadas: {len(funciones_probadas)}")
    print(f"Cobertura: {cobertura:.1f}%")

    if cobertura == 100:
        print("✅ ¡Cobertura completa!")
    else:
        print("⚠️  Cobertura incompleta")
        no_probadas = set(funciones_a_probar) - set(funciones_probadas)
        if no_probadas:
            print("Funciones no probadas:")
            for func in no_probadas:
                print(f"  - {func}")


# 8. PRUEBAS MANUALES Y DEMOSTRACIÓN
# -----------------------------------

def demostrar_pruebas_manuales():
    """Demuestra pruebas manuales como alternativa"""

    print("\n=== PRUEBAS MANUALES ===")

    # Pruebas de sumar
    print("1. Probando sumar():")
    try:
        assert sumar(2, 3) == 5, "2 + 3 debería ser 5"
        assert sumar(-1, 1) == 0, "-1 + 1 debería ser 0"
        assert sumar(0, 0) == 0, "0 + 0 debería ser 0"
        print("   ✅ sumar() pasa todas las pruebas")
    except AssertionError as e:
        print(f"   ❌ sumar() falló: {e}")

    # Pruebas de dividir
    print("\n2. Probando dividir():")
    try:
        assert dividir(10, 2) == 5, "10 / 2 debería ser 5"
        assert dividir(9, 3) == 3, "9 / 3 debería ser 3"

        # Probar división por cero
        try:
            dividir(1, 0)
            assert False, "Debería haber lanzado ValueError"
        except ValueError:
            pass  # Esperado

        print("   ✅ dividir() pasa todas las pruebas")
    except AssertionError as e:
        print(f"   ❌ dividir() falló: {e}")

    # Pruebas de es_palindromo
    print("\n3. Probando es_palindromo():")
    try:
        assert es_palindromo("ana") == True, "'ana' debería ser palíndromo"
        assert es_palindromo("python") == False, "'python' no debería ser palíndromo"
        assert es_palindromo("A man a plan a canal Panama") == True, "Frase debería ser palíndromo"
        print("   ✅ es_palindromo() pasa todas las pruebas")
    except AssertionError as e:
        print(f"   ❌ es_palindromo() falló: {e}")

    # Pruebas de Calculadora
    print("\n4. Probando Calculadora:")
    try:
        calc = Calculadora()
        assert calc.sumar(5, 3) == 8, "5 + 3 debería ser 8"
        assert calc.multiplicar(4, 2) == 8, "4 × 2 debería ser 8"
        assert len(calc.obtener_historial()) == 2, "Historial debería tener 2 operaciones"

        calc.limpiar_historial()
        assert len(calc.obtener_historial()) == 0, "Historial debería estar vacío"

        print("   ✅ Calculadora pasa todas las pruebas")
    except AssertionError as e:
        print(f"   ❌ Calculadora falló: {e}")


# 9. EJECUCIÓN PRINCIPAL
# -----------------------

if __name__ == '__main__':
    print("🔬 SISTEMA DE PRUEBAS DE UNIDAD")
    print("=" * 50)

    # Ejecutar pruebas manuales
    demostrar_pruebas_manuales()

    # Generar reporte de cobertura
    generar_reporte_cobertura()

    print("\n" + "=" * 50)
    print("Ejecutando pruebas unitarias con unittest...")
    print("=" * 50)

    # Ejecutar todas las pruebas
    unittest.main(verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("¡Sistema de pruebas demostrado exitosamente!")
    print("\nBEST PRACTICES RECOMENDADAS:")
    print("1. Escribe pruebas antes del código (TDD)")
    print("2. Mantén las pruebas simples y rápidas")
    print("3. Usa nombres descriptivos para los tests")
    print("4. Prueba casos límite y errores")
    print("5. Mantén la cobertura de código alta")
    print("6. Ejecuta las pruebas frecuentemente")