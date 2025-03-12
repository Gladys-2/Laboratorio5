import unittest
from gestion_alumnos import buscar_alumno  # Importamos la función buscar_alumno desde el módulo gestion_alumnos

class TestGestionAlumnos(unittest.TestCase):# Esta clase contiene las pruebas unitarias para la función buscar_alumno

    def setUp(self):
        # Método que se ejecuta antes de cada prueba
        # Aquí definimos una prueba: una lista de diccionarios con información de alumnos
        self.alumnos = [
            {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
            {"nombre": "Luis", "edad": 22, "carrera": "Matemáticas"},
            {"nombre": "María", "edad": 21, "carrera": "Física"}
        ]

    def test_buscar_alumno_existente(self):# Este es un caso de prueba donde se busca un alumno que sí existe en la lista
        resultado = buscar_alumno(self.alumnos, "Ana")  # Llamamos a la función buscar_alumno
        self.assertIsNotNone(resultado)  # Comprobamos que la función no devuelva None, es decir, el alumno se encontró
        self.assertEqual(resultado['nombre'], "Ana")  # Verificamos que el nombre del alumno encontrado sea "Ana"

    def test_buscar_alumno_inexistente(self):# Este es un caso de prueba donde se busca un alumno que NO existe en la lista
        resultado = buscar_alumno(self.alumnos, "Carlos")  # Llamamos a la función buscar_alumno
        self.assertIsNone(resultado)  # Comprobamos que la función devuelva None, es decir, el alumno no se encontró

if __name__ == '_main_':
    # Esta línea ejecuta las pruebas cuando el archivo se ejecuta directamente
    unittest.main()