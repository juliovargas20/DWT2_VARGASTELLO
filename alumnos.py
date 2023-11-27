import pickle

class Alumno:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = None
        self.nacionalidad = nacionalidad

    def leerNota(self):
        self.nota = float(input(f"Ingrese nota para {self.nombre} {self.apellido}: "))

    def registrarNota(self, notaAlumno):
        if 0 <= notaAlumno <= 20:
            self.nota = notaAlumno
            print(f"Nota registrada correctamente para {self.nombre} {self.apellido}")
        else:
            print("La nota debe estar en el rango de 0 a 20. Por favor, inténtelo de nuevo.")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad}, Nota: {self.nota}, Nacionalidad: {self.nacionalidad}"

def guardar_alumnos(lista_alumnos):
    with open('alumnos_data.pkl', 'wb') as file:
        pickle.dump(lista_alumnos, file)

def cargar_alumnos():
    try:
        with open('alumnos_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


