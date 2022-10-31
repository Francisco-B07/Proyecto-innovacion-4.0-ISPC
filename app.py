# from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for
import modelo
import controlador

app = Flask(__name__)


# ---------------LISTADO ORDENADO POR INTERPRETE---------------
@app.route('/')
def index():
    con = modelo.Conectar()
    listado = con.ListarAlbumes()
    return render_template('index.html', listado=listado)


# ---------------LISTADO ORDENADO POR GENERO---------------
@app.route('/listadoGenero')
def listadoGenero():
    con = modelo.Conectar()
    listado = con.ListarPorGenero()
    return render_template("listadoGenero.html", listado=listado)


# ---------------AGREGAR ÁLBUM---------------
@app.route('/cargar')
def cargar():
    data = controlador.CargarAlbum()
    return render_template("cargar.html", data=data)


@app.route('/agregar_album', methods=['POST'])
def agregar_album():
    if request.method == 'POST':
        codigoAlbum = request.form['codigoAlbum']
        nombre = request.form['nombre']
        interprete = request.form['interprete']
        genero = request.form['genero']
        cantidadTemas = request.form['cantidadTemas']
        discografica = request.form['discografica']
        formato = request.form['formato']
        fechaLanzamiento = request.form['fechaLanzamiento']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        caratula = request.form['caratula']

        nuevoAlbum = modelo.Album(0, codigoAlbum, nombre, interprete, genero, cantidadTemas,
                                  discografica, formato, fechaLanzamiento, precio, cantidad, caratula)
        con = modelo.Conectar()
        con.InsertarAlbum(nuevoAlbum)
    return redirect(url_for('index'))


# ---------------EDITAR ÁLBUM---------------
@app.route('/editar/<int:cod_album>')
def editar(cod_album):
    data = controlador.EditarAlbum(cod_album)
    return render_template('editar.html', data=data)


@app.route('/update/<int:id_album>', methods=['POST'])
def update_album(id_album):
    if request.method == 'POST':
        codigoAlbum = request.form['codigoAlbum']
        nombre = request.form['nombre']
        interprete = request.form['interprete']
        genero = request.form['genero']
        cantidadTemas = request.form['cantidadTemas']
        discografica = request.form['discografica']
        formato = request.form['formato']
        fechaLanzamiento = request.form['fechaLanzamiento']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        caratula = request.form['caratula']

        albumEditado = modelo.Album(0, codigoAlbum, nombre, interprete, genero, cantidadTemas,
                                    discografica, formato, fechaLanzamiento, precio, cantidad, caratula)
        con = modelo.Conectar()
        con.EditarAlbum(id_album, albumEditado)
        return redirect(url_for('index'))


# ---------------ELIMINAR ÁLBUM---------------
@app.route('/eliminar/<int:cod_album>')
def eliminar(cod_album):
    con = modelo.Conectar()
    con.EliminarAlbum(cod_album)
    return redirect(url_for('index'))


# ---------------BUSCAR ÁLBUM---------------
@app.route('/buscar_album', methods=['POST'])
def buscar_album():
    if request.method == 'POST':
        album = request.form['album']
        album = '%'+album+'%'
        con = modelo.Conectar()
        listado = con.BuscarAlbum(album)
    return render_template('albums-encontrados.html', listado=listado)


# ---------------agregar interprete---------------
@app.route('/agregar_interprete')
def agregar_interprete():
    con = modelo.Conectar()
    # con.InsertarInterprete()
    return render_template("agregar_interprete.html")


@app.route('/add_interprete', methods=['POST'])
def add_interprete():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        nacionalidad = request.form['nacionalidad']
        foto = request.form['foto']
        interprete = modelo.Interprete(0, nombre, apellido, nacionalidad, foto)
        con = modelo.Conectar()
        con.InsertarInterprete(interprete)
    return redirect(url_for('index'))


# ---------------agregar genero---------------
@app.route('/agregar')
def agregar():
    con = modelo.Conectar()
    # con.InsertarInterprete()
    return render_template("agregar.html")


@app.route('/add_genero', methods=['POST'])
def add_genero():
    if request.method == 'POST':
        genero = request.form['genero']
        con = modelo.Conectar()
        con.InsertarGenero(genero)
    return redirect(url_for('index'))


# ---------------agregar discografica---------------
@app.route('/add_discografica', methods=['POST'])
def add_discografica():
    if request.method == 'POST':
        discografica = request.form['discografica']
        con = modelo.Conectar()
        con.InsertarDiscografica(discografica)
    return redirect(url_for('index'))


# ---------------agregar formato---------------
@app.route('/add_formato', methods=['POST'])
def add_formato():
    if request.method == 'POST':
        formato = request.form['formato']
        con = modelo.Conectar()
        con.InsertarFormato(formato)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
