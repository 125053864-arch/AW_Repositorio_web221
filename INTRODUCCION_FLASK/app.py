
# Importamos los paquetes de Flask
from flask import Flask, render_template, request, url_for, redirect, session

from werkzeug.security import generate_password_hash, check_password_hash

from flask_mysqldb import MySQL


# Creamos una instancia de nuestra aplicacion
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'FlaskDB'
app.config['TEMPLATE_AUTO_RELOAD'] = True

app.secret_key = 'mysecretkey'

mysql = MySQL(app)


# Ruta principal
@app.route("/")
def home():
    return render_template("login.html")


# Ruta de registro
@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password = request.form["password"]
        id_rol = request.form["id_rol"]

        # Encriptamos la contraseña
        password_hasheada = generate_password_hash(password)

        cursor = mysql.connection.cursor()

        # Buscamos si el correo ya existe
        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )

        if cursor.fetchone():
            cursor.close()
            return render_template("registro.html", mensaje="El correo ya está registrado")

        # Insertamos el nuevo usuario
        cursor.execute(
            """INSERT INTO usuarios
            (nombre, apellido_p, apellido_m, correo, password, id_rol)
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                nombre,
                apellido_p,
                apellido_m,
                correo,
                password_hasheada,
                id_rol
            )
        )

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("home"))

    return render_template("registro.html")


# Ruta de inicio de sesion
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        correo = request.form["correo"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()

        # Consulta para buscar al usuario por su correo
        sql = """
            SELECT
                usuarios.id,
                usuarios.nombre,
                usuarios.apellido_p,
                usuarios.apellido_m,
                usuarios.correo,
                usuarios.password,
                roles.nombre
            FROM usuarios
            INNER JOIN roles
            ON usuarios.id_rol = roles.id_rol
            WHERE usuarios.correo = %s
        """

        cursor.execute(sql, (correo,))

        usuario = cursor.fetchone()

        cursor.close()

        # Comprobamos si el usuario existe y su contraseña es correcta
        if usuario and check_password_hash(usuario[5], password):

            session["id_usuario"] = usuario[0]
            session["nombre"] = usuario[1]
            session["rol"] = usuario[6]

            if session["rol"] == "Administrador":
                return redirect(url_for("admin"))

            return redirect(url_for("usuario"))

        return render_template("login.html", mensaje="Correo o contraseña incorrectos")

    return render_template("login.html")


# Ruta del administrador
@app.route("/admin")
def admin():

    if "id_usuario" not in session:
        return redirect(url_for("login"))

    if session.get("rol") != "Administrador":
        return "Acceso denegado"

    return render_template(
        "administrador.html",
        nombre=session["nombre"]
    )


# Ruta del usuario normal
@app.route("/usuario")
def usuario():

    if "id_usuario" not in session:
        return redirect(url_for("login"))

    return render_template(
        "usuario.html",
        nombre=session["nombre"]
    )


# Cerrar sesion
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# Iniciamos el servidor Flask en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000, debug=True)


