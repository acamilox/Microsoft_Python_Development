'''

Escriba una función Python llamada read_file_contents que tome file_path como argumento.

Dentro de la función, utilice un bloque try-except para intentar abrir el archivo, leer
su contenido e imprimirlo en la consola.

Maneje el FileNotFoundError específicamente imprimiendo un mensaje de error apropiado
si el archivo no existe.

'''

def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('Error: File not found - /Users/Example/Documents/my_file.txt')