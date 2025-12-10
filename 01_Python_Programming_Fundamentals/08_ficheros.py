"""
Manejo de Ficheros en Python
Lectura, escritura y manipulación de archivos
"""

import os
import json
import csv
from datetime import datetime

# 1. OPERACIONES BÁSICAS CON ARCHIVOS
# ------------------------------------
print("=== OPERACIONES BÁSICAS CON ARCHIVOS ===")


def demostracion_archivos_basicos():
    """Demuestra operaciones básicas con archivos"""

    # Crear y escribir en un archivo
    print("1. ESCRITURA BÁSICA:")
    with open('ejemplo.txt', 'w', encoding='utf-8') as archivo:
        archivo.write("Línea 1: Hola mundo\n")
        archivo.write("Línea 2: Python es genial\n")
        archivo.write("Línea 3: Manejo de archivos\n")
    print("   Archivo 'ejemplo.txt' creado exitosamente")

    # Leer todo el contenido
    print("\n2. LECTURA COMPLETA:")
    with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print("   Contenido completo:")
        print("   " + contenido.replace('\n', '\n   '))

    # Leer línea por línea
    print("\n3. LECTURA POR LÍNEAS:")
    with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
        print("   Líneas individuales:")
        for i, linea in enumerate(archivo, 1):
            print(f"   Línea {i}: {linea.strip()}")

    # Agregar contenido (append)
    print("\n4. AGREGAR CONTENIDO:")
    with open('ejemplo.txt', 'a', encoding='utf-8') as archivo:
        archivo.write("Línea 4: Contenido agregado\n")
        archivo.write("Línea 5: Última línea\n")
    print("   Contenido agregado exitosamente")

    # Leer con readlines()
    print("\n5. LECTURA CON READLINES():")
    with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        print(f"   Total de líneas: {len(lineas)}")
        for i, linea in enumerate(lineas, 1):
            print(f"   Línea {i}: {linea.strip()}")


# Ejecutar demostración
demostracion_archivos_basicos()

# 2. MANEJO DE ERRORES EN ARCHIVOS
# --------------------------------
print("\n=== MANEJO DE ERRORES EN ARCHIVOS ===")


