import json

def cargar_alumnos(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

def buscar_alumno(alumnos, nombre):
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre.lower():
            return alumno
    return None

if __name__ == "_main_":
    ruta = 'alumnos.json'
    alumnos = cargar_alumnos(ruta)
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")
    resultado = buscar_alumno(alumnos, nombre_buscar)
    if resultado:
        print(f"Alumno encontrado: {resultado}")
    else:
        print("Alumno no encontrado.")