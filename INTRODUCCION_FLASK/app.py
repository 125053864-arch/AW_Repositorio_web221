#importamos los paquetes de flask
from flask import Flask, render_template, request, url_for, redirect, session

from werkzeug.security import generate_password_hash, check_password_hash

from flask_mysqldb import MySQL
#Ceamos una instancia de nuestra aplicacion
app = Flask(__name__)
app.config['MYSQL_HOST']= 'LOCALHOST'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'FlaskDB'
app.config['TEMPLATE_AUTO_RELOAD']= 'FlaskDB'
app.secret_key= 'mysecretkey'
mysql = MySQL(app)



#Creacion de ruta. La ruta / es la ruta raiz, sera la que se mostrara cuando el proyecto 
@app.route("/")
def home():
    return render_template("login.html")
@app.route("/registro",methods=["GET","POST"])
def registro():
 
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password = request.form["pasword"]
        id_rol = request.form["id_rol"]

        password_hasheada = generate_password_hash(password)

        cursor = mysql.connection.cursor()

        cursor.execute(
            "select id from usuarios where correo = %s", (correo,)
            )

        if cursor.fetchone():
            cursor.close()

            return render_template(
                "registro.html"
            )
        cursor.excute(
            """INSERT INTO usuarios
            (nombre, apellido_p,apellido_m, correo, password, id_rol)
            VALUES(%s,%s,%s,%s,%s,%s)""",
            (
                nombre,
                apellido_p,
                apellido_m,
                correo,
                password,
                id_rol
            )
        )

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("home"))
    return render_template("registro")

@app.route("/login", method=["Get", "POST"])
def login():

    if request.method == "POST":

        correo = request.form["correo"]
        password =request.form["passwoed"]

        cursor = mysql.connection.cursor()
        #consula para buscar al usuario por su correo 

        sql = """
            SELECT  
            usuarios.id,
            usuarios.nombre,
            usuarios.apellido_p,
            usuarios.apellido_m,
            usuarios.correo,
            usuarios.password
            roles.nombre
            FROM usuarios
            INNER JOIN id_rol
            ON usuarios.id_rol = roles.id_rol
            WHERE usuarios.correo = %s
        """

        cursor.Execute(sql, (correo,))

        usuario = cursor.fetchone()

        cursor.close()

        if usuario and check_password_hash(usuario[5], password):

            session["id_usuario"] = usuario[0]

            session["nombre"] = usuario[1]

            session["rol"] = usuario[6]

            if session["rol"] == "Administrador":
                return redirect(url_for("admin"))

            return redirect(url_for("usuario"))
        return render_template("login.html")

@app.route("/admin")
def admin():

    if "id_usuario" not in session:
        return redirect(url_for("login"))

    if session.get("rol" != "Administrador"):
        return "Acceso denegado"
    return render_template(
        "administrador.html",
        nombre=session["nombre"])











#iniciamos el servidor Flask en el puesto 5000

if __name__ == "__main__":
    app.run(port=5000)

