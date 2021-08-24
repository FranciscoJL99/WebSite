import sqlite3

def createDataBase():
    miConexion = sqlite3.connect("PageDatabase")
    miCursor = miConexion.cursor()
    miCursor.execute("CREATE TABLE PONENTES (NOMBRE VARCHAR(50), TEMA VARCHAR(50), FECHA VARCHAR(30), MEET VARCHAR(50))")
    miConexion.close()
    return 'SE CREO CON EXITO LA BASE DE DATOS'

def insertResults(name, tema, fecha, meet):
    miConexion = sqlite3.connect("PageDatabase")
    miCursor = miConexion.cursor()
    query = str("INSERT INTO PONENTES VALUES('"+name+"', '"+tema+"', '"+fecha+"', '"+meet+"')")
    print ("QUERY A EJECUTAR: ", query)
    miCursor.execute(query)
    print(" SE INSERTARON LOS DATOS DE FORMA EXITOSA")
    miConexion.commit()
    miConexion.close()

def consulta(name):
    miConexion = sqlite3.connect("PageDatabase")
    miCursor = miConexion.cursor()
    query = str("SELECT "+name+" FROM PONENTES")
    print("QUERY A EJECUTAR: ", query)
    consulta = miCursor.execute(query)
    #consulta = miCursor.fetchone()
    consultaOrder = [row[0] for row in consulta]
    print("Resultado de la consulta: ", consulta)
   # miCursor.execute("DELECT FROM NAME= ''")
    miConexion.close()
    return consultaOrder