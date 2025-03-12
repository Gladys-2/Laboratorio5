import json

def cargar_alumnos(ruta_archivo):# Esta función carga los datos de los alumnos desde un archivo JSON.
    # 'ruta_archivo' es la ruta al archivo JSON que contiene los datos.
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)  # Lee el archivo y carga su contenido como un objeto de Python (en este caso, una lista de diccionarios)

def buscar_alumno(alumnos, nombre):# Esta función busca un alumno en la lista de 'alumnos' por su nombre.
    # Compara los nombres sin importar mayúsculas/minúsculas (por eso se usa .lower()).
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre.lower():  # Si se encuentra un alumno con el nombre especificado, se devuelve el diccionario con su información.
            return alumno
    return None  # Si no se encuentra el alumno, se devuelve None.

if __name__ == "_main_":
    # Este bloque se ejecuta solo si el script se ejecuta directamente (no cuando se importa como módulo).
    # Ruta al archivo JSON donde se encuentran los datos de los alumnos
    ruta = 'alumnos.json' # Cargar los datos de los alumnos desde el archivo JSON
    alumnos = cargar_alumnos(ruta) # Pedir al usuario el nombre del alumno a buscar
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ") # Buscar el alumno con la función buscar_alumno
    resultado = buscar_alumno(alumnos, nombre_buscar)
    # Mostrar los resultados de la búsqueda
    if resultado:
        # Si se encuentra un alumno, se muestra su información
        print(f"Alumno encontrado: {resultado}")
    else:
        # Si no se encuentra, se informa al usuario
        print("Alumno no encontrado.")