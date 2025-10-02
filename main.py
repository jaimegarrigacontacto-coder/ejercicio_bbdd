from DAO_carreras import *
from carrera import Carrera

opcion = None

while opcion != 0:
    print("1- Añadir carrera\n2- Actualizar carrera\n3- Ver carreras\n4- Borrar carrera\n0- Salir")
    opcion = int(input("Selecciona opción: "))

    if opcion == 1:
        nombreCarrera = input("Inserta nombre de la carrera: ")
        sql = "INSERT INTO carreras (nombre) VALUES (%s)"
        valores = [nombreCarrera]
        mycursor.execute(sql, valores)

        mydb.commit()
        print(f"Se ha(n) insertado {mycursor.rowcount} fila(s).")

    if opcion == 3:
        nombreCarrera = input("Inserta nombre de la carrera: ")
        sql = f"SELECT * FROM carreras WHERE nombre LIKE '{nombreCarrera}'"
        mycursor.execute(sql)
        consulta = mycursor.fetchall()

        for fila in consulta:
            print(fila)