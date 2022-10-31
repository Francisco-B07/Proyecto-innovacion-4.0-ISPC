import modelo


def CargarAlbum():
    con = modelo.Conectar()
    interpretes = con.ListarInterprete()
    generos = con.ListarGenero()
    discografica = con.ListarDiscografica()
    formato = con.ListarFormato()
    data = (interpretes, generos, discografica, formato)
    return data


def EditarAlbum(cod_album):
    con = modelo.Conectar()
    interpretes = con.ListarInterprete()
    generos = con.ListarGenero()
    discograficas = con.ListarDiscografica()
    formatos = con.ListarFormato()
    album = con.ObtenerAlbum(cod_album)
    album = album[0]
    interprete = con.ObtenerInterprete(album[3])
    nombreInterprete = interprete[0][1] + ' ' + interprete[0][2]
    genero = con.ObtenerGenero(album[4])
    genero = genero[0][1]
    discografica = con.ObtenerDiscografica(album[6])
    discografica = discografica[0][1]
    formato = con.ObtenerFormato(album[7])
    formato = formato[0][1]
    data = (interpretes, generos, discograficas,
            formatos, album, nombreInterprete, genero, discografica, formato)
    return data


# def ListarAlbumesPorArtistas():
#     con = modelo.Conectar()
#     listado = con.ListarAlbumes()
#     print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
#     for album in listado:
#         print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
#     input("Presione ENTER para continuar")

# def ListarAlbumesPorGenero():
#     con = modelo.Conectar()
#     listado = con.ListarPorGenero()
#     print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
#     for album in listado:
#         print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
#     input("Presione ENTER para continuar")

# def EliminarAlbum():
#     con = modelo.Conectar()
#     listado = con.ListarPorGenero()
#     print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
#     for album in listado:
#         print(' ', album[0], "\t", album[1], "\t\t", album[2]+' '+album[3], "\t\t  ",
#               album[4], "\t", album[5], " $", album[6], " Cant:", album[7], " ", album[8])
#     cod_album = int(input("Ingrese el código del album a borrar: "))
#     con.EliminarAlbum(cod_album)
#     con.conexion.close()
#     input("Presione ENTER para continuar")


# def InsertarAlbum():
#     cod_album = int(input("\nIngrese el código del nuevo Álbum: "))
#     nombre = input("Ingrese el nombre del álbum: ")

#     con = modelo.Conectar()

#     print("\nIntérpretes Disponibles:")

#     for i in con.ListarInterprete():
#         print(i)
#     id_interprete = int(input("\nIngrese el ID del Intérprete: "))

#     print("\nGénero")
#     for g in con.ListarGenero():
#         print(g)
#     id_genero = int(input("\nIngrese el ID del Género: "))

#     cant_temas = int(input("\nIngrese la cantidad de temas: "))

#     print("\nDiscográfica")
#     for d in con.ListarDiscografica():
#         print(d)
#     id_discografica = int(input("\nIngrese el ID de la discografica: "))

#     print("\nFormato")
#     for f in con.ListarFormato():
#         print(f)

#     id_formato = int(input("\nIngrese el ID del formato: "))
#     fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
#     precio = float(input("\nIngrese el precio: "))
#     cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
#     caratula = input("\nIngrese la dirección web de la Carátula: ")

#     nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
#     con.InsertarAlbum(nuevoAlbum)
#     input("Presione ENTER para continuar")
