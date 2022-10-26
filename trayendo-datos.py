import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='disqueria'
    )
    if conexion.is_connected():
        print("La conexión fue exitosa.")

        # objeto que hace de enlace entre la BD y nuestro programa
        cursor = conexion.cursor()

        cursor.execute("select * from genero")
        lista = cursor.fetchall()

        for dato in lista:
            print(dato)


except:
    print("No se conectó!")

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión se cerró")
