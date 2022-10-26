import mysql.connector


class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='disqueria'
            )
            # self.conexion = mysql.connector.connect(
            #     host='sql10.freesqldatabase.com',
            #     port=3306,
            #     user='sql10524202',
            #     password='vpbuQZVVL4',
            #     db='sql10524202'
            # )

        except mysql.connector.Error as err:
            print("No se conectó")
            print(err)

    def ListarAlbums(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT cod_album, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album, interprete, discografica, formato, genero WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero ORDER By album.id_interprete")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as err:
                print("No se conectó")
                print(err)


con = Conectar()

for album in con.ListarAlbums():
    print(album)

# print(con.ListarAlbums())
