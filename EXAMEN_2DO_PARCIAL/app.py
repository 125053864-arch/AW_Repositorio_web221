
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(_name_)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']= 'crud_albums'

app.secret_key = 'mysecrtkey'

mysql = MySQL(app)


@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.Execute('SELECT * FORM tb_albums')
    conAlbums = con.fetchall()
    print(conAlbums)
    return render_template('index.html', listaAlbums= conAlbums)

if_name_=='_main_':
app.run(debug=True)


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo= request.form['TxtTitulo']
        autor= request.form['TxtAutor']
        ano= request.form['TxtAno']
        calificacion= request.form['TxtCalificacion']
        resena= request.form['TxtResena']
        print(titulo,autor,ano,calificacion,resena)

        con = mysql.connection.cursor()
        con.Execute('INSERT INTO tb_albums(titulo, autor, ano, calificacion, resena ) VALUES(%s,%s,%s,%s,%s)',(titulo, autor, ano, calificacion, resena))
        mysql.connection.commit()

    flash('El album fue agregado correctamente!')
    return redirect(url_for('index'))




        
