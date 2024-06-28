import utilidades
import os

# Alumnos guardados en la aplicación
alumnos = []

def registrar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    nivel = input("Ingrese el nivel del alumno (Ejemplo: 1°, 2°, 3°, etc.): ")

    # Validaciones básicas
    if not nombre or not apellido or not edad.isdigit() or not nivel:
        print("Datos ingresados incorrectamente. Por favor, intente de nuevo.")
        return

    edad = int(edad)
    notas = utilidades.generar_notas()

    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nivel": nivel,
        "notas": notas
    }
    
    alumnos.append(alumno)
    print("Alumno registrado exitosamente.")

def listar_alumnos():
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}, Apellido: {alumno['apellido']}, Edad: {alumno['edad']}, Nivel: {alumno['nivel']}, Notas: {alumno['notas']}")

def buscar_alumnos_por_nivel():
    nivel = input("Ingrese el nivel a buscar: ")
    encontrados = [alumno for alumno in alumnos if alumno['nivel'] == nivel]
    
    if not encontrados:
        print("No se encontraron alumnos en ese nivel.")
        return

    for alumno in encontrados:
        print(f"Nombre: {alumno['nombre']}, Apellido: {alumno['apellido']}, Edad: {alumno['edad']}, Nivel: {alumno['nivel']}, Notas: {alumno['notas']}")

def calcular_nota_promedio():
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    todas_las_notas = [nota for alumno in alumnos for nota in alumno['notas']]
    promedio = utilidades.calcular_promedio(todas_las_notas)
    print(f"La nota promedio de todos los alumnos es: {promedio:.2f}")

def guardar_datos():
    with open('archivo.txt', 'w') as file:
        for alumno in alumnos:
            file.write(f"{alumno['nombre']},{alumno['apellido']},{alumno['edad']},{alumno['nivel']},{','.join(map(str, alumno['notas']))}\n")

def cargar_datos():
    if os.path.exists('archivo.txt'):
        with open('archivo.txt', 'r') as file:
            for line in file:
                nombre, apellido, edad, nivel, *notas = line.strip().split(',')
                alumno = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "edad": int(edad),
                    "nivel": nivel,
                    "notas": list(map(int, notas))
                }
                alumnos.append(alumno)

def menu():
    cargar_datos()
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Registrar alumno")
        print("2. Listar todos los alumnos")
        print("3. Buscar alumnos por nivel")
        print("4. Calcular la nota promedio de los alumnos")
        print("5. Salir y guardar")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_alumno()
        elif opcion == '2':
            listar_alumnos()
        elif opcion == '3':
            buscar_alumnos_por_nivel()
        elif opcion == '4':
            calcular_nota_promedio()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
