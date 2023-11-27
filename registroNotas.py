from alumnos import Alumno, cargar_alumnos, guardar_alumnos

def main():
    alumnos = cargar_alumnos()

    while True:
        print("Bienvenidos al registro de notas")
        comando = input("Ingrese comando (R: Registrar, C: Calificar, P: Promedio, S: Suma, X: Salir): ").upper() #La funcion upper() es para transformarlo en mayúsculas 

        if comando == "R":
            nombre = input("Ingrese nombre del alumno: ")
            apellido = input("Ingrese apellido del alumno: ")
            edad = input("Ingrese edad del alumno: ")
            nacionalidad = input("Ingrese nacionalidad del alumno: ")

            nuevo_alumno = Alumno(nombre, apellido, edad, nacionalidad)
            alumnos.append(nuevo_alumno)
            print(f"Alumno {nombre} {apellido} registrado correctamente.")

        elif comando == "C":
            for alumno in alumnos:
                alumno.leerNota()

        elif comando == "P":
            if alumnos:
                promedio = sum(alumno.nota for alumno in alumnos) / len(alumnos)
                print(f"El promedio de notas para {len(alumnos)} alumnos es: {promedio:.2f}")
            else:
                print("No hay alumnos registrados.")

        elif comando == "S":
            if alumnos:
                suma_notas = sum(alumno.nota for alumno in alumnos)
                print(f"La suma de notas de {len(alumnos)} alumnos es: {suma_notas}")
            else:
                print("No hay alumnos registrados.")

        elif comando == "X":
            guardar_alumnos(alumnos)
            print("Programa terminado.")
            break

        else:
            print("Comando no reconocido. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
