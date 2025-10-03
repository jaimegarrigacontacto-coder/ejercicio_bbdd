import mysql.connector

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