def leer_archivo_seguro(nombre_archivo):
    """
    Intenta leer un archivo de forma segura con manejo de errores
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    except FileNotFoundError:
        return f"Error: El archivo '{nombre_archivo}' no existe"

    except PermissionError:
        return f"Error: No tienes permisos para leer '{nombre_archivo}'"

    except UnicodeDecodeError:
        return f"Error: Problema de codificación en '{nombre_archivo}'"

    except Exception as e:
        return f"Error inesperado: {type(e).__name__} - {str(e)}"


# Probar con diferentes casos
archivos_prueba = ['ejemplo.txt', 'archivo_inexistente.txt', '/root/archivo_protegido.txt']

for archivo in archivos_prueba:
    resultado = leer_archivo_seguro(archivo)
    print(f"Archivo: {archivo}")
    print(f"Resultado: {resultado}\n")

# 3. TRABAJANDO CON ARCHIVOS JSON
# -------------------------------
print("=== TRABAJANDO CON ARCHIVOS JSON ===")


def demostracion_json():
    """Demuestra lectura y escritura de archivos JSON"""

    # Datos para guardar en JSON
    datos_estudiantes = {
        "estudiantes": [
            {
                "id": 1,
                "nombre": "Ana García",
                "edad": 22,
                "carrera": "Ingeniería",
                "materias": ["Matemáticas", "Física", "Programación"],
                "activo": True
            },
            {
                "id": 2,
                "nombre": "Carlos López",
                "edad": 21,
                "carrera": "Medicina",
                "materias": ["Anatomía", "Biología", "Química"],
                "activo": True
            },
            {
                "id": 3,
                "nombre": "María Rodríguez",
                "edad": 23,
                "carrera": "Derecho",
                "materias": ["Derecho Civil", "Derecho Penal"],
                "activo": False
            }
        ],
        "total_estudiantes": 3,
        "fecha_actualizacion": datetime.now().isoformat()
    }

    # Guardar datos en JSON
    with open('estudiantes.json', 'w', encoding='utf-8') as archivo:
        json.dump(datos_estudiantes, archivo, indent=2, ensure_ascii=False)
    print("1. Datos guardados en 'estudiantes.json'")

    # Leer datos desde JSON
    with open('estudiantes.json', 'r', encoding='utf-8') as archivo:
        datos_cargados = json.load(archivo)

    print("2. Datos cargados desde JSON:")
    print(f"   Total estudiantes: {datos_cargados['total_estudiantes']}")

    for estudiante in datos_cargados['estudiantes']:
        estado = "Activo" if estudiante['activo'] else "Inactivo"
        print(f"   - {estudiante['nombre']} ({estudiante['carrera']}) - {estado}")

    # Modificar y guardar cambios
    datos_cargados['estudiantes'].append({
        "id": 4,
        "nombre": "Pedro Martínez",
        "edad": 20,
        "carrera": "Administración",
        "materias": ["Contabilidad", "Economía"],
        "activo": True
    })
    datos_cargados['total_estudiantes'] = len(datos_cargados['estudiantes'])
    datos_cargados['fecha_actualizacion'] = datetime.now().isoformat()

    with open('estudiantes_actualizado.json', 'w', encoding='utf-8') as archivo:
        json.dump(datos_cargados, archivo, indent=2, ensure_ascii=False)

    print("3. Datos actualizados guardados en 'estudiantes_actualizado.json'")


# Ejecutar demostración JSON
demostracion_json()

# 4. TRABAJANDO CON ARCHIVOS CSV
# ------------------------------
print("\n=== TRABAJANDO CON ARCHIVOS CSV ===")


def demostracion_csv():
    """Demuestra lectura y escritura de archivos CSV"""

    # Datos para guardar en CSV
    datos_empleados = [
        ['ID', 'Nombre', 'Departamento', 'Salario', 'Fecha_Contratacion'],
        [1, 'Ana García', 'Ventas', 50000, '2020-01-15'],
        [2, 'Carlos López', 'TI', 75000, '2019-03-20'],
        [3, 'María Rodríguez', 'Marketing', 60000, '2021-06-10'],
        [4, 'Pedro Martínez', 'Ventas', 55000, '2022-02-28'],
        [5, 'Laura Díaz', 'TI', 80000, '2018-11-05']
    ]

    # Guardar datos en CSV
    with open('empleados.csv', 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos_empleados)
    print("1. Datos guardados en 'empleados.csv'")

    # Leer datos desde CSV
    print("\n2. Leyendo datos desde CSV:")
    with open('empleados.csv', 'r', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        for i, fila in enumerate(reader):
            if i == 0:
                print("   Encabezados:", fila)
            else:
                print(f"   Fila {i}: {fila}")

    # Leer CSV como diccionarios
    print("\n3. Leyendo CSV como diccionarios:")
    with open('empleados.csv', 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            print(f"   {fila['Nombre']} - {fila['Departamento']} - ${fila['Salario']}")

    # Agregar nuevos empleados
    nuevos_empleados = [
        [6, 'Sofia Chen', 'Marketing', 65000, '2023-01-15'],
        [7, 'David Kim', 'TI', 85000, '2023-03-20']
    ]

    with open('empleados.csv', 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(nuevos_empleados)
    print("\n4. Nuevos empleados agregados al CSV")


# Ejecutar demostración CSV
demostracion_csv()

# 5. OPERACIONES CON EL SISTEMA DE ARCHIVOS
# -----------------------------------------
print("\n=== OPERACIONES CON EL SISTEMA DE ARCHIVOS ===")


def demostracion_sistema_archivos():
    """Demuestra operaciones con el sistema de archivos"""

    print("1. INFORMACIÓN DEL DIRECTORIO ACTUAL:")
    directorio_actual = os.getcwd()
    print(f"   Directorio actual: {directorio_actual}")

    print("\n2. LISTANDO ARCHIVOS EN EL DIRECTORIO:")
    archivos = os.listdir('.')
    print(f"   Archivos en el directorio actual ({len(archivos)} encontrados):")

    for archivo in sorted(archivos)[:10]:  # Mostrar solo los primeros 10
        if os.path.isfile(archivo):
            tamaño = os.path.getsize(archivo)
            print(f"     📄 {archivo} ({tamaño} bytes)")
        else:
            print(f"     📁 {archivo}/")

    print("\n3. INFORMACIÓN DE ARCHIVOS ESPECÍFICOS:")
    archivos_verificar = ['ejemplo.txt', 'estudiantes.json', 'empleados.csv']

    for archivo in archivos_verificar:
        if os.path.exists(archivo):
            tamaño = os.path.getsize(archivo)
            modificado = datetime.fromtimestamp(os.path.getmtime(archivo))
            es_archivo = os.path.isfile(archivo)
            es_directorio = os.path.isdir(archivo)

            print(f"   {archivo}:")
            print(f"     Existe: Sí")
            print(f"     Tamaño: {tamaño} bytes")
            print(f"     Modificado: {modificado}")
            print(f"     Es archivo: {es_archivo}")
            print(f"     Es directorio: {es_directorio}")
        else:
            print(f"   {archivo}: No existe")

    print("\n4. CREANDO DIRECTORIOS:")
    # Crear directorios de prueba
    directorios_crear = ['temp_dir', 'data/archivos', 'backup/2024']

    for directorio in directorios_crear:
        os.makedirs(directorio, exist_ok=True)
        print(f"   Directorio creado: {directorio}")

    # Verificar creación
    print("\n5. VERIFICANDO DIRECTORIOS CREADOS:")
    for root, dirs, files in os.walk('.'):
        nivel = root.count(os.sep)
        indentacion = ' ' * 2 * nivel
        print(f"{indentacion}📁 {os.path.basename(root)}/")

        sub_indentacion = ' ' * 2 * (nivel + 1)
        for archivo in files[:3]:  # Mostrar solo primeros 3 archivos por directorio
            print(f"{sub_indentacion}📄 {archivo}")

        if len(files) > 3:
            print(f"{sub_indentacion}... y {len(files) - 3} más")


# Ejecutar demostración del sistema de archivos
demostracion_sistema_archivos()

# 6. EJEMPLO PRÁCTICO: SISTEMA DE REGISTRO DE LOGS
# ------------------------------------------------
print("\n=== SISTEMA DE REGISTRO DE LOGS ===")


class SistemaLogs:
    """Sistema simple para registrar logs en archivos"""

    def __init__(self, archivo_log='sistema.log'):
        self.archivo_log = archivo_log
        self.niveles = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    def registrar(self, nivel, mensaje, usuario='SISTEMA'):
        """Registra un mensaje en el log"""
        if nivel not in self.niveles:
            raise ValueError(f"Nivel debe ser uno de: {self.niveles}")

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        linea_log = f"[{timestamp}] [{nivel}] [{usuario}] {mensaje}\n"

        with open(self.archivo_log, 'a', encoding='utf-8') as archivo:
            archivo.write(linea_log)

        print(f"LOG: {linea_log.strip()}")

    def leer_logs(self, nivel=None, usuario=None, ultimas_lineas=10):
        """Lee logs con filtros opcionales"""
        if not os.path.exists(self.archivo_log):
            return "No hay logs registrados"

        with open(self.archivo_log, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Aplicar filtros
        lineas_filtradas = []
        for linea in lineas:
            cumple_nivel = nivel is None or f"[{nivel}]" in linea
            cumple_usuario = usuario is None or f"[{usuario}]" in linea

            if cumple_nivel and cumple_usuario:
                lineas_filtradas.append(linea)

        # Retornar últimas líneas
        return lineas_filtradas[-ultimas_lineas:]

    def estadisticas_logs(self):
        """Proporciona estadísticas de los logs"""
        if not os.path.exists(self.archivo_log):
            return {"total_logs": 0}

        with open(self.archivo_log, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        conteo_niveles = {}
        for linea in lineas:
            for nivel in self.niveles:
                if f"[{nivel}]" in linea:
                    conteo_niveles[nivel] = conteo_niveles.get(nivel, 0) + 1
                    break

        return {
            'total_logs': len(lineas),
            'conteo_por_nivel': conteo_niveles,
            'archivo': self.archivo_log,
            'tamaño_bytes': os.path.getsize(self.archivo_log)
        }


# Usar el sistema de logs
print("1. REGISTRANDO LOGS DE EJEMPLO:")
sistema_logs = SistemaLogs('mi_sistema.log')

# Registrar algunos logs de ejemplo
sistema_logs.registrar('INFO', 'Sistema iniciado correctamente')
sistema_logs.registrar('INFO', 'Usuario admin conectado', 'admin')
sistema_logs.registrar('WARNING', 'Espacio en disco bajo (85% usado)')
sistema_logs.registrar('ERROR', 'No se pudo conectar a la base de datos', 'app_server')
sistema_logs.registrar('INFO', 'Backup completado exitosamente', 'backup_service')

print("\n2. LEYENDO LOGS RECIENTES:")
logs_recientes = sistema_logs.leer_logs(ultimas_lineas=3)
for log in logs_recientes:
    print(f"   {log.strip()}")

print("\n3. FILTRANDO LOGS POR NIVEL:")
logs_error = sistema_logs.leer_logs(nivel='ERROR')
for log in logs_error:
    print(f"   {log.strip()}")

print("\n4. ESTADÍSTICAS DE LOGS:")
stats = sistema_logs.estadisticas_logs()
for clave, valor in stats.items():
    print(f"   {clave}: {valor}")

# 7. EJEMPLO PRÁCTICO: ORGANIZADOR DE ARCHIVOS
# --------------------------------------------
print("\n=== ORGANIZADOR DE ARCHIVOS ===")


class OrganizadorArchivos:
    """Organiza archivos en directorios por tipo"""

    # Mapeo de extensiones a carpetas
    CATEGORIAS = {
        'documentos': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
        'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv'],
        'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'codigo': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
        'comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz']
    }

    def __init__(self, directorio_base='.'):
        self.directorio_base = directorio_base

    def analizar_directorio(self):
        """Analiza los archivos en el directorio"""
        archivos_por_categoria = {categoria: [] for categoria in self.CATEGORIAS}
        archivos_por_categoria['otros'] = []

        for archivo in os.listdir(self.directorio_base):
            ruta_completa = os.path.join(self.directorio_base, archivo)

            if os.path.isfile(ruta_completa):
                extension = os.path.splitext(archivo)[1].lower()
                categoria = self._clasificar_archivo(extension)
                archivos_por_categoria[categoria].append(archivo)

        return archivos_por_categoria

    def _clasificar_archivo(self, extension):
        """Clasifica un archivo por su extensión"""
        for categoria, extensiones in self.CATEGORIAS.items():
            if extension in extensiones:
                return categoria
        return 'otros'

    def organizar_archivos(self, ejecutar=False):
        """Organiza los archivos en carpetas por categoría"""
        archivos_por_categoria = self.analizar_directorio()

        print("PLAN DE ORGANIZACIÓN:")
        total_archivos = 0

        for categoria, archivos in archivos_por_categoria.items():
            if archivos:
                print(f"\n  📁 {categoria.upper()}:")
                for archivo in archivos:
                    print(f"     ➤ {archivo}")
                total_archivos += len(archivos)

        print(f"\nTotal de archivos a organizar: {total_archivos}")

        if ejecutar and total_archivos > 0:
            print("\nEJECUTANDO ORGANIZACIÓN...")
            self._ejecutar_organizacion(archivos_por_categoria)
        elif ejecutar:
            print("No hay archivos para organizar")

    def _ejecutar_organizacion(self, archivos_por_categoria):
        """Ejecuta la organización real de archivos"""
        for categoria, archivos in archivos_por_categoria.items():
            if archivos:
                # Crear directorio si no existe
                directorio_categoria = os.path.join(self.directorio_base, categoria)
                os.makedirs(directorio_categoria, exist_ok=True)

                # Mover archivos
                for archivo in archivos:
                    ruta_original = os.path.join(self.directorio_base, archivo)
                    ruta_destino = os.path.join(directorio_categoria, archivo)

                    try:
                        os.rename(ruta_original, ruta_destino)
                        print(f"  ✓ Movido: {archivo} → {categoria}/")
                    except Exception as e:
                        print(f"  ✗ Error moviendo {archivo}: {e}")


# Demostración del organizador (solo análisis, sin ejecutar)
print("ANÁLISIS DEL DIRECTORIO ACTUAL:")
organizador = OrganizadorArchivos()
archivos_por_categoria = organizador.analizar_directorio()

for categoria, archivos in archivos_por_categoria.items():
    if archivos:
        print(f"  {categoria}: {len(archivos)} archivos")
        for archivo in archivos[:3]:  # Mostrar solo 3 por categoría
            print(f"    - {archivo}")
        if len(archivos) > 3:
            print(f"    ... y {len(archivos) - 3} más")

print("\n" + "=" * 60)
print("¡Manejo de archivos demostrado exitosamente!")
print("Archivos creados durante la demostración:")
archivos_creados = [f for f in os.listdir('.') if f.endswith(('.txt', '.json', '.csv', '.log'))]
for archivo in sorted(archivos_creados):
    print(f"  📄 {archivo}")