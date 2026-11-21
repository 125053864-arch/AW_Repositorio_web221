
from flask import Flask, redirect, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_albums'

app.secret_key = 'mysecretkey'

mysql = MySQL(app)


@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_albums')
    conPeliculas = con.fetchall()
    print(conPeliculas)
    return render_template('index.html', listPeliculas= conPeliculas)


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo= request.form['txtTitulo']
        autor= request.form['txtAutor']
        ano= request.form['txtAnio']
        calificacion= request.form['txtCalificacion']
        resena= request.form['txtResena']
        print(titulo,autor,ano,calificacion,resena)

        con = mysql.connection.cursor()
        con.execute('INSERT INTO tb_albums(titulo, autor, ano, calificacion, resena) VALUES(%s,%s,%s,%s,%s)',(titulo,autor,ano,calificacion,resena))
        mysql.connection.commit()

    flash('La pelicula fue agregada correctamente!')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_albums WHERE id=%s', (id,))
    consultarId = con.fetchone()
    con.close()
    return render_template('editarAlbum.html', Pelicula=consultarId)


@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        autor = request.form['txtAutor']
        ano = request.form['txtAnio']
        calificacion = request.form['txtCalificacion']
        resena = request.form['txtResena']

        con = mysql.connection.cursor()
        con.execute('UPDATE tb_albums SET titulo=%s, autor=%s, ano=%s, calificacion=%s, resena=%s WHERE id=%s', (titulo,autor,ano,calificacion,resena,id))
        mysql.connection.commit()
    flash('Se actualizó la pelicula' +titulo)
    return redirect(url_for('index'))


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']

        con = mysql.connection.cursor()
        con.execute('DELETE FROM tb_albums WHERE id=%s', (id,))
        mysql.connection.commit()

    flash('Se eliminó la pelicula '+titulo)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)