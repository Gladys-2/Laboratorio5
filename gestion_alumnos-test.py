import unittest
from gestion_alumnos import buscar_alumno

class TestGestionAlumnos(unittest.TestCase):

    def setUp(self):
       
        self.alumnos = [
            {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
            {"nombre": "Luis", "edad": 22, "carrera": "Matemáticas"},
            {"nombre": "María", "edad": 21, "carrera": "Física"}
        ]

    def test_buscar_alumno_existente(self):
       
        resultado = buscar_alumno(self.alumnos, "Ana")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado['nombre'], "Ana")

    def test_buscar_alumno_inexistente(self):
    
        resultado = buscar_alumno(self.alumnos, "Carlos")
        self.assertIsNone(resultado)

if __name__ == '_main_':
    unittest.main()