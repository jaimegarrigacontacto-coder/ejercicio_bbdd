import mysql.connector
from carrera import Carrera

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="carreras"
)

mycursor = mydb.cursor()

def consultaSelectAll():
    sql = "SELECT * FROM carreras"
    mycursor.execute(sql)
    return mycursor.fetchall()

def borrarCarrera(idcarrera):
    sql = "DELETE FROM carreras WHERE idcarreras = %s"
    valores = (idcarrera,)
    mycursor.execute(sql, valores)
    mydb.commit()

def setAñadir(nombre, grado, rama):
    carrera = Carrera(nombre, grado, rama)
    sql = "INSERT INTO carreras (nombre, grado, rama) VALUES (%s, %s, %s)"
    valores = (carrera.getNombre(), carrera.getGrado(), carrera.getRama())
    mycursor.execute(sql, valores)
    mydb.commit()

def actualizarCarrera(nom, grad, rm, id):
    carrera = Carrera(nom, grad, rm)
    sql = "UPDATE carreras SET nombre = %s, grado = %s, rama = %s WHERE idcarreras = %s"
    valores = (carrera.getNombre(), carrera.getGrado(), carrera.getRama(), id)
    mycursor.execute(sql, valores)
    mydb.commit()