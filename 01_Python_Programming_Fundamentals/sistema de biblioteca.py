# Diseña un sistema de biblioteca que permita registrar libros y préstamos.

'''
Requisitos

Clase Libro
• titulo
• autor
• año
• disponible (True al inicio)
• prestar() → marca como no disponible
• devolver() → marca como disponible


Clase Usuario
• nombre
• lista de libros_prestados
• prestar_libro(libro)
• devolver_libro(libro)


Clase Biblioteca
• lista de libros
• agregar_libro(libro)
• buscar_libro(titulo)
• listar_disponibles()

Simulación obligatoria
1. Crear 5 libros
2. Crear 2 usuarios
3. Registrar dos préstamos
4. Registrar una devolución
5. Imprimir los libros disponibles antes y después del proceso

'''

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = True  # Atributo, no método
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self):
        self.disponible = True
    
    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.año}) - {'Disponible' if self.disponible else 'Prestado'}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []  # Atributo inicializado aquí
    
    def prestar_libro(self, libro):
        if libro.prestar():  # Intenta prestar el libro
            self.libros_prestados.append(libro)
            return True
        return False
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            return True
        return False
    
    def __str__(self):
        return f"Usuario: {self.nombre}, Libros prestados: {len(self.libros_prestados)}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []  # Inicializar lista vacía
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def listar_disponibles(self):
        disponibles = []
        for libro in self.libros:
            if libro.disponible:
                disponibles.append(libro)
        return disponibles
    
    def __str__(self):
        return f"Biblioteca con {len(self.libros)} libros"


# SIMULACIÓN
def main():
    print("=" * 50)
    print("SISTEMA DE BIBLIOTECA")
    print("=" * 50)
    
    # 1. Crear biblioteca
    biblioteca = Biblioteca()
    
    # 2. Crear 5 libros
    libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    libro4 = Libro("1984", "George Orwell", 1949)
    libro5 = Libro("Orgullo y prejuicio", "Jane Austen", 1813)
    
    # Agregar libros a la biblioteca
    for libro in [libro1, libro2, libro3, libro4, libro5]:
        biblioteca.agregar_libro(libro)
    
    # 3. Crear 2 usuarios
    usuario1 = Usuario("Juan")
    usuario2 = Usuario("Pedro")
    
    print("\nEstado inicial de la biblioteca:")
    print(biblioteca)
    
    # Listar libros disponibles ANTES de préstamos
    print("\nLibros disponibles antes de los préstamos:")
    disponibles = biblioteca.listar_disponibles()
    for libro in disponibles:
        print(f"  - {libro.titulo}")
    
    print(f"\nTotal disponibles: {len(disponibles)}")
    print("=" * 50)
    
    # 4. Registrar dos préstamos
    print("\nREGISTRANDO PRÉSTAMOS:")
    print("-" * 30)
    
    # Primer préstamo
    print(f"\n{usuario1.nombre} intenta prestar '{libro1.titulo}'")
    if usuario1.prestar_libro(libro1):
        print(f"✓ Préstamo exitoso")
    else:
        print("✗ Libro no disponible")
    
    # Segundo préstamo
    print(f"\n{usuario2.nombre} intenta prestar '{libro2.titulo}'")
    if usuario2.prestar_libro(libro2):
        print(f"✓ Préstamo exitoso")
    else:
        print("✗ Libro no disponible")
    
    # Intentar préstamo de libro ya prestado
    print(f"\n{usuario1.nombre} intenta prestar '{libro2.titulo}' (ya prestado)")
    if usuario1.prestar_libro(libro2):
        print(f"✓ Préstamo exitoso")
    else:
        print("✗ Libro no disponible (ya está prestado)")
    
    print("\nEstado después de los préstamos:")
    print(f"{usuario1}")
    print(f"{usuario2}")
    
    # 5. Registrar una devolución
    print("\n" + "=" * 50)
    print("REGISTRANDO DEVOLUCIÓN:")
    print("-" * 30)
    
    print(f"\n{usuario1.nombre} devuelve '{libro1.titulo}'")
    if usuario1.devolver_libro(libro1):
        print("✓ Devolución exitosa")
    else:
        print("✗ Error en devolución")
    
    print(f"\nEstado final de {usuario1}")
    
    # 6. Imprimir los libros disponibles DESPUÉS del proceso
    print("\n" + "=" * 50)
    print("LIBROS DISPONIBLES DESPUÉS DEL PROCESO:")
    print("-" * 40)
    
    disponibles_final = biblioteca.listar_disponibles()
    for libro in disponibles_final:
        print(f"  - {libro.titulo}")
    
    print(f"\nTotal disponibles: {len(disponibles_final)}")
    
    # Resumen
    print("\n" + "=" * 50)
    print("RESUMEN FINAL:")
    print("-" * 30)
    print(f"Libros en biblioteca: {len(biblioteca.libros)}")
    print(f"Libros disponibles: {len(disponibles_final)}")
    print(f"Libros prestados: {len(biblioteca.libros) - len(disponibles_final)}")
    print(f"Libros de {usuario1.nombre}: {[libro.titulo for libro in usuario1.libros_prestados]}")
    print(f"Libros de {usuario2.nombre}: {[libro.titulo for libro in usuario2.libros_prestados]}")
    
    # Mostrar estado de todos los libros
    print("\nEstado detallado de todos los libros:")
    for libro in biblioteca.libros:
        print(f"  - {libro}")


if __name__ == "__main__":
    main()