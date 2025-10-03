from DAO_carreras import *
from carrera import Carrera

opcion = None

while opcion != 0:
    print("1- Añadir carrera\n2- Actualizar carrera\n3- Ver carreras\n4- Borrar carrera\n0- Salir")
    opcion = input("\nSelecciona opción: ")
    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("Error. Opción no válida.")

    if opcion == 1:
        nombre = input("Inserta nombre de la carrera: ")
        grado = input("Inserta el grado de la carrera: ")
        rama = input("Inserta la rama de la carrera: ")
        setAñadir(nombre, grado, rama)

        print(f"Se ha insertado {mycursor.rowcount} fila.")

    elif opcion == 2:
        idvalida = False
        while idvalida is not True:
            idCarrera = input("Inserta el ID de la carrera a actualizar: ")
            if idCarrera.isdigit():
                idvalida = True
            else:
                print("Error. ID no válida")
        
        nuevoNombre = input("Nuevo nombre: ")
        nuevoGrado = input("Nuevo grado: ")
        nuevaRama = input("Nueva rama: ")
        actualizarCarrera(nuevoNombre, nuevoGrado, nuevaRama, idCarrera)

        print(f"Se ha actualizado {mycursor.rowcount} fila.")

    elif opcion == 3:
        consulta = consultaSelectAll()
        print("Lista de carreras:")
        for fila in consulta:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Grado: {fila[2]}, Rama: {fila[3]}")

    elif opcion == 4:
        idvalida = False
        while idvalida is not True:
            idCarrera = input("Inserta el ID de la carrera a borrar: ")
            if idCarrera.isdigit():
                idvalida = True
            else:
                print("Error. ID no válida")

        borrarCarrera(idCarrera)

        print(f"Se ha borrado {mycursor.rowcount} fila.")

    elif opcion == 0:
        print("Saliendo del programa...")
