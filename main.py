from DAO_carreras import *
from carrera import Carrera

opcion = None

while opcion != 0:
    print("1- Añadir carrera\n2- Actualizar carrera\n3- Ver carreras\n4- Borrar carrera\n0- Salir")
    opcion = int(input("Selecciona opción: "))

    if opcion == 1:
        nombre = input("Inserta nombre de la carrera: ")
        grado = input("Inserta el grado de la carrera: ")
        rama = input("Inserta la rama de la carrera: ")
        carrera = Carrera(nombre, grado, rama)
        sql = "INSERT INTO carreras (nombre, grado, rama) VALUES (%s, %s, %s)"
        valores = (carrera.getNombre(), carrera.getGrado(), carrera.getRama())
        mycursor.execute(sql, valores)
        mydb.commit()

        print(f"Se ha insertado {mycursor.rowcount} fila.")

    elif opcion == 2:
        idCarrera = int(input("Inserta el ID de la carrera a actualizar: "))
        nuevoNombre = input("Nuevo nombre: ")
        nuevoGrado = input("Nuevo grado: ")
        nuevaRama = input("Nueva rama: ")
        carrera = Carrera(nuevoNombre, nuevoGrado, nuevaRama)
        sql = "UPDATE carreras SET nombre = %s, grado = %s, rama = %s WHERE idcarreras = %s"
        valores = (carrera.getNombre(), carrera.getGrado(), carrera.getRama(), idCarrera)
        mycursor.execute(sql, valores)
        mydb.commit()

        print(f"Se ha actualizado {mycursor.rowcount} fila.")

    elif opcion == 3:
        sql = "SELECT * FROM carreras"
        mycursor.execute(sql)
        consulta = mycursor.fetchall()
        print("Lista de carreras:")
        for fila in consulta:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Grado: {fila[2]}, Rama: {fila[3]}")

    elif opcion == 4:
        idCarrera = int(input("Inserta el ID de la carrera a borrar: "))
        sql = "DELETE FROM carreras WHERE idcarreras = %s"
        valores = (idCarrera,)
        mycursor.execute(sql, valores)
        mydb.commit()

        print(f"Se ha borrado {mycursor.rowcount} fila.")

    elif opcion == 0:
        print("Saliendo del programa...")