# from flask_mysqldb import MySQL
from flask import Flask, render_template, jsonify
import modelo


app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'disqueria'

# conexion = MySQL(app)


@app.route('/')
def index():
    # para usar variables:
    # cursos = ['PHP', 'JAVA', 'JS', 'TS']
    # data = {
    #     'titulo': 'Index',
    #     'bienvenida': 'Saludos',
    #     'cursos': cursos,
    #     'cant_cursos': len(cursos)
    # }
    # despues usamos binding en el HTML
    return render_template('index.html')


@app.route('/listado')
def listado():
    con = modelo.Conectar()
    listado = con.ListarAlbumes()
    return render_template("listado.html", listado=listado)


@app.route('/listadoGenero')
def listadoGenero():
    con = modelo.Conectar()
    listado = con.ListarPorGenero()
    return render_template("listadoGenero.html", listado=listado)


@app.route('/cargar')
def cargar():
    return render_template("cargar.html")


@app.route('/editar/<int:cod_album>')
def editar(cod_album):
    return render_template('editar.html')


@app.route('/eliminar/<int:cod_album>')
def eliminar(cod_album):
    con = modelo.Conectar()
    con.EliminarAlbum(cod_album)
    return render_template('listado.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
