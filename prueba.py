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

        informacionServidor = conexion.get_server_info()
        print("información del servidor: ", informacionServidor)

except mysql.connector.Error as err:
    print("No se conectó!")
    print(err)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión se cerró")